"""
Streamlit application for Resume Screening System
Run with: streamlit run app.py
"""
import streamlit as st
import sys
import os
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from text_processor import TextProcessor
from skill_extractor import SkillExtractor
from resume_scorer import ResumeScorer
from file_handler import FileHandler
from utils import Utils

# Page configuration
st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        padding: 20px;
    }
    .score-high {
        color: #28a745;
        font-weight: bold;
    }
    .score-medium {
        color: #ffc107;
        font-weight: bold;
    }
    .score-low {
        color: #dc3545;
        font-weight: bold;
    }
    .matched-skill {
        background-color: #d4edda;
        padding: 5px 10px;
        border-radius: 5px;
        margin: 2px;
        display: inline-block;
    }
    .missing-skill {
        background-color: #f8d7da;
        padding: 5px 10px;
        border-radius: 5px;
        margin: 2px;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'job_description' not in st.session_state:
    st.session_state.job_description = ""
if 'results' not in st.session_state:
    st.session_state.results = None
if 'resumes' not in st.session_state:
    st.session_state.resumes = []

# Header
st.markdown("<h1 class='main-header'>📄 Resume Screening System</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select Page:", ["Home", "Upload & Screen", "Results", "About"])

# Initialize components
text_processor = TextProcessor()
skill_extractor = SkillExtractor()
resume_scorer = ResumeScorer()
file_handler = FileHandler()

# Home Page
if page == "Home":
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🎯 What is This?")
        st.info("""
        This is an AI-powered Resume Screening System that:
        
        ✅ **Analyzes** resumes and job descriptions
        ✅ **Extracts** technical and soft skills
        ✅ **Scores** resumes based on job fit
        ✅ **Ranks** candidates automatically
        ✅ **Identifies** skill gaps for each candidate
        """)
    
    with col2:
        st.header("🚀 How It Works")
        st.info("""
        1. **Upload** a job description (PDF/DOCX/TXT)
        2. **Upload** multiple resumes (PDF/DOCX/TXT)
        3. **Screen** - System analyzes and scores each resume
        4. **Review** - See ranked candidates with skill analysis
        5. **Export** - Download detailed results
        """)
    
    st.header("📊 Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Text Analysis
        - Advanced NLP processing
        - Semantic similarity matching
        - Content relevance scoring
        """)
    
    with col2:
        st.markdown("""
        ### Skill Extraction
        - 50+ technical skills
        - Soft skills assessment
        - Skill gap analysis
        """)
    
    with col3:
        st.markdown("""
        ### Intelligent Ranking
        - Composite scoring
        - Weighted metrics
        - Candidate comparison
        """)

# Upload & Screen Page
elif page == "Upload & Screen":
    st.header("📤 Upload Documents")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Job Description")
        job_file = st.file_uploader(
            "Upload Job Description",
            type=['txt', 'pdf', 'docx'],
            key='job_file'
        )
        
        if job_file is not None:
            try:
                job_content = job_file.read()
                st.session_state.job_description = file_handler.read_text_file(
                    job_content,
                    job_file.name
                )
                st.success("✅ Job description uploaded successfully!")
                
                with st.expander("Preview Job Description"):
                    st.text(st.session_state.job_description[:500])
            except Exception as e:
                st.error(f"❌ Error reading job file: {str(e)}")
        
        if st.session_state.job_description:
            st.write(f"📝 Characters: {len(st.session_state.job_description)}")
    
    with col2:
        st.subheader("Resumes")
        resume_files = st.file_uploader(
            "Upload Resumes",
            type=['txt', 'pdf', 'docx'],
            accept_multiple_files=True,
            key='resume_files'
        )
        
        if resume_files:
            st.session_state.resumes = []
            for resume_file in resume_files:
                try:
                    resume_content = resume_file.read()
                    resume_text = file_handler.read_text_file(
                        resume_content,
                        resume_file.name
                    )
                    st.session_state.resumes.append({
                        'name': resume_file.name,
                        'text': resume_text
                    })
                except Exception as e:
                    st.error(f"❌ Error reading {resume_file.name}: {str(e)}")
            
            if st.session_state.resumes:
                st.success(f"✅ {len(st.session_state.resumes)} resume(s) uploaded!")
    
    st.markdown("---")
    
    # Screening button
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🔍 Screen Resumes", use_container_width=True):
            if not st.session_state.job_description:
                st.error("❌ Please upload a job description first!")
            elif not st.session_state.resumes:
                st.error("❌ Please upload at least one resume!")
            else:
                with st.spinner("⏳ Screening resumes..."):
                    try:
                        # Rank resumes
                        ranked_resumes = resume_scorer.rank_resumes(
                            st.session_state.job_description,
                            st.session_state.resumes,
                            skill_extractor
                        )
                        
                        st.session_state.results = ranked_resumes
                        st.success("✅ Screening complete! Go to Results tab to see rankings.")
                    except Exception as e:
                        st.error(f"❌ Error during screening: {str(e)}")

# Results Page
elif page == "Results":
    if st.session_state.results is None:
        st.info("📋 No results yet. Please screen resumes first from the 'Upload & Screen' page.")
    else:
        st.header("📊 Screening Results")
        
        # Overall Statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Candidates", len(st.session_state.results))
        
        with col2:
            avg_score = sum(r['score']['total_score'] for r in st.session_state.results) / len(st.session_state.results)
            st.metric("Average Score", f"{avg_score:.2f}/100")
        
        with col3:
            top_score = st.session_state.results[0]['score']['total_score']
            st.metric("Top Score", f"{top_score:.2f}/100")
        
        with col4:
            st.metric("Job Description Uploaded", "✅" if st.session_state.job_description else "❌")
        
        st.markdown("---")
        
        # Candidate Rankings
        st.subheader("🏆 Candidate Rankings")
        
        for idx, resume in enumerate(st.session_state.results):
            with st.expander(
                f"#{resume['rank']} - {resume['name']} | Score: {resume['score']['total_score']}/100",
                expanded=(idx == 0)
            ):
                col1, col2, col3 = st.columns(3)
                
                # Score Breakdown
                with col1:
                    st.markdown("### Score Breakdown")
                    
                    score = resume['score']['total_score']
                    if score >= 70:
                        score_class = "score-high"
                        status = "🟢 Excellent Match"
                    elif score >= 50:
                        score_class = "score-medium"
                        status = "🟡 Good Match"
                    else:
                        score_class = "score-low"
                        status = "🔴 Weak Match"
                    
                    st.markdown(f"<h3 class='{score_class}'>{score}/100</h3>", unsafe_allow_html=True)
                    st.markdown(f"**{status}**")
                    
                    st.metric("Text Similarity", f"{resume['score']['text_similarity_score']}/40")
                    st.metric("Skills Match", f"{resume['score']['skills_score']}/60")
                
                # Skills Breakdown
                with col2:
                    st.markdown("### Skills Match")
                    
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        st.metric(
                            "Technical Skills",
                            f"{resume['score']['technical_match_pct']}%"
                        )
                    
                    with col_b:
                        st.metric(
                            "Soft Skills",
                            f"{resume['score']['soft_match_pct']}%"
                        )
                    
                    st.markdown("**Matched Technical Skills:**")
                    if resume['skill_matches']['matched_technical']:
                        for skill in resume['skill_matches']['matched_technical']:
                            st.markdown(
                                f'<span class="matched-skill">✓ {skill}</span>',
                                unsafe_allow_html=True
                            )
                    else:
                        st.write("None")
                    
                    st.markdown("**Missing Technical Skills:**")
                    if resume['skill_matches']['missing_technical']:
                        for skill in resume['skill_matches']['missing_technical']:
                            st.markdown(
                                f'<span class="missing-skill">✗ {skill}</span>',
                                unsafe_allow_html=True
                            )
                    else:
                        st.write("None")
                
                # Additional Details
                with col3:
                    st.markdown("### Soft Skills")
                    
                    st.markdown("**Matched Soft Skills:**")
                    if resume['skill_matches']['matched_soft']:
                        for skill in resume['skill_matches']['matched_soft']:
                            st.markdown(
                                f'<span class="matched-skill">✓ {skill}</span>',
                                unsafe_allow_html=True
                            )
                    else:
                        st.write("None")
                    
                    st.markdown("**Missing Soft Skills:**")
                    if resume['skill_matches']['missing_soft']:
                        for skill in resume['skill_matches']['missing_soft']:
                            st.markdown(
                                f'<span class="missing-skill">✗ {skill}</span>',
                                unsafe_allow_html=True
                            )
                    else:
                        st.write("None")
        
        st.markdown("---")
        
        # Export Options
        st.subheader("📥 Export Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            report = Utils.generate_report(
                st.session_state.results,
                st.session_state.job_description
            )
            st.download_button(
                label="📄 Download Text Report",
                data=report,
                file_name="screening_report.txt",
                mime="text/plain"
            )
        
        with col2:
            json_data = Utils.export_results_json(
                st.session_state.results,
                st.session_state.job_description
            )
            st.download_button(
                label="📋 Download JSON Data",
                data=json_data,
                file_name="screening_results.json",
                mime="application/json"
            )

# About Page
elif page == "About":
    st.header("ℹ️ About This System")
    
    st.markdown("""
    ## Resume Screening System v1.0
    
    An intelligent, ML-powered system designed to automate and optimize the resume screening process.
    
    ### Technologies Used
    - **Python**: Core programming language
    - **Streamlit**: Interactive web interface
    - **spaCy/NLTK**: Natural Language Processing
    - **Scikit-learn**: Machine Learning and text vectorization
    - **PyPDF2**: PDF document processing
    - **python-docx**: DOCX document processing
    
    ### How It Works
    
    1. **Text Preprocessing**: Cleans and normalizes resume and job description text
    2. **Skill Extraction**: Identifies technical and soft skills from both documents
    3. **Vectorization**: Converts text to numerical features using TF-IDF
    4. **Similarity Matching**: Calculates cosine similarity between job and resume
    5. **Composite Scoring**: Combines text similarity (40%) and skills matching (60%)
    6. **Ranking**: Sorts candidates by overall score
    
    ### Skill Database
    - **50+** technical skills (Python, Java, AWS, Docker, etc.)
    - **10+** soft skills (Communication, Leadership, Teamwork, etc.)
    - Easily extensible with custom skills
    
    ### Scoring Formula
    
    ```
    Total Score = (Text Similarity × 40) + (Skills Match × 60)
    
    Where:
    - Text Similarity: Cosine similarity between job description and resume (0-40 points)
    - Skills Match: Average of technical and soft skill match percentages (0-60 points)
    ```
    
    ### Features
    - ✅ Multi-file upload (PDF, DOCX, TXT)
    - ✅ Real-time screening and ranking
    - ✅ Detailed skill gap analysis
    - ✅ Exportable reports (TXT, JSON)
    - ✅ Interactive UI with expandable details
    - ✅ Production-ready code
    
    ### Limitations & Future Enhancements
    - Current skill extraction is keyword-based (future: ML-based entity extraction)
    - PDF parsing may vary with complex layouts
    - Could add CV parsing with computer vision
    - Could integrate with ATS systems
    
    ### Repository
    GitHub: https://github.com/YourUsername/FUTURE_ML_03
    
    ### Support & Issues
    Found a bug? Have a feature request? Create an issue on GitHub.
    """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("👨‍💼 Designed for HR Professionals and Recruiters")
    
    with col2:
        st.warning("🔬 Built with ML Best Practices")
    
    with col3:
        st.success("📊 Production-Ready Code")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**FUTURE_ML_03** | Resume Screening System")

with col2:
    st.markdown("Made with ❤️ using Streamlit")

with col3:
    st.markdown("Version 1.0 | 2024")
