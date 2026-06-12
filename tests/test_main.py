"""
Unit tests for Resume Screening System
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from text_processor import TextProcessor
from skill_extractor import SkillExtractor
from resume_scorer import ResumeScorer


class TestTextProcessor:
    """Test text processing functions"""
    
    def setup_method(self):
        self.processor = TextProcessor()
    
    def test_clean_text(self):
        """Test text cleaning"""
        text = "Hello World! Visit https://example.com or email test@example.com"
        cleaned = self.processor.clean_text(text)
        
        assert "example.com" not in cleaned
        assert "hello world" in cleaned.lower()
        assert len(cleaned) < len(text)
    
    def test_tokenize(self):
        """Test tokenization"""
        text = "Python is great"
        tokens = self.processor.tokenize(text)
        
        assert isinstance(tokens, list)
        assert len(tokens) > 0
    
    def test_process_text(self):
        """Test full text processing"""
        text = "I have 5 years of experience with Python and Java"
        tokens = self.processor.process_text(text)
        
        assert isinstance(tokens, list)
        assert "python" in [t.lower() for t in tokens]
        assert "java" in [t.lower() for t in tokens]


class TestSkillExtractor:
    """Test skill extraction"""
    
    def setup_method(self):
        self.extractor = SkillExtractor()
    
    def test_extract_technical_skills(self):
        """Test technical skill extraction"""
        text = "Proficient in Python, Java, JavaScript, React, and Docker"
        skills = self.extractor.extract_skills(text)
        
        assert 'technical' in skills
        assert 'python' in skills['technical']
        assert 'java' in skills['technical']
        assert 'react' in skills['technical']
    
    def test_extract_soft_skills(self):
        """Test soft skill extraction"""
        text = "Strong communication and leadership abilities with excellent teamwork"
        skills = self.extractor.extract_skills(text)
        
        assert 'soft' in skills
        assert 'communication' in skills['soft']
        assert 'leadership' in skills['soft']
    
    def test_get_skill_matches(self):
        """Test skill matching"""
        resume_skills = {
            'technical': {'python': 1, 'java': 1},
            'soft': {'communication': 1}
        }
        job_skills = {
            'technical': {'python': 1, 'docker': 1},
            'soft': {'communication': 1, 'leadership': 1}
        }
        
        matches = self.extractor.get_skill_matches(resume_skills, job_skills)
        
        assert 'python' in matches['matched_technical']
        assert 'docker' in matches['missing_technical']
        assert 'communication' in matches['matched_soft']
        assert 'leadership' in matches['missing_soft']


class TestResumeScorer:
    """Test resume scoring"""
    
    def setup_method(self):
        self.scorer = ResumeScorer()
    
    def test_calculate_similarity(self):
        """Test similarity calculation"""
        text1 = "Python Java React Docker AWS"
        text2 = "Python Java JavaScript Node.js AWS"
        
        similarity = self.scorer.calculate_similarity(text1, text2)
        
        assert 0 <= similarity <= 1
        assert similarity > 0  # Should have some similarity
    
    def test_score_resume(self):
        """Test resume scoring"""
        job_desc = "Need Python and Docker experience"
        resume_text = "I have 5 years Python and Docker skills"
        skills_match = {
            'matched_technical': ['python', 'docker'],
            'missing_technical': ['kubernetes'],
            'matched_soft': ['communication'],
            'missing_soft': ['leadership']
        }
        
        score = self.scorer.score_resume(job_desc, resume_text, skills_match)
        
        assert 'total_score' in score
        assert 'text_similarity_score' in score
        assert 'skills_score' in score
        assert 0 <= score['total_score'] <= 100


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
