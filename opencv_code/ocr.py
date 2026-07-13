import easyocr
import cv2
import numpy as np

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def ocr_image(image_path):
    """Extract text from image"""
    results = reader.readtext(image_path)
    
    for detection in results:
        bbox, text, confidence = detection
        print(f"Text: {text}")
        print(f"Confidence: {confidence}")
        print("-" * 30)
    
    return results

def visualize_ocr(image_path, output_path='output.jpg'):
    """Draw bounding boxes on image"""
    image = cv2.imread(image_path)
    results = reader.readtext(image_path)
    
    for detection in results:
        bbox = np.array(detection[0], dtype=int)
        text = detection[1]
        confidence = detection[2]
        
        cv2.polylines(image, [bbox], True, (0, 255, 0), 2)
        cv2.putText(image, f"{text} ({confidence:.2f})", 
                   tuple(bbox[0]), cv2.FONT_HERSHEY_SIMPLEX, 
                   0.5, (0, 0, 255), 2)
    
    cv2.imwrite(output_path, image)
    print(f"Saved to {output_path}")

def extract_all_text(image_path):
    """Extract and return all text as a single string"""
    results = reader.readtext(image_path)
    full_text = "\n".join([detection[1] for detection in results])
    return full_text

if __name__ == '__main__':
    image_path = 'img.jpg'
    
    # Extract and print text
    ocr_image(image_path)
    
    # Uncomment to visualize with bounding boxes:
    # visualize_ocr(image_path, 'output.jpg')
    
    # Uncomment to get all text as string:
    # text = extract_all_text(image_path)
    # print("\n=== All Text ===\n", text)