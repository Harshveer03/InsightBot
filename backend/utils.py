import pdfplumber
from PIL import Image
import pytesseract
import torch
from transformers import BlipProcessor, BlipForQuestionAnswering

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

def extract_text_from_pdf(path):
    try:
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        return None

def extract_text_from_image(path):
    try:
        image = Image.open(path)
        return pytesseract.image_to_string(image)
    except Exception as e:
        return None

def generate_answer_blip(image_path, question):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, question, return_tensors="pt")
    outputs = model.generate(**inputs)
    return processor.decode(outputs[0], skip_special_tokens=True)
