# YOLOv8-powered Computer Vision Pipelines 🚀

This repository contains multiple advanced YOLOv8 object detection pipelines, trained weights, datasets, and execution scripts for various tasks, primarily focusing on **Safety Compliance (PPE)** and **Financial Document OCR (Invoice/Receipt Parsing)**.

---

## 📂 Repository Structure

Below is the reorganized, production-ready directory layout:

```text
├── invoice_receipt_ocr/       # YOLOv8-based Invoice & Receipt Information Extraction
│   ├── best.pt                # Trained weights (detects fields: total, store, date, etc.)
│   ├── ppprotected.pt         # Safety model weights copy
│   └── dataset/               # Structured training/testing datasets for OCR
│
├── ppe_safety_detection/      # Construction Safety Monitoring Application
│   ├── best.pt                # PPE Detection weights (helmet, vest, person, etc.)
│   ├── app.py                 # Main video inference pipeline (annotates video + saves output)
│   ├── webcam.py              # Real-time webcam inference script
│   └── *.mp4                  # Sample test footage (cons.mp4, mm.mp4, etc.)
│
├── road_helmet_detection/     # Road Safety Compliance Detection (Roboflow source)
│   ├── yolov8n.pt             # Pre-trained base weights
│   ├── data.yaml              # Roboflow dataset config (bicyclist, driver, helmet, etc.)
│   ├── train/ & valid/        # Image datasets and annotations
│   └── runs/                  # Execution checkpoints and logs
│
├── experiments/               # Research & Development Playgrounds
│   ├── basic_yolo_tests/      # Basic notebooks and placeholder assets (cat, lion, etc.)
│   └── opencv_utils/          # General computer vision utilities (OCR, shape detection, face/eye detection)
│
└── datasets/                  # Project datasets consolidation
    ├── raw/                   # Raw split documentation
    ├── train/                 # Consolidated train placeholders
    └── valid/                 # Consolidated valid placeholders
```

---

## 🧠 Model Reference & Classes

Here is the exact breakdown of the trained models (`best.pt`) contained in this repository:

### 1. Invoice & Receipt OCR/Information Extraction
* **Location:** `invoice_receipt_ocr/best.pt`
* **Task:** Object Detection (`detect`)
* **Classes (9 classes):**
  * `0`: `invoice_total` — Total amount payable.
  * `1`: `item_name` — Name of individual item/line-item.
  * `2`: `item_price` — Unit or total price of an item.
  * `3`: `date` — Transaction date.
  * `4`: `store_name` — Name of the merchant/store.
  * `5`: `address` — Store or billing address.
  * `6`: `tax` — Tax amount (VAT/GST/etc.).
  * `7`: `subtotal` — Net amount before taxes.
  * `8`: `currency_symbol` — Currency indicators ($, €, £, etc.).

### 2. PPE (Personal Protective Equipment) & Construction Safety
* **Location:** `ppe_safety_detection/best.pt` (Also at `invoice_receipt_ocr/ppprotected.pt`)
* **Task:** Object Detection (`detect`)
* **Classes (5 classes):**
  * `0`: `helmet` — Person wearing a safety helmet/hard hat.
  * `1`: `no-helmet` — Person without a safety helmet.
  * `2`: `no-vest` — Person without a high-visibility safety vest.
  * `3`: `person` — Detected individual.
  * `4`: `vest` — Person wearing a high-visibility safety vest.

### 3. Road Safety & Helmet Detection
* **Location:** `road_helmet_detection/runs/detect/train/weights/best.pt`
* **Task:** Object Detection (`detect`)
* **Classes (4 classes):**
  * `0`: `bicyclist` — Bicycle riders.
  * `1`: `driver` — Motorcycle/vehicle drivers.
  * `2`: `helmet` — Helmet worn.
  * `3`: `no-helmet` — Helmet absent.

---

## 🛠️ Getting Started & Installation

### Prerequisites
Make sure you have Python 3.8+ installed (tested with Python 3.13.5). Install the core dependencies:

```bash
pip install ultralytics opencv-python torch torchvision
```

---

## 🚀 How to Run the Applications

### 🎥 Running Construction PPE Safety Detection on Video
To process a video file using the PPE safety detection model:
1. Navigate to the safety app directory:
   ```bash
   cd ppe_safety_detection
   ```
2. Run the inference script:
   ```bash
   python app.py
   ```
This will read the default video (`42923-434300950_medium.mp4`), run the detection model to identify persons, helmets, and vests, output a live window, and save the annotated video as `output.mp4`.

### 📹 Running PPE Safety Detection on Webcam
To run the live webcam detection monitor:
1. Navigate to the safety app directory:
   ```bash
   cd ppe_safety_detection
   ```
2. Run the webcam script:
   ```bash
   python webcam.py
   ```
Press `q` to exit the video display.

### 📝 Programmatic Inference Example (Python)
You can load and use any of these models directly in your custom Python scripts:

```python
from ultralytics import YOLO

# 1. Load the target model
model = YOLO("invoice_receipt_ocr/best.pt") # For OCR
# or: model = YOLO("ppe_safety_detection/best.pt") # For PPE Safety

# 2. Run inference on an image
results = model("path/to/invoice.jpg")

# 3. View detection results
for result in results:
    boxes = result.boxes
    for box in boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        confidence = float(box.conf[0])
        coordinates = box.xyxy[0].tolist()
        print(f"Detected {class_name} with {confidence:.2f} conf at {coordinates}")
```

---

## 🛡️ License & Attributions
* Road safety datasets and models sourced via [Roboflow Universe](https://universe.roboflow.com/).
* Other code and custom training weights are created for research and demonstration purposes.
