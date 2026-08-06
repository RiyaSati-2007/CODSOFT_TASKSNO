# Image Captioning AI - CODSOFT Task 3

from PIL import Image
import matplotlib.pyplot as plt
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load pre-trained model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Take image path from user
image_path = input("Enter image path: ")

# Open image
image = Image.open(image_path)

# Generate caption
inputs = processor(images=image, return_tensors="pt")

output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)

# Display image
plt.imshow(image)
plt.axis("off")
plt.title(caption)
print(caption)
plt.show()

print("Generated Caption:")
print(caption)