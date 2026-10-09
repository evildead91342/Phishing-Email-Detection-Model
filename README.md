  

# 📬 Phishing Email Detection using Machine Learning

A machine learning–based system designed to automatically detect phishing emails by analyzing their textual content. This project applies **Natural Language Processing (NLP)** and **classification algorithms** to distinguish between phishing and legitimate emails with high accuracy.

---

## 🔍 Project Overview

Phishing emails are one of the most common cybersecurity threats, often tricking users into revealing sensitive information. This project addresses the problem by building an automated detection system that:

-   Preprocesses raw email text
    
-   Converts emails into numerical representations using **Doc2Vec**
    
-   Trains and evaluates multiple machine learning classifiers
    
-   Predicts whether an email is **phishing** or **legitimate**
    

The project includes scripts, notebooks, datasets, and saved models to support training, evaluation, and inference.

---

## ✨ Features

-   🧹 **Text Preprocessing**  
    Cleans email content by removing noise, stopwords, punctuation, and unnecessary tokens.
    
-   📊 **Feature Extraction**  
    Uses **Doc2Vec** to transform email text into meaningful document embeddings.
    
-   🤖 **Machine Learning Models**  
    Trains and evaluates multiple classifiers to identify phishing patterns.
    
-   📈 **Model Evaluation**  
    Computes performance metrics such as:
    
    -   Accuracy
        
    -   Precision
        
    -   Recall
        
    -   F1-Score
        
    -   Confusion Matrix
        
    -   ROC Curve
        
-   💾 **Saved Models**  
    Pretrained models are included for faster testing and deployment.
    

---

## 🗂️ Project Structure

```
Phishing-Email-Detection/│├── data/                  # Email datasets (phishing & legitimate)├── models/                # Saved trained models├── notebooks/             # Jupyter notebooks for experiments├── src/                   # Source code for preprocessing and modeling│   ├── preprocessing.py│   ├── train_model.py│   ├── evaluate_model.py│├── requirements.txt       # Project dependencies├── README.md              # Project documentation└── main.py                # Entry point for training/testing
```

The list below will help understanding the role of each coding file.

```
Dataset: the folder contains the dataset for the project.    Enron dataset    Phishing datasetNotebook: Jupyter notebooks of this program for every dataset.dumped_models: In this folder there are saved Doc2Vec model and ten classifcation models.balanced_dataset.py, imbalanced_dataset: the entire program code for every type of dataset in a python file.load_data.py: load the data from Dataset.preprocess.py: functions for cleaning text before training the model.train.py: the stage of training model with Doc2vec algorithm and other machine learning classification algorithms.evaluate.py: evaluate the model with different methods, such as: accuracy score, confusion matrix, ROC curve, Area Under the Curve, Precision and Recall, F1 score.data_X_test.npy, data_y_test.npy: save numpy data X_test and y_test for evaluating after word embeddings by Doc2Vec algorithm.unit-test.py: unit test for program.startup.sh: bash script for automatic installation program.requirements.txt: the required packages of program.
```

---

## 🛠️ Technologies Used

-   **Python**
    
-   **Natural Language Processing (NLP)**
    
-   **Doc2Vec**
    
-   **scikit-learn**
    
-   **NumPy**
    
-   **pandas**
    
-   **Matplotlib / Seaborn** (for visualization)
    

---

## 🚀 Installation & Setup

1.  **Clone the repository**
    
    ```bash
    git clone https://github.com/mohammedtouheedpatelgithubcom/Phishing-Email-Detection.gitcd Phishing-Email-Detection
    ```
    
2.  **Create a virtual environment (optional but recommended)**
    
    ```bash
    python -m venv venvsource venv/bin/activate   # On Windows: venvScriptsactivate
    ```
    
3.  **Install dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```
    

---

## ▶️ Usage

-   **Train the model**
    
    ```bash
    python main.py
    ```
    
-   **Evaluate performance**  
    Evaluation metrics and plots will be generated after training.
    
-   **Predict new emails**  
    Use the trained model to classify new email text as phishing or legitimate.
    

---

## 📊 Results

The trained models demonstrate strong performance in detecting phishing emails, showing high accuracy and balanced precision-recall scores. Detailed results and visualizations can be found in the notebooks and evaluation scripts.

---

## 📌 Future Improvements

-   Integrate deep learning models (LSTM, BERT)
    
-   Deploy as a web application or browser extension
    
-   Real-time email filtering support
    
-   Larger and more diverse datasets
    

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork this repository, improve the code, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Mohammed Touheed Patel**  
GitHub: [mohammedtouheedpatelgithubcom](https://github.com/mohammedtouheedpatelgithubcom)