# Tuberculosis Detection from Chest X-Ray Images Using Machine Learning

## Project Overview

This project focuses on detecting Tuberculosis from chest X-ray images using machine learning and deep learning-based feature extraction. Tuberculosis mainly affects the lungs, and early detection can help support faster diagnosis and treatment.

This project was completed as part of the Machine Learning Design course. The main objective was to evaluate whether open-source machine learning tools can classify chest X-ray images as either **Normal** or **Tuberculosis-positive**.

---

## Team Members

- Nitin Reddy Mereddy
- Riswana Palliyaliyil

---

## Dataset

The dataset used in this project is the **Tuberculosis TB Chest X-Ray Dataset** from Kaggle.

**Dataset Link:**  
https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset

The dataset contains:

- **3,500 Normal chest X-ray images**
- **700 Tuberculosis-positive chest X-ray images**
- **Total: 4,200 images**

This is a **binary image classification problem**, where the model predicts whether a chest X-ray image belongs to the **Normal** class or the **Tuberculosis-positive** class.

The dataset is not included in this repository due to size and licensing considerations. It can be downloaded directly from Kaggle.

---

## Tools and Technologies

- Python
- df-analyze
- df-embed
- X-Vision Helper
- ResNet-50
- Parameter Efficient Fine-Tuning
- Logistic Regression
- Stochastic Gradient Descent
- LightGBM
- Random Forest
- K-Nearest Neighbours

---

## Useful Links

- **df-analyze:** https://github.com/stfxecutables/df-analyze
- **X-Vision Helper:** https://github.com/moayadeldin/X-vision-helper
- **Dataset:** https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset

---

## Methodology

The project followed these main steps:

1. Downloaded and organized the chest X-ray dataset.
2. Mapped image labels into **Normal** and **Tuberculosis** classes.
3. Generated a parquet file for structured data processing.
4. Extracted image embeddings using **df-embed** and **ResNet-50-based methods**.
5. Ran multiple machine learning models using **df-analyze**.
6. Compared models using the following evaluation metrics:
   - Accuracy
   - AUROC
   - Balanced Accuracy
   - F1 Score
   - Sensitivity
   - Specificity
7. Performed downsampling experiments using:
   - 50% of the dataset
   - 75% of the dataset
8. Fine-tuned ResNet-50 using different train-validation-test splits.
9. Applied Parameter Efficient Fine-Tuning and compared the final results.

---

## Dataset Sample

The dataset contains chest X-ray images from both **Normal** and **Tuberculosis-positive** classes.

![Dataset Sample](<screenshots/Dataset sample.png>)

---

## Experiments

### 1. Full Dataset Experiment

The full dataset experiment used all **4,200 chest X-ray images**. Machine learning models were trained and evaluated using extracted image embeddings.

The main models compared in this experiment included:

- Logistic Regression
- Stochastic Gradient Descent
- LightGBM
- Random Forest
- K-Nearest Neighbours

---

### 2. Downsampling Experiments

To understand the impact of dataset size on model performance, two downsampling experiments were performed:

- **50% downsampled dataset**
- **75% downsampled dataset**

The results showed that model performance slightly decreased as the dataset size was reduced, but **Logistic Regression** and **SGD** remained strong performers.

---

### 3. Fine-Tuning Experiments

ResNet-50 was fine-tuned using different train-validation-test splits:

- **80% training, 10% validation, 10% testing**
- **70% training, 10% validation, 20% testing**
- **40% training, 30% validation, 30% testing**

The extracted embeddings were then used with **df-analyze** for model comparison.

---

### 4. PEFT Experiment

Parameter Efficient Fine-Tuning was applied to improve model learning while reducing the amount of training required.

The embeddings generated after PEFT were used for further model evaluation and comparison.

---

## Key Results

The best-performing models achieved very high classification performance.

For the full dataset experiment, **Logistic Regression** achieved approximately:

| Metric | Score |
|---|---:|
| Accuracy | 99.7% |
| AUROC | 1.000 |
| Balanced Accuracy | 99.1% |
| F1 Score | 99.5% |

**Stochastic Gradient Descent** also performed strongly and remained consistent across multiple experiments.

---

## Results Screenshots

### Holdout Set Performance on Full Dataset

![Holdout Set Performance on Full Dataset](<screenshots/Holdout set performance on full dataset.png>)

### 5-Fold Performance on Full Dataset

![5-Fold Performance on Full Dataset](<screenshots/5-fold performance on full dataset.png>)

---

## Key Insights

- Logistic Regression and SGD were the most consistent models across the experiments.
- df-analyze made it easier to compare multiple machine learning models efficiently.
- ResNet-50 embeddings helped convert chest X-ray images into useful numerical features for classification.
- Downsampling reduced performance slightly, but the best models still maintained strong results.
- The project shows how machine learning and deep learning-based feature extraction can support medical image classification tasks.

---

## Repository Structure

```text
src/
    Python scripts for data preparation, label mapping, dataset splitting, and X-Vision Helper usage.

reports/
    Final project report and phase report.

presentation/
    Project presentation file.

results/
    df-analyze results, downsampling results, fine-tuning results, and PEFT results.

screenshots/
    Dataset sample and model performance screenshots.
```

---

## Files Included

- Source code files used for data preparation, label mapping, dataset splitting, and model workflow.
- Final project report.
- Phase 3 project report.
- Project presentation.
- df-analyze result files.
- Downsampling experiment results.
- Fine-tuning experiment results.
- PEFT result file.
- Screenshots showing dataset sample and model performance.

---

## Note

The dataset and generated embedding files are not included in this repository because of file size and licensing limitations.

The results, reports, code files, presentation, and screenshots are included for reference.

Large generated files such as parquet files, model files, full image datasets, and compressed dataset files should be excluded from the repository.