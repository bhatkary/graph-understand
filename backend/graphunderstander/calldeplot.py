from transformers import Pix2StructProcessor, Pix2StructForConditionalGeneration
import requests
from PIL import Image


def call_deplot(image):
    processor = Pix2StructProcessor.from_pretrained("google/deplot")
    model = Pix2StructForConditionalGeneration.from_pretrained("google/deplot")

    inputs = processor(
        images=image,
        text="Generate underlying data table of the figure below:",
        return_tensors="pt",
    )
    predictions = model.generate(**inputs, max_new_tokens=512)
    print(processor.decode(predictions[0], skip_special_tokens=True))
    return processor.decode(predictions[0], skip_special_tokens=True)
