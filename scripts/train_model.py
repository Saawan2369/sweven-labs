"""
Model training script example

This script demonstrates how to train a machine learning model with configurable parameters.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import joblib


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Train a machine learning model')
    parser.add_argument('--data', type=str, default='data/processed/processed_data.csv',
                        help='Path to processed data')
    parser.add_argument('--n-estimators', type=int, default=100,
                        help='Number of trees in random forest')
    parser.add_argument('--max-depth', type=int, default=10,
                        help='Maximum depth of trees')
    parser.add_argument('--output-dir', type=str, default='models/example_model',
                        help='Directory to save model')
    return parser.parse_args()


def load_data(data_path):
    """Load processed data for training."""
    print(f"Loading data from {data_path}...")
    # Generate synthetic data for demonstration
    np.random.seed(42)
    X = np.random.randn(1000, 5)
    y = np.random.randint(0, 2, 1000)
    return X, y


def train_model(X_train, y_train, n_estimators, max_depth):
    """Train the model."""
    print(f"Training Random Forest with {n_estimators} estimators, max_depth={max_depth}...")
    
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_train, y_train, X_test, y_test):
    """Evaluate model performance."""
    print("\nEvaluating model...")
    
    # Cross-validation on training set
    cv_scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"Cross-validation scores: {cv_scores}")
    print(f"Mean CV score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
    
    # Test set evaluation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nTest set accuracy: {accuracy:.4f}")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return {
        'cv_scores': cv_scores.tolist(),
        'mean_cv_score': float(cv_scores.mean()),
        'std_cv_score': float(cv_scores.std()),
        'test_accuracy': float(accuracy)
    }


def save_model(model, metrics, config, output_dir):
    """Save model, metrics, and configuration."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Save model
    model_path = output_path / 'model.pkl'
    joblib.dump(model, model_path)
    print(f"\nModel saved to {model_path}")
    
    # Save metrics
    metrics_path = output_path / 'metrics.json'
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"Metrics saved to {metrics_path}")
    
    # Save configuration
    config_path = output_path / 'config.json'
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    print(f"Configuration saved to {config_path}")


def main():
    """Main training pipeline."""
    args = parse_args()
    
    print("=" * 60)
    print("Model Training Pipeline")
    print("=" * 60)
    
    # Load data
    X, y = load_data(args.data)
    print(f"Loaded data: X shape = {X.shape}, y shape = {y.shape}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    
    # Train model
    model = train_model(X_train, y_train, args.n_estimators, args.max_depth)
    
    # Evaluate model
    metrics = evaluate_model(model, X_train, y_train, X_test, y_test)
    
    # Prepare configuration
    config = {
        'timestamp': datetime.now().isoformat(),
        'data_path': args.data,
        'n_estimators': args.n_estimators,
        'max_depth': args.max_depth,
        'train_samples': len(X_train),
        'test_samples': len(X_test)
    }
    
    # Save everything
    save_model(model, metrics, config, args.output_dir)
    
    print("\n" + "=" * 60)
    print("Training completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
