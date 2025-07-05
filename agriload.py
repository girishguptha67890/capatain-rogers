from PIL import Image
import pytesseract
import cv2

# Load the image
image_path = "weather_data.jpg"
image = cv2.imread(image_path)

# Convert to grayscale (improves OCR accuracy)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# OCR
text = pytesseract.image_to_string(gray)

# Output the extracted text
print("Extracted Data:")
print(text)

