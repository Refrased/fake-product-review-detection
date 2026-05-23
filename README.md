# Fake Product Review Detection Using NLP

## Overview

Fake reviews can mislead customers and affect purchasing decisions. This project uses Natural Language Processing (NLP) and Machine Learning techniques to classify product reviews as either Genuine or Fake.

The system accepts a review as input, processes the text using TF-IDF Vectorization, and predicts whether the review is genuine or fake using a Logistic Regression model.

---

## Problem Statement

Online shopping platforms contain large numbers of product reviews. Some reviews are artificially generated or manipulated to influence customer decisions.

The objective of this project is to build a machine learning model that can automatically identify fake reviews and distinguish them from genuine customer feedback.

---

## Objectives

- Detect fake product reviews using NLP.
- Preprocess and analyze review text.
- Convert text data into numerical features.
- Train a machine learning classification model.
- Provide predictions through a simple web interface.

---

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- HTML
- CSS

---

## Dataset

The project uses a synthetic dataset containing:

- 1000 Product Reviews
- 500 Genuine Reviews
- 500 Fake Reviews

Dataset format:

| Review | Label |
|----------|----------|
| Good quality product | 1 |
| Buy now best product ever | 0 |

Where:

- 1 = Genuine Review
- 0 = Fake Review

---

## System Architecture

Input Review

↓

Text Preprocessing

↓

TF-IDF Vectorization

↓

Logistic Regression Model

↓

Prediction Result

↓

Fake / Genuine Review

---

## Machine Learning Workflow

### Step 1: Data Collection

Review data is collected and stored in CSV format.

### Step 2: Text Processing

The review text is cleaned and prepared for analysis.

### Step 3: Feature Extraction

TF-IDF Vectorization converts text into numerical vectors.

### Step 4: Model Training

A Logistic Regression classifier is trained using the processed data.

### Step 5: Prediction

The trained model predicts whether a review is fake or genuine.

---

## Project Structure

```text
fake-product-review-detection/

│
├── app.py
├── train_model.py
├── reviews.csv
├── model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates
    └── index.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fake-product-review-detection.git
```

Move into the project directory:

```bash
cd fake-product-review-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Generate dataset (optional):

```bash
python generate_dataset.py
```

Train the model:

```bash
python train_model.py
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Sample Inputs

### Genuine Review

```text
The product arrived on time and works as expected.
```

Output:

```text
Genuine Review
```

### Fake Review

```text
Best product ever buy now immediately.
```

Output:

```text
Fake Review
```

---

## Features

- Fake Review Detection
- NLP-based Text Analysis
- TF-IDF Feature Extraction
- Logistic Regression Classification
- User-Friendly Web Interface
- Real-Time Predictions

---

## Future Enhancements

- Use real-world datasets from e-commerce platforms.
- Improve accuracy using advanced NLP models.
- Integrate Deep Learning techniques.
- Deploy the application on cloud platforms.
- Add review confidence scores.

---

## Conclusion

This project demonstrates how Natural Language Processing and Machine Learning can be used to identify fake product reviews. The system successfully processes review text, extracts meaningful features, and classifies reviews as fake or genuine through an easy-to-use web interface.

---

## Author

College Mini Project

Fake Product Review Detection Using NLP and Machine Learning
