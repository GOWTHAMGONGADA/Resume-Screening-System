# 🚀 Quick Start Guide

Resume Screening System - Get Started in 5 Minutes!

---

## Step 1: Installation (2 min)



# Create virtual environment (recommended)
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (one-time setup)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

---

## Step 2: Start the App (1 min)

```bash
# Run Streamlit application
streamlit run app.py
```

✅ App opens automatically at: `http://localhost:8501`

---

## Step 3: Test with Sample Data (2 min)

1. **Navigate to "Upload & Screen"** tab
2. **Upload Job Description:**
   - Use: `data/sample_jobs/senior_engineer.txt`
3. **Upload Resumes:**
   - Select: `data/sample_resumes/resume_1.txt` through `resume_4.txt`
4. **Click "🔍 Screen Resumes"**
5. **Go to "Results"** tab to see rankings

---

## Sample Results

```
RANKING:
1. 🥇 John Anderson    - 85.3/100 (Excellent Match)
2. 🥈 Sarah Mitchell   - 62.1/100 (Good Match)
3. 🥉 Michael Chen     - 55.8/100 (Good Match)
4.    Emily Rodriguez  - 41.2/100 (Weak Match)

✅ Matched Skills: Python, Java, React, AWS, Docker
❌ Missing Skills: TensorFlow, Kubernetes, Spark
```

---

## Explore the Code

### View ML Pipeline
```bash
# Open Jupyter notebook for detailed exploration
jupyter notebook notebooks/resume_screening.ipynb
```

### Run Tests
```bash
# Install pytest (optional)
pip install pytest

# Run unit tests
pytest tests/ -v
```

---

## Use Your Own Files

### Supported Formats
✅ PDF (.pdf)  
✅ Word (.docx, .doc)  
✅ Text (.txt)

### Upload Custom Files
1. In Streamlit app: "Upload & Screen" tab
2. Click file uploader
3. Select your files
4. Click "🔍 Screen Resumes"

---

## Export Results

After screening, in Results tab:

📄 **Download Text Report** → Full analysis in .txt  
📋 **Download JSON Data** → Structured results in .json  
📊 **View CSV** → Import to Excel/Sheets  

---

## Project Structure

```
SCREENING_SYSTEM/
├── app.py                    # Web app (run this!)
├── requirements.txt          # Dependencies
├── README.md                 # Full documentation
│
├── src/                      # Core modules
│   ├── text_processor.py    # Text cleaning
│   ├── skill_extractor.py   # Skill detection
│   ├── resume_scorer.py     # Ranking logic
│   ├── file_handler.py      # PDF/DOCX parsing
│   └── utils.py             # Utilities
│
├── data/                     # Sample data
│   ├── sample_jobs/
│   └── sample_resumes/
│
├── notebooks/
│   └── resume_screening.ipynb  # ML exploration
│
└── outputs/                  # Generated reports
```

---

## Troubleshooting

### Streamlit won't start?
```bash
streamlit run app.py --logger.level=debug
```

### PDF not reading?
```bash
pip install PyPDF2 --upgrade
```

### Missing NLTK data?
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Port 8501 already in use?
```bash
streamlit run app.py --server.port 8502
```

---

## Key Features ✨

✅ **Multi-format upload** (PDF, DOCX, TXT)  
✅ **Real-time screening** (instant results)  
✅ **Skill extraction** (50+ skills recognized)  
✅ **Ranking algorithm** (smart scoring)  
✅ **Skill gap analysis** (shows missing skills)  
✅ **Export reports** (TXT, JSON, CSV)  
✅ **Production-ready** (professional code)  

---

## Example Workflow

```
1. Open app → http://localhost:8501

2. Upload:
   - Job description (what you're looking for)
   - Resumes (candidate documents)

3. Screen:
   - Click "🔍 Screen Resumes"
   - Wait for analysis

4. Review:
   - See ranked candidates
   - View skill gaps
   - Export results

5. Export:
   - Download reports
   - Share with team
   - Make hiring decisions
```

---

## Next Steps

1. ✅ **Get it running** (follow Quick Start above)
2. 📚 **Read the docs** (README.md for details)
3. 🔬 **Explore the code** (notebooks/resume_screening.ipynb)
4. 🧪 **Try your data** (upload your own resumes)
5. 🚀 **Deploy it** (push to GitHub, deploy to cloud)

---

## Need Help?

📖 Read full documentation: [README.md](README.md)  
💻 View Jupyter notebook: [resume_screening.ipynb](notebooks/resume_screening.ipynb)  
🧪 Run tests: `pytest tests/ -v`  
📋 Check code comments: [src/](src/)  

---

## Performance Tips

- **Single resume:** ~100-500ms
- **100 resumes:** ~10-50 seconds
- **Tip:** Process in batches for very large datasets

---

**That's it! You're ready to screen resumes with ML! 🎉**

Questions? Check the full [README.md](README.md) or review [notebooks/resume_screening.ipynb](notebooks/resume_screening.ipynb)
