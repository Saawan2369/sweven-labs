"""
Data processing script example

This script demonstrates how to process raw data and save it for model training.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_raw_data(file_path):
    """Load raw data from CSV file."""
    print(f"Loading data from {file_path}...")
    # In a real scenario, this would load actual data
    # For this example, we'll generate synthetic data
    np.random.seed(42)
    data = pd.DataFrame({
        'feature1': np.random.randn(1000),
        'feature2': np.random.randn(1000),
        'feature3': np.random.randn(1000),
        'target': np.random.randint(0, 2, 1000)
    })
    return data


def clean_data(df):
    """Clean and preprocess the data."""
    print("Cleaning data...")
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()
    
    # Remove outliers (simple example using IQR method)
    for col in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    
    return df


def engineer_features(df):
    """Create new features from existing ones."""
    print("Engineering features...")
    
    # Example: Create interaction features
    df['feature1_x_feature2'] = df['feature1'] * df['feature2']
    df['feature_sum'] = df['feature1'] + df['feature2'] + df['feature3']
    
    # Example: Create polynomial features
    df['feature1_squared'] = df['feature1'] ** 2
    
    return df


def save_processed_data(df, output_path):
    """Save processed data to file."""
    print(f"Saving processed data to {output_path}...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")


def main():
    """Main data processing pipeline."""
    print("=" * 60)
    print("Data Processing Pipeline")
    print("=" * 60)
    
    # Define paths
    raw_data_path = "data/raw/sample_data.csv"
    processed_data_path = Path("data/processed/processed_data.csv")
    
    # Load data
    df = load_raw_data(raw_data_path)
    print(f"Loaded {len(df)} rows")
    
    # Clean data
    df = clean_data(df)
    print(f"After cleaning: {len(df)} rows")
    
    # Engineer features
    df = engineer_features(df)
    print(f"Added {len(df.columns) - 4} new features")
    
    # Save processed data
    save_processed_data(df, processed_data_path)
    
    # Print summary statistics
    print("\nProcessed Data Summary:")
    print(df.describe())
    
    print("\n" + "=" * 60)
    print("Data processing completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
