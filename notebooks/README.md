# Notebooks

This directory contains Jupyter notebooks for exploratory data analysis, visualization, and prototyping.

## Naming Convention

Use descriptive names with numbers for ordering:
- `01_data_exploration.ipynb`
- `02_feature_engineering.ipynb`
- `03_model_training.ipynb`
- `04_results_visualization.ipynb`

## Best Practices

1. **Clear Structure**: Use markdown cells to organize your notebook into sections
2. **Restart & Run All**: Ensure notebooks can run from top to bottom
3. **Version Control**: Clear output cells before committing (or use `nbstripout`)
4. **Documentation**: Explain your thought process and findings
5. **Modular Code**: Move reusable code to Python modules in `src/`

## Tools

- **Jupyter Lab**: Modern interface for notebooks
- **nbconvert**: Convert notebooks to HTML, PDF, or Python scripts
- **papermill**: Parameterize and execute notebooks
- **nbdime**: Better notebook diffs in Git

## Converting to Scripts

When code stabilizes, convert notebooks to Python scripts:
```bash
jupyter nbconvert --to script notebook.ipynb
```
