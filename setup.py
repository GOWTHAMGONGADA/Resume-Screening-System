"""
Setup script for Resume Screening System
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="resume-screening-system",
    version="1.0.0",
    author="ML Team",
    author_email="your.email@example.com",
    description="Automated Resume Screening & Ranking System using ML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/FUTURE_ML_03",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Business",
        "Topic :: Office/Business :: News/Diary",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "nltk>=3.6.0",
        "PyPDF2>=1.26.0",
        "python-docx>=0.8.11",
        "streamlit>=1.10.0",
        "joblib>=1.1.0",
        "requests>=2.26.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0",
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
        ],
    },
)
