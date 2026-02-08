"""
Example experiment: Simple Linear Regression

This is a basic example demonstrating the structure of an experiment in Sweven Labs.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def generate_sample_data(n_samples=100, noise=0.1):
    """Generate synthetic data for regression."""
    np.random.seed(42)
    X = np.random.rand(n_samples, 1) * 10
    y = 2.5 * X.squeeze() + 1.5 + np.random.randn(n_samples) * noise
    return X, y


def train_model(X_train, y_train):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R² Score: {r2:.4f}")
    print(f"Model coefficients: {model.coef_}")
    print(f"Model intercept: {model.intercept_:.4f}")
    
    return y_pred


def visualize_results(X_test, y_test, y_pred):
    """Visualize predictions vs actual values."""
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual', alpha=0.6)
    plt.plot(X_test, y_pred, color='red', label='Predicted', linewidth=2)
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression: Actual vs Predicted')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('experiments/example_regression_results.png')
    print("Results saved to 'experiments/example_regression_results.png'")


def main():
    """Main experiment workflow."""
    print("=" * 60)
    print("Example Experiment: Linear Regression")
    print("=" * 60)
    
    # Generate data
    print("\n1. Generating sample data...")
    X, y = generate_sample_data(n_samples=100, noise=5)
    
    # Split data
    print("2. Splitting data into train/test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    print("3. Training model...")
    model = train_model(X_train, y_train)
    
    # Evaluate
    print("4. Evaluating model...")
    y_pred = evaluate_model(model, X_test, y_test)
    
    # Visualize
    print("5. Generating visualization...")
    visualize_results(X_test, y_test, y_pred)
    
    print("\n" + "=" * 60)
    print("Experiment completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
