from rapidocr_onnxruntime import RapidOCR

# Create OCR engine
engine = RapidOCR()

# OCR on image
result, _ = engine(r"C:\Users\princ\Downloads\ChatGPT Image May 27, 2026, 02_57_23 PM (2).png")

# Print text
for line in result:
    print(line[1])