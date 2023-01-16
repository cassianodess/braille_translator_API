from flask import Blueprint, make_response, request
import pytesseract
from PIL import Image

translator_blueprint = Blueprint("translator_blueprint", __name__, url_prefix="/api/translate")


@translator_blueprint.route("", methods=["POST"])
def translate():

    image = request.files["image"]

    image_to_text = pytesseract.image_to_string(
        Image.open(image),
         lang="por+eng",
         output_type=pytesseract.Output.STRING
    )

    return make_response({
        "message": "text has been translated successfully",
        "data": {
            "raw_text": image_to_text,
            "braille": "",
        },
    }), 200