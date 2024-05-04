from flask import Flask, request, render_template, jsonify
import pdfreader
from pdfreader import SimplePDFViewer
import os

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = SimplePDFViewer(file)
        for page_num in range(reader.getPageNum):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

# Route to handle the file upload and text extraction
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        
        pdf_file = request.files["file"]
        
        if pdf_file.filename == "":
            return "No selected file"
        
        if pdf_file:
            # Save uploaded file
            file_path = os.path.join("uploads", pdf_file.filename)
            pdf_file.save(file_path)
            
            # Extract text from PDF
            extracted_text = extract_text_from_pdf(file_path)
            return jsonify({"text": extracted_text})  # Return JSON response
    
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
