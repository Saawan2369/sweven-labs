# Data

This directory contains datasets used in experiments and models.

## Structure

- `raw/`: Original, immutable data dumps
- `processed/`: Cleaned and transformed data ready for modeling
- `external/`: Data from third-party sources

## Guidelines

1. **Never commit large data files** - Use Git LFS or external storage
2. Keep raw data immutable - always create copies for processing
3. Document data sources and collection methods
4. Include data dictionaries when applicable
5. Use consistent file naming conventions

## Data Privacy

⚠️ **Important**: Never commit sensitive or personal data to version control.
Use `.gitignore` patterns to exclude data files and only commit metadata or small sample datasets.

## Example .gitignore entries for data

```
data/raw/*.csv
data/processed/*.parquet
data/external/*.json
!data/raw/sample_*.csv  # Allow small sample files
```
