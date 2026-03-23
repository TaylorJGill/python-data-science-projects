# Python Data Science Projects

A collection of Python projects from my data science coursework, covering signal processing, machine learning classification, and AI game logic.

---

## Projects

### ECG Signal Processing & Arrhythmia Classification
Two-part project working with real ECG time-series data.
- **Part 1** — Full signal processing pipeline: missing value interpolation, FFT-based denoising, R-peak detection via cross-correlation, and heart rate calculation
- **Part 2** — Arrhythmia classification across 5 classes using KNN, Decision Tree, and Random Forest with GridSearchCV hyperparameter tuning

**Tools:** NumPy, SciPy, Pandas, Matplotlib, scikit-learn

→ [`ecg-signal-processing/`](ecg-signal-processing/)

---

### Tic Tac Toe AI
Human vs. computer Tic Tac Toe with a configurable AI player. Supports random play (N=0) and a one-step lookahead strategy (N=1) that wins when possible, blocks opponent threats, and prefers center and corner positions. Includes a full test suite compatible with both `pytest` and the standard library.

**Tools:** Python standard library

→ [`tic-tac-toe-ai/`](tic-tac-toe-ai/)

---

## Setup

Each project folder contains its own README with specific installation and usage instructions. In general:

```bash
git clone https://github.com/TaylorJGill/python-data-science-projects.git
cd python-data-science-projects
```

Then navigate to the project folder of interest.
