from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from utils import extract_text_from_pdf, extract_text_from_image, generate_answer_blip

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploaded_files')
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    question = request.form.get("question", "")

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        ext = filename.rsplit('.', 1)[1].lower()

        try:
            if ext == 'pdf':
                extracted_text = extract_text_from_pdf(filepath)
                if not extracted_text:
                    return jsonify({"error": "PDF reading failed"}), 500
                return jsonify({"answer": f"✅ Answer:\n\nQ: {question}\n\n✅ Answer:\n{extracted_text.strip()[:700]}"})

            elif ext in ['png', 'jpg', 'jpeg']:
                answer = generate_answer_blip(filepath, question)
                return jsonify({"answer": f"✅ Answer:\n\nQ: {question}\n\n✅ Answer:\n{answer}"})
            else:
                return jsonify({"error": "Unsupported file type"}), 400

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file type"}), 400

if __name__ == "__main__":
    app.run(debug=True)
