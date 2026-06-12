"""
Resume scoring and ranking module
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class ResumeScorer:
    """Scores and ranks resumes against job descriptions"""
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=100,
            stop_words='english',
            ngram_range=(1, 2)
        )
    
    def calculate_similarity(self, text1, text2):
        """
        Calculate cosine similarity between two texts
        
        Args:
            text1 (str): First text (job description)
            text2 (str): Second text (resume)
            
        Returns:
            float: Similarity score between 0 and 1
        """
        try:
            # Vectorize both texts
            tfidf_matrix = self.vectorizer.fit_transform([text1, text2])
            
            # Calculate cosine similarity
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            
            return float(similarity)
        except Exception as e:
            print(f"Error calculating similarity: {e}")
            return 0.0
    
    def score_resume(self, job_description, resume_text, skills_match):
        """
        Calculate comprehensive score for a resume
        
        Args:
            job_description (str): Job description text
            resume_text (str): Resume text
            skills_match (dict): Skills match result from SkillExtractor
            
        Returns:
            dict: Detailed score breakdown
        """
        # Text similarity score (40% weight)
        text_similarity = self.calculate_similarity(job_description, resume_text)
        text_score = text_similarity * 40
        
        # Skills matching score (60% weight)
        matched_technical = len(skills_match.get('matched_technical', []))
        missing_technical = len(skills_match.get('missing_technical', []))
        matched_soft = len(skills_match.get('matched_soft', []))
        missing_soft = len(skills_match.get('missing_soft', []))
        
        # Calculate total required skills
        total_job_technical = matched_technical + missing_technical
        total_job_soft = matched_soft + missing_soft
        
        # Calculate match percentages
        if total_job_technical > 0:
            technical_match_pct = (matched_technical / total_job_technical) * 100
        else:
            technical_match_pct = 0
        
        if total_job_soft > 0:
            soft_match_pct = (matched_soft / total_job_soft) * 100
        else:
            soft_match_pct = 0
        
        # Skills score (average of technical and soft skill matches)
        if total_job_technical > 0 or total_job_soft > 0:
            avg_skill_match = (technical_match_pct + soft_match_pct) / 2
            skills_score = (avg_skill_match / 100) * 60
        else:
            skills_score = 0
        
        # Total score
        total_score = text_score + skills_score
        
        return {
            'total_score': round(total_score, 2),
            'text_similarity_score': round(text_score, 2),
            'skills_score': round(skills_score, 2),
            'technical_match_pct': round(technical_match_pct, 2),
            'soft_match_pct': round(soft_match_pct, 2),
            'matched_technical': matched_technical,
            'missing_technical': missing_technical,
            'matched_soft': matched_soft,
            'missing_soft': missing_soft
        }
    
    def rank_resumes(self, job_description, resume_list, skill_extractor):
        """
        Rank multiple resumes against a job description
        
        Args:
            job_description (str): Job description text
            resume_list (list): List of resume texts with metadata
            skill_extractor: SkillExtractor instance
            
        Returns:
            list: Ranked resumes with scores
        """
        job_skills = skill_extractor.extract_skills(job_description)
        
        ranked_resumes = []
        
        for i, resume in enumerate(resume_list):
            resume_text = resume.get('text', '')
            resume_name = resume.get('name', f'Resume_{i+1}')
            
            # Extract skills from resume
            resume_skills = skill_extractor.extract_skills(resume_text)
            
            # Get skill matches
            skill_matches = skill_extractor.get_skill_matches(resume_skills, job_skills)
            
            # Score the resume
            score = self.score_resume(job_description, resume_text, skill_matches)
            
            ranked_resumes.append({
                'name': resume_name,
                'score': score,
                'skill_matches': skill_matches,
                'resume_skills': resume_skills
            })
        
        # Sort by total score (descending)
        ranked_resumes.sort(key=lambda x: x['score']['total_score'], reverse=True)
        
        # Add rank
        for rank, resume in enumerate(ranked_resumes, 1):
            resume['rank'] = rank
        
        return ranked_resumes
