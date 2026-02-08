# Getting Started with Sweven Labs

This guide will help you get started with your first experiment in Sweven Labs.

## Prerequisites

- Python 3.9 or higher installed
- Git for version control
- Basic knowledge of Python and machine learning

## Step 1: Set Up Your Environment

### 1.1 Clone the Repository

```bash
git clone https://github.com/Saawan2369/sweven-labs.git
cd sweven-labs
```

### 1.2 Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n sweven-labs python=3.9
conda activate sweven-labs
```

### 1.3 Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Run Your First Experiment

### 2.1 Try the Example Experiment

```bash
python experiments/example_regression.py
```

This will:
- Generate synthetic data
- Train a simple linear regression model
- Evaluate the model
- Create a visualization

### 2.2 Explore the Example Notebook

```bash
jupyter lab
```

Open `notebooks/01_example_eda.ipynb` and run through the cells to see exploratory data analysis in action.

## Step 3: Create Your Own Experiment

### 3.1 Create Experiment Directory

```bash
mkdir experiments/my_first_experiment
cd experiments/my_first_experiment
```

### 3.2 Create Your Experiment Script

Create a file `experiment.py`:

```python
"""My First Experiment: Image Classification"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    # Load data
    print("Loading dataset...")
    digits = load_digits()
    X, y = digits.data, digits.target
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    print("Training model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
```

### 3.3 Create Experiment README

Create `README.md`:

```markdown
# My First Experiment: Digit Classification

## Objective
Train a Random Forest classifier on the digits dataset.

## Dataset
- Source: sklearn.datasets.load_digits
- Samples: 1797
- Features: 64 (8x8 pixel values)
- Classes: 10 (digits 0-9)

## Results
- Accuracy: XX.XX%
- Training time: X seconds

## Conclusions
[Your findings here]
```

### 3.4 Run Your Experiment

```bash
python experiment.py
```

## Step 4: Work with Data

### 4.1 Add Your Data

Place your data files in the appropriate directory:
- `data/raw/` - Original data
- `data/external/` - Third-party data

### 4.2 Process Your Data

Use the example script:

```bash
python scripts/process_data.py
```

Or create your own processing script in `scripts/`.

## Step 5: Train and Save Models

### 5.1 Train a Model

```bash
python scripts/train_model.py \
    --data data/processed/your_data.csv \
    --n-estimators 100 \
    --output-dir models/my_model
```

### 5.2 Model Directory Structure

Your trained model will be saved with:
- `model.pkl` - The trained model
- `config.json` - Training configuration
- `metrics.json` - Evaluation metrics

## Step 6: Document Your Work

Always document your experiments:

1. **Experiment README**: Describe objectives, methods, and results
2. **Code Comments**: Explain non-obvious logic
3. **Notebooks**: Use markdown cells to explain your analysis
4. **Git Commits**: Write clear commit messages

## Step 7: Best Practices

### Version Control

```bash
# Check status
git status

# Add files
git add experiments/my_first_experiment/

# Commit with descriptive message
git commit -m "feat: Add digit classification experiment"

# Push to your fork
git push origin main
```

### Code Quality

```bash
# Format code
black experiments/my_first_experiment/

# Check for issues
ruff check experiments/my_first_experiment/
```

### Testing

If you create reusable code in `src/`, write tests:

```bash
pytest tests/
```

## Next Steps

- Explore more complex experiments
- Try different ML algorithms
- Work with real datasets
- Create interactive visualizations
- Share your findings

## Getting Help

- Check the main [README.md](../README.md)
- Review example scripts and notebooks
- Open an issue on GitHub
- Join discussions

Happy experimenting! 🚀
