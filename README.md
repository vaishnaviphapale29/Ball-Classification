# 🏏 Ball Classification using Decision Tree

## 📌 Project Overview

This is my **first Machine Learning project**, developed using Python and Scikit-learn. The project demonstrates how a Decision Tree Classification algorithm can classify a ball as either a **Tennis Ball or a Cricket Ball** based on its weight and surface type.

The dataset values are manually defined in the Python code to understand the basic working of a supervised machine learning classification model.

## 🎯 Objectives

- Understand the fundamentals of Machine Learning.
- Learn how supervised learning works.
- Implement a Decision Tree Classifier using Scikit-learn.
- Train a model using manually defined data.
- Predict the type of ball using input features.
- Evaluate model predictions using an accuracy score.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning Library:** Scikit-learn
- **Algorithm:** Decision Tree Classifier
- **Evaluation Metric:** Accuracy Score

## 📊 Dataset Description

This project uses a small, manually created dataset.

The dataset contains two independent features:

| Feature | Description |
|---|---|
| Weight | Weight of the ball (numeric value) |
| Surface | Surface type of the ball |

### Feature Encoding

- Rough = 1
- Smooth = 0

### Target Class Encoding

- Tennis Ball = 1
- Cricket Ball = 2

The independent variables are stored in `X`, and the target labels are stored in `Y`.

**Note:** The values are manually entered for learning purposes. They are illustrative values and are not intended to represent a verified real-world ball dataset.

## ⚙️ Project Workflow

1. Define the dataset manually.
2. Separate the training and testing data.
3. Create a Decision Tree Classifier.
4. Train the model using `fit()`.
5. Predict the ball class using `predict()`.
6. Compare the predicted labels with the actual test labels.
7. Calculate the accuracy score using `accuracy_score()`.

## 🧠 Machine Learning Algorithm

### Decision Tree Classifier

A Decision Tree is a supervised machine learning algorithm used for classification and regression tasks.

It learns decision rules from the training data and uses those rules to predict the class of new observations.

In this project, the classifier learns patterns from the manually defined ball data and predicts whether the input represents a Tennis Ball or a Cricket Ball.

## ▶️ How to Run the Project

### Step 1: Install Python

Install Python 3 on your computer if it is not already installed.

### Step 2: Install the required library

Open the terminal in VS Code and run:

```bash
pip install scikit-learn
```

### Step 3: Run the Python file

Save the code as `BallClassification.py` and execute:

```bash
python BallClassification.py
```

## 📈 Expected Output

```text
Ball classification case study
Model predicts the object as : [1 2]
Accuracy Score : 100.0 %
```

**Note:** The displayed accuracy is based on only two test samples. It does not establish that the model will achieve 100% accuracy on unseen real-world data.

## 📚 Key Learnings

- Basics of supervised machine learning.
- Difference between independent and dependent variables.
- Training and testing a classification model.
- Using Scikit-learn's Decision Tree Classifier.
- Making predictions with `predict()`.
- Evaluating predictions using an accuracy score.

## 🚀 Future Improvements

- Use a larger, realistic dataset.
- Apply `train_test_split()` for systematic dataset splitting.
- Set `random_state` for reproducible model behavior.
- Evaluate the model using a confusion matrix and classification report.
- Compare Decision Tree performance with other classification algorithms.

## 📝 Conclusion

This project is a beginner-friendly introduction to supervised machine learning. It demonstrates the basic process of preparing data, training a Decision Tree Classifier, predicting classes, and evaluating model performance using Python and Scikit-learn.
