# Models

This directory contains trained machine learning models and their metadata.

## Structure

Each model should include:
- Model weights/checkpoints (`.pth`, `.h5`, `.pkl`, etc.)
- Model configuration files
- Training metrics and evaluation results
- Model card with performance metrics and usage instructions

## Best Practices

1. Use semantic versioning for model versions (e.g., `model-v1.0.0`)
2. Document model architecture and training data
3. Include evaluation metrics and test results
4. Store large models in external storage (S3, GCS, etc.) and reference them
5. Keep model metadata in version control

## Model Registry

Consider using tools like:
- MLflow for model tracking
- Weights & Biases for experiment management
- DVC for data and model versioning

## Example Structure

```
models/
├── image-classifier/
│   ├── v1.0.0/
│   │   ├── model.pth
│   │   ├── config.json
│   │   ├── metrics.json
│   │   └── README.md
│   └── v1.1.0/
└── text-generator/
```
