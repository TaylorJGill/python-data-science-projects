# ECG Signal Processing & Arrhythmia Classification

This project processes and classifies ECG (electrocardiogram) signals using signal processing techniques and machine learning. It is split into two Jupyter notebooks.

---

## Part 1 — Signal Processing (`ecg_part1_signal_processing.ipynb`)

Processes a raw ECG time-series signal through a full pipeline:

1. Load and inspect the raw signal
2. Handle missing values via linear interpolation
3. Denoise using Fast Fourier Transform (low-pass filter at 100 Hz)
4. Detect R-peaks using cross-correlation with derivative-based kernels
5. Calculate instantaneous heart rate from R-peak intervals

**Tools:** NumPy, SciPy (FFT, ndimage), Pandas, Matplotlib

---

## Part 2 — Arrhythmia Classification (`ecg_part2_classification.ipynb`)

Builds and compares three machine learning classifiers to detect arrhythmia types from labeled ECG signal segments.

- **Dataset:** 3,841 samples × 187 time points, across 5 classes (normal + 4 arrhythmia types)
- **Models:** K-Nearest Neighbors, Decision Tree, Random Forest
- **Tuning:** GridSearchCV with 5-fold cross-validation
- **Result:** Random Forest achieved the best test accuracy (~84.8%)

**Tools:** NumPy, Pandas, Matplotlib, scikit-learn

---

## Setup

### Requirements

```bash
pip install numpy pandas matplotlib scipy scikit-learn jupyter
```

### Data Files

The notebooks require the following CSV files (included in this repo):

| Notebook | File |
|----------|------|
| Part 1 | `project_ecg_part1_signal_missing_value.csv` |
| Part 2 | `ECG_dataX.csv`, `ECG_dataY.csv` |

Update the file path in the data loading cell to match your local setup.

### Running the Notebooks

```bash
jupyter notebook
```

Then open either notebook from the Jupyter interface.
