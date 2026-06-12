"""
File handling module for PDF and DOCX support
"""
import os
import tempfile
try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

try:
    from docx import Document
except ImportError:
    Document = None


class FileHandler:
    """Handles file reading for PDF and DOCX formats"""
    
    @staticmethod
    def read_text_file(file_content, filename):
        """
        Read text from uploaded file
        
        Args:
            file_content (bytes): File content
            filename (str): Filename with extension
            
        Returns:
            str: Extracted text
        """
        extension = os.path.splitext(filename)[1].lower()
        
        if extension == '.txt':
            return FileHandler._read_txt(file_content)
        elif extension == '.pdf':
            return FileHandler._read_pdf(file_content)
        elif extension in ['.docx', '.doc']:
            return FileHandler._read_docx(file_content)
        else:
            raise ValueError(f"Unsupported file format: {extension}")
    
    @staticmethod
    def _read_txt(file_content):
        """Read text file"""
        try:
            return file_content.decode('utf-8')
        except UnicodeDecodeError:
            return file_content.decode('latin-1')
    
    @staticmethod
    def _read_pdf(file_content):
        """Read PDF file"""
        if PdfReader is None:
            raise ImportError("PyPDF2 not installed. Install with: pip install PyPDF2")
        
        try:
            # Write to temporary file
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
                tmp.write(file_content)
                tmp_path = tmp.name
            
            # Read PDF
            text = ""
            with open(tmp_path, 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                for page in reader.pages:
                    text += page.extract_text()
            
            # Clean up
            os.unlink(tmp_path)
            
            return text
        except Exception as e:
            raise ValueError(f"Error reading PDF: {str(e)}")
    
    @staticmethod
    def _read_docx(file_content):
        """Read DOCX file"""
        if Document is None:
            raise ImportError("python-docx not installed. Install with: pip install python-docx")
        
        try:
            # Write to temporary file
            with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
                tmp.write(file_content)
                tmp_path = tmp.name
            
            # Read DOCX
            doc = Document(tmp_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            # Clean up
            os.unlink(tmp_path)
            
            return text
        except Exception as e:
            raise ValueError(f"Error reading DOCX: {str(e)}")
    
    @staticmethod
    def validate_file_size(file_size, max_size_mb=10):
        """
        Validate file size
        
        Args:
            file_size (int): File size in bytes
            max_size_mb (int): Maximum allowed size in MB
            
        Returns:
            bool: True if valid
            
        Raises:
            ValueError: If file is too large
        """
        max_size_bytes = max_size_mb * 1024 * 1024
        if file_size > max_size_bytes:
            raise ValueError(f"File size exceeds {max_size_mb}MB limit")
        return True
