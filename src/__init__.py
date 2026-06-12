"""
Resume Screening System - ML Pipeline
Track: ML (Machine Learning)
Task: FUTURE_ML_03

A production-ready system for automated resume screening and candidate ranking
using Natural Language Processing and Machine Learning.
"""

__version__ = "1.0.0"
__author__ = "ML Team"
__description__ = "Automated Resume Screening & Ranking System"

from .text_processor import TextProcessor
from .skill_extractor import SkillExtractor
from .resume_scorer import ResumeScorer
from .file_handler import FileHandler
from .utils import Utils

__all__ = [
    'TextProcessor',
    'SkillExtractor',
    'ResumeScorer',
    'FileHandler',
    'Utils'
]
