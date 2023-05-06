from flask import Blueprint, make_response, request
import pytesseract
from PIL import Image
from app.controllers.translator.braille import decode
from PyPDF2 import PdfReader
import docx2txt

translator_blueprint = Blueprint("translator_blueprint", __name__, url_prefix="/api/translate")


@translator_blueprint.route("", methods=["POST"])
def translate():

    try:
        file = request.files.to_dict()

        if file.keys().__contains__("image"):
            image = request.files["image"]
            image_to_text = pytesseract.image_to_string(
                Image.open(image),
                lang="por+eng",
                output_type=pytesseract.Output.STRING,
                timeout=5
            )

            if len(image_to_text) < 1:
                raise Exception("text must not be empty")

            return make_response({
                "status": 200,
                "message": "text has been translated successfully",
                "data": {
                    "raw_text": image_to_text,
                    "braille": decode(image_to_text),
                },
            }), 200
        
        elif file.keys().__contains__("pdf"):
            reader = PdfReader(request.files["pdf"])
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            if len(text) < 1:
                raise Exception("text must not be empty")

            return make_response({
                "status": 200,
                "message": "PDF has been translated successfully",
                "data": {
                    "raw_text": text,
                    "braille": decode(text)
                },
            }), 200
        
        elif file.keys().__contains__("docx"):
            text = docx2txt.process(request.files["docx"])
            if len(text) < 1:
                raise Exception("text must not be empty")
            return make_response({
                "status": 200,
                "message": "DOCX has been translated successfully",
                "data": {
                    "raw_text": text,
                    "braille": decode(text)
                },
            }), 200
        
        elif file.keys().__contains__("txt"):
            text = str(request.files["txt"].read(), 'utf-8')
            if len(text) < 1:
                raise Exception("text must not be empty")
            return make_response({
                "status": 200,
                "message": "TXT file has been translated successfully",
                "data": {
                    "raw_text": text,
                    "braille": decode(text)
                },
            }), 200
        
        else:
            raise Exception("there is no file in body")

    except Exception as error:
        return make_response({
        "status": 400,
        "message": error.args[0],
        "data": None
    }), 200