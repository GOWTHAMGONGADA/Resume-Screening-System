"""
Utility functions for resume screening system
"""
import json
from datetime import datetime


class Utils:
    """Utility functions"""
    
    @staticmethod
    def format_score_for_display(score):
        """
        Format score dictionary for display
        
        Args:
            score (dict): Score dictionary
            
        Returns:
            dict: Formatted score
        """
        return {
            'Overall Score': f"{score['total_score']}/100",
            'Text Match': f"{score['text_similarity_score']}/40",
            'Skills Match': f"{score['skills_score']}/60",
            'Technical Skills Match': f"{score['technical_match_pct']}%",
            'Soft Skills Match': f"{score['soft_match_pct']}%"
        }
    
    @staticmethod
    def generate_report(ranked_resumes, job_description):
        """
        Generate summary report
        
        Args:
            ranked_resumes (list): Ranked resumes from ResumeScorer
            job_description (str): Job description
            
        Returns:
            str: Summary report
        """
        report = f"\n{'='*60}\n"
        report += f"RESUME SCREENING REPORT\n"
        report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"{'='*60}\n\n"
        
        report += f"Job Description Preview:\n{job_description[:200]}...\n\n"
        report += f"Total Resumes Screened: {len(ranked_resumes)}\n\n"
        
        report += f"{'RANK':<6} {'SCORE':<10} {'CANDIDATE':<25} {'TECH MATCH':<12} {'SOFT MATCH':<12}\n"
        report += f"{'-'*60}\n"
        
        for resume in ranked_resumes:
            rank = resume['rank']
            score = resume['score']['total_score']
            name = resume['name'][:23]
            tech = f"{resume['score']['technical_match_pct']}%"
            soft = f"{resume['score']['soft_match_pct']}%"
            
            report += f"{rank:<6} {score:<10.2f} {name:<25} {tech:<12} {soft:<12}\n"
        
        report += f"\n{'='*60}\n"
        report += "Top Candidate Analysis:\n"
        
        if ranked_resumes:
            top = ranked_resumes[0]
            report += f"\nCandidate: {top['name']}\n"
            report += f"Overall Score: {top['score']['total_score']}/100\n"
            report += f"Text Similarity: {top['score']['text_similarity_score']}/40\n"
            report += f"Skills Score: {top['score']['skills_score']}/60\n"
            report += f"\nMatched Technical Skills: {', '.join(top['skill_matches']['matched_technical']) if top['skill_matches']['matched_technical'] else 'None'}\n"
            report += f"Missing Technical Skills: {', '.join(top['skill_matches']['missing_technical']) if top['skill_matches']['missing_technical'] else 'None'}\n"
            report += f"\nMatched Soft Skills: {', '.join(top['skill_matches']['matched_soft']) if top['skill_matches']['matched_soft'] else 'None'}\n"
            report += f"Missing Soft Skills: {', '.join(top['skill_matches']['missing_soft']) if top['skill_matches']['missing_soft'] else 'None'}\n"
        
        report += f"\n{'='*60}\n"
        
        return report
    
    @staticmethod
    def export_results_json(ranked_resumes, job_description):
        """
        Export results as JSON
        
        Args:
            ranked_resumes (list): Ranked resumes
            job_description (str): Job description
            
        Returns:
            str: JSON string
        """
        export_data = {
            'timestamp': datetime.now().isoformat(),
            'job_description_preview': job_description[:500],
            'total_resumes': len(ranked_resumes),
            'results': []
        }
        
        for resume in ranked_resumes:
            export_data['results'].append({
                'rank': resume['rank'],
                'name': resume['name'],
                'score': resume['score'],
                'skill_matches': resume['skill_matches']
            })
        
        return json.dumps(export_data, indent=2)
