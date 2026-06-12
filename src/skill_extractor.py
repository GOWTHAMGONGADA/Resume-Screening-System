"""
Skill extraction module for identifying technical and soft skills
"""
import re
from collections import defaultdict


class SkillExtractor:
    """Extracts skills from resume and job description text"""
    
    def __init__(self):
        # Comprehensive skill dictionary
        self.technical_skills = {
            # Programming Languages
            'python': ['python', 'py'],
            'java': ['java'],
            'javascript': ['javascript', 'js', 'node', 'nodejs'],
            'csharp': ['c#', 'csharp', 'c sharp'],
            'cpp': ['c++', 'cpp'],
            'php': ['php'],
            'ruby': ['ruby'],
            'go': ['golang', 'go'],
            'rust': ['rust'],
            'scala': ['scala'],
            'r': ['r programming', 'r language'],
            
            # Web Development
            'react': ['react', 'reactjs'],
            'angular': ['angular'],
            'vue': ['vue', 'vuejs'],
            'django': ['django'],
            'flask': ['flask'],
            'fastapi': ['fastapi'],
            'express': ['express', 'expressjs'],
            'html': ['html', 'html5'],
            'css': ['css', 'css3'],
            'sass': ['sass', 'scss'],
            'webpack': ['webpack'],
            
            # Databases
            'sql': ['sql', 'tsql'],
            'mysql': ['mysql'],
            'postgresql': ['postgresql', 'postgres'],
            'mongodb': ['mongodb', 'mongo'],
            'redis': ['redis'],
            'elasticsearch': ['elasticsearch'],
            'cassandra': ['cassandra'],
            'oracle': ['oracle'],
            
            # Cloud & DevOps
            'aws': ['aws', 'amazon web services'],
            'azure': ['azure', 'microsoft azure'],
            'gcp': ['gcp', 'google cloud', 'google cloud platform'],
            'docker': ['docker'],
            'kubernetes': ['kubernetes', 'k8s'],
            'jenkins': ['jenkins'],
            'git': ['git', 'github', 'gitlab'],
            'terraform': ['terraform'],
            'ansible': ['ansible'],
            
            # Data & ML
            'tensorflow': ['tensorflow'],
            'pytorch': ['pytorch'],
            'keras': ['keras'],
            'scikit-learn': ['scikit-learn', 'sklearn'],
            'pandas': ['pandas'],
            'numpy': ['numpy'],
            'spark': ['spark', 'apache spark'],
            'hadoop': ['hadoop'],
            'matplotlib': ['matplotlib'],
            'seaborn': ['seaborn'],
            'jupyter': ['jupyter', 'ipython'],
            'machine learning': ['machine learning', 'ml'],
            'deep learning': ['deep learning'],
            'nlp': ['nlp', 'natural language processing'],
            'cv': ['computer vision', 'cv'],
            
            # Big Data & Analytics
            'hive': ['hive'],
            'pig': ['pig'],
            'tableau': ['tableau'],
            'powerbi': ['power bi', 'powerbi'],
            'excel': ['excel', 'ms excel'],
            'sap': ['sap'],
            'salesforce': ['salesforce'],
            
            # Testing & QA
            'junit': ['junit'],
            'pytest': ['pytest'],
            'selenium': ['selenium'],
            'jira': ['jira'],
            'testng': ['testng'],
            
            # Other Tools
            'linux': ['linux'],
            'unix': ['unix'],
            'windows': ['windows'],
            'macos': ['macos', 'mac os'],
            'rest': ['rest', 'restful'],
            'graphql': ['graphql'],
            'json': ['json'],
            'xml': ['xml'],
            'soap': ['soap'],
            'api': ['api', 'apis'],
            'microservices': ['microservices'],
            'monolithic': ['monolithic'],
            'agile': ['agile'],
            'scrum': ['scrum'],
            'kanban': ['kanban'],
            'ci/cd': ['ci/cd', 'continuous integration', 'continuous deployment'],
            'devops': ['devops'],
        }
        
        self.soft_skills = {
            'communication': ['communication', 'communicate'],
            'leadership': ['leadership', 'lead'],
            'teamwork': ['teamwork', 'team work', 'team player'],
            'problem-solving': ['problem solving', 'problem-solving'],
            'analytical': ['analytical', 'analysis'],
            'creativity': ['creativity', 'creative'],
            'time management': ['time management', 'time-management'],
            'critical thinking': ['critical thinking'],
            'attention to detail': ['attention to detail'],
            'collaboration': ['collaboration', 'collaborate'],
            'adaptability': ['adaptability', 'adaptable'],
            'customer service': ['customer service'],
            'project management': ['project management'],
        }
    
    def extract_skills(self, text):
        """
        Extract skills from text
        
        Args:
            text (str): Text to extract skills from
            
        Returns:
            dict: Dictionary with extracted skills
        """
        text = text.lower()
        
        extracted_technical = defaultdict(int)
        extracted_soft = defaultdict(int)
        
        # Extract technical skills
        for skill, keywords in self.technical_skills.items():
            for keyword in keywords:
                # Use word boundary to match whole words
                pattern = r'\b' + re.escape(keyword) + r'\b'
                matches = len(re.findall(pattern, text))
                if matches > 0:
                    extracted_technical[skill] += matches
        
        # Extract soft skills
        for skill, keywords in self.soft_skills.items():
            for keyword in keywords:
                pattern = r'\b' + re.escape(keyword) + r'\b'
                matches = len(re.findall(pattern, text))
                if matches > 0:
                    extracted_soft[skill] += matches
        
        # Keep only skills that were found
        return {
            'technical': dict(extracted_technical),
            'soft': dict(extracted_soft)
        }
    
    def get_all_skills(self, skills_dict):
        """
        Get combined list of all skills
        
        Args:
            skills_dict (dict): Skills dictionary from extract_skills
            
        Returns:
            list: All extracted skills
        """
        all_skills = list(skills_dict.get('technical', {}).keys()) + \
                     list(skills_dict.get('soft', {}).keys())
        return all_skills
    
    def get_skill_matches(self, resume_skills, job_skills):
        """
        Find skill matches between resume and job
        
        Args:
            resume_skills (dict): Skills from resume
            job_skills (dict): Skills from job description
            
        Returns:
            dict: Matched and missing skills
        """
        resume_technical = set(resume_skills.get('technical', {}).keys())
        resume_soft = set(resume_skills.get('soft', {}).keys())
        
        job_technical = set(job_skills.get('technical', {}).keys())
        job_soft = set(job_skills.get('soft', {}).keys())
        
        matched_technical = resume_technical & job_technical
        missing_technical = job_technical - resume_technical
        
        matched_soft = resume_soft & job_soft
        missing_soft = job_soft - resume_soft
        
        return {
            'matched_technical': sorted(list(matched_technical)),
            'missing_technical': sorted(list(missing_technical)),
            'matched_soft': sorted(list(matched_soft)),
            'missing_soft': sorted(list(missing_soft))
        }
