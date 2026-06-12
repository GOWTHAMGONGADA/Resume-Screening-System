# Resume Screening System 📄

**Track:** Machine Learning (ML)  
**Task:** FUTURE_ML_03  
**Status:** ✅ Production Ready  

---

## 📋 Overview

A sophisticated **AI-powered resume screening system** that automatically analyzes, scores, and ranks resumes based on job descriptions. This system uses Natural Language Processing (NLP) and Machine Learning to streamline the hiring process.

### Key Features
✅ **Multi-format support:** PDF, DOCX, TXT  
✅ **Skill extraction:** 50+ technical and soft skills  
✅ **Smart scoring:** Text similarity + skills matching  
✅ **Intelligent ranking:** Automatic candidate prioritization  
✅ **Skill gap analysis:** Identifies missing and required skills  
✅ **Web interface:** Interactive Streamlit dashboard  
✅ **Export results:** TXT, JSON, CSV formats  

---

## 🎯 How It Works

### Scoring Formula
```
Total Score = (Text Similarity × 40%) + (Skills Match × 60%)

Where:
- Text Similarity: Cosine similarity between job & resume (0-40 points)
- Skills Match: Average of technical & soft skill percentages (0-60 points)
```

### Pipeline
1. **Text Preprocessing** → Cleaning, tokenization, lemmatization
2. **Skill Extraction** → Identifying technical & soft skills
3. **Feature Vectorization** → TF-IDF text representation
4. **Similarity Matching** → Cosine similarity calculation
5. **Composite Scoring** → Combined scoring logic
6. **Ranking & Analysis** → Sorting and gap identification

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda
- 2GB+ free disk space

### Installation

```bash
# Clone repository
git clone https://github.com/YourUsername/FUTURE_ML_03.git
cd FUTURE_ML_03

# Create virtual environment (recommended)
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### Running the Application

```bash
# Start Streamlit app (opens in browser)
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Using the Jupyter Notebook

```bash
# Start Jupyter
jupyter notebook

# Open: notebooks/resume_screening.ipynb
```

---

## 📁 Project Structure

```
FUTURE_ML_03/
├── app.py                          # Streamlit web application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── src/
│   ├── __init__.py
│   ├── text_processor.py          # Text cleaning & preprocessing
│   ├── skill_extractor.py         # Skill extraction logic
│   ├── resume_scorer.py           # Scoring & ranking
│   ├── file_handler.py            # PDF/DOCX file processing
│   └── utils.py                   # Utility functions
│
├── notebooks/
│   └── resume_screening.ipynb     # Complete ML pipeline walkthrough
│
├── data/
│   ├── sample_resumes/            # Sample resume files
│   │   ├── resume_1.txt
│   │   ├── resume_2.txt
│   │   ├── resume_3.txt
│   │   └── resume_4.txt
│   │
│   └── sample_jobs/               # Sample job descriptions
│       └── senior_engineer.txt
│
├── models/                        # Saved ML models & artifacts
│   ├── vectorizer.pkl
│   └── trained_model.pkl
│
└── outputs/                       # Generated reports
    ├── screening_report.txt
    ├── screening_results.csv
    └── screening_results.json
```

---

## 🎮 Usage Guide

### Web Interface (Streamlit)

1. **Upload Job Description**
   - Click "Upload Job Description" 
   - Select PDF, DOCX, or TXT file
   - Preview appears automatically

2. **Upload Resumes**
   - Click "Upload Resumes" (multi-select)
   - Add 1-100+ resume files
   - All formats supported

3. **Screen Resumes**
   - Click "🔍 Screen Resumes" button
   - Processing starts automatically
   - Results display in real-time

4. **Review Results**
   - See ranked candidates
   - Expand each for details
   - View skill gaps
   - Export reports

### Jupyter Notebook

The notebook (`notebooks/resume_screening.ipynb`) includes:
- Step-by-step NLP pipeline
- Data exploration & visualization
- Skill extraction examples
- Scoring demonstrations
- Report generation

Run cells sequentially to understand the ML workflow.

---

## 📊 Features Explained

### 1. Text Preprocessing
```python
✓ Lowercase conversion
✓ URL & email removal
✓ Special character removal
✓ Whitespace normalization
✓ Tokenization
✓ Stopword removal
✓ Lemmatization
```

### 2. Skill Extraction
Recognizes 50+ skills across categories:
- **Programming:** Python, Java, JavaScript, C++, etc.
- **Frontend:** React, Angular, Vue, HTML5, CSS3
- **Backend:** Node.js, Django, Flask, FastAPI
- **Databases:** SQL, PostgreSQL, MongoDB, Redis
- **Cloud:** AWS, Azure, GCP, Docker, Kubernetes
- **ML/Data:** TensorFlow, PyTorch, Spark, Hadoop
- **Soft Skills:** Communication, Leadership, Teamwork

### 3. Similarity Scoring
- **TF-IDF Vectorization:** Converts text to numerical features
- **Cosine Similarity:** Measures semantic similarity (0-1)
- **Weighted Scoring:** Combines multiple dimensions

### 4. Skill Matching
```
Technical Match % = Matched Skills / Total Required Skills × 100
Soft Match % = Matched Soft Skills / Total Soft Skills × 100
Overall Skill Score = (Tech % + Soft %) / 2 × 60 points
```

---

## 🧪 Testing

### Run Unit Tests
```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
pytest tests/

# Run specific test
pytest tests/test_text_processor.py -v

# With coverage
pytest --cov=src tests/
```

### Manual Testing
```python
from src.text_processor import TextProcessor
from src.skill_extractor import SkillExtractor
from src.resume_scorer import ResumeScorer

# Initialize components
processor = TextProcessor()
extractor = SkillExtractor()
scorer = ResumeScorer()

# Test text processing
cleaned = processor.clean_text("Your text here")
print(cleaned)

# Test skill extraction
skills = extractor.extract_skills("Python Java AWS Docker")
print(skills)

# Test scoring
similarity = scorer.calculate_similarity("Job desc", "Resume text")
print(f"Similarity: {similarity}")
```

---

## 📈 Performance & Metrics

### Scoring Metrics
- **Text Similarity Score:** 0-40 points
- **Skills Match Score:** 0-60 points
- **Overall Score:** 0-100 points

### Candidate Classification
```
🟢 EXCELLENT FIT:  70-100 points (Strong match)
🟡 GOOD FIT:       50-69 points  (Suitable match)
🔴 WEAK FIT:       0-49 points   (Poor match)
```

### Processing Speed
- Single resume: ~100-500ms
- 100 resumes: ~10-50 seconds
- Scales linearly with dataset size

---

## 🔧 Configuration

### Adjusting Weights
Modify scoring weights in `resume_scorer.py`:
```python
text_score = text_similarity * 40    # Adjust: 40 = 40% weight
skills_score = skills_match * 60      # Adjust: 60 = 60% weight
```

### Adding Custom Skills
Edit `skill_extractor.py`:
```python
self.technical_skills = {
    'my_skill': ['variant1', 'variant2'],
    # Add more...
}
```

### Filter Candidates
Modify threshold in app.py or use CSV export for custom filtering.

---

## 📦 Dependencies

### Core Libraries
- **numpy:** Numerical computing
- **pandas:** Data manipulation
- **scikit-learn:** ML algorithms & text vectorization
- **nltk:** NLP toolkit (tokenization, lemmatization)

### File Processing
- **PyPDF2:** PDF text extraction
- **python-docx:** DOCX file reading

### Web Framework
- **streamlit:** Interactive web interface

### Visualization
- **matplotlib:** Static plots
- **seaborn:** Statistical visualizations

---

## 🐛 Troubleshooting

### Issue: PDF files not reading
**Solution:** Ensure `PyPDF2` is installed
```bash
pip install PyPDF2 --upgrade
```

### Issue: NLTK data missing
**Solution:** Download required datasets
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Issue: Streamlit not starting
**Solution:** Check port availability
```bash
streamlit run app.py --server.port 8501
```

### Issue: Memory error with large files
**Solution:** Process files in batches or increase available RAM

---

## 🚀 Deployment

### Local Deployment
```bash
streamlit run app.py
# Access at: http://localhost:8501
```

### Docker Deployment
```bash
# Build image
docker build -t resume-screener .

# Run container
docker run -p 8501:8501 resume-screener
```

### Cloud Deployment (Streamlit Cloud)
```bash
# Push to GitHub
git push origin main

# Deploy via: https://streamlit.io/cloud
```

---

## 📊 Sample Results

### Example Run
```
Job: Senior Software Engineer
Resumes: 4 candidates

RANKING:
1. John Anderson     Score: 85.3/100  (Excellent match)
2. Sarah Mitchell    Score: 62.1/100  (Good match)
3. Michael Chen      Score: 55.8/100  (Good match)
4. Emily Rodriguez   Score: 41.2/100  (Weak match)

Top Candidate Analysis:
- Matched: Python, Java, React, AWS, Docker
- Missing: TensorFlow, Spark, Kubernetes
- Skill Gap: 3/12 (75% match)
```

---

## 📚 Resources

### Documentation
- [spaCy Documentation](https://spacy.io/)
- [NLTK Book](https://www.nltk.org/book/)
- [Scikit-learn Guide](https://scikit-learn.org/stable/)
- [Streamlit Docs](https://docs.streamlit.io/)

### Recommended Datasets
- [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)
- [Job Descriptions Dataset](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset)
- [Job Postings Dataset](https://www.kaggle.com/datasets/PromptCloudHQ/us-jobs-on-monstercom)

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💼 Author

**Your Name**  
Machine Learning & NLP Enthusiast  
GitHub: [@YourUsername](https://github.com/YourUsername)  
Email: your.email@example.com

---

## 🎓 Learning Outcomes

By building this project, you'll learn:
- ✅ NLP fundamentals (preprocessing, tokenization, lemmatization)
- ✅ Feature extraction (TF-IDF, embeddings, vectorization)
- ✅ Text similarity metrics (cosine similarity, semantic matching)
- ✅ Scoring & ranking algorithms
- ✅ File handling (PDF, DOCX, TXT parsing)
- ✅ ML pipeline implementation
- ✅ Web UI development (Streamlit)
- ✅ Production-ready code practices
- ✅ Data export & reporting
- ✅ Real-world HR-tech application development

---

## 🎯 Future Enhancements

- [ ] Deep learning embeddings (BERT, transformers)
- [ ] Computer vision for CV parsing
- [ ] Database integration for candidate storage
- [ ] Email notification system
- [ ] Advanced filtering & search
- [ ] Performance analytics dashboard
- [ ] Multi-language support
- [ ] Resume formatting templates
- [ ] API for third-party integration
- [ ] ML model fine-tuning on labeled data

---

## 📞 Support

For issues, questions, or suggestions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an [Issue](https://github.com/YourUsername/FUTURE_ML_03/issues)
3. Start a [Discussion](https://github.com/YourUsername/FUTURE_ML_03/discussions)

---

## ✨ Acknowledgments

- NLTK & spaCy teams for NLP libraries
- Scikit-learn for ML tools
- Streamlit for web framework
- Kaggle for sample datasets

---

**Made with ❤️ for HR Professionals, Recruiters & ML Enthusiasts**

⭐ **If this project helps you, please star it!** ⭐
