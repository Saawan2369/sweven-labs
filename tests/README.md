# Tests

This directory contains unit tests and integration tests for the project.

## Structure

Mirror the structure of `src/`:
```
tests/
├── __init__.py
├── test_data/
│   ├── test_loaders.py
│   └── test_preprocessors.py
├── test_models/
│   └── test_architectures.py
└── conftest.py  # Shared fixtures
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_data/test_loaders.py

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x
```

## Best Practices

1. **Test Naming**: Use `test_` prefix for test functions
2. **Fixtures**: Use pytest fixtures for setup/teardown
3. **Coverage**: Aim for >80% code coverage
4. **Fast Tests**: Keep unit tests fast (<1s each)
5. **Mock External Calls**: Mock API calls and external services

## Example Test

```python
"""Tests for data loaders."""

import pytest
from src.data import loaders


def test_load_dataset_returns_correct_shape():
    """Test that loaded dataset has expected shape."""
    df, target = loaders.load_dataset("tests/fixtures/sample.csv")
    assert df.shape[0] == 100
    assert len(target) == 100


@pytest.fixture
def sample_dataframe():
    """Fixture providing sample DataFrame for tests."""
    return pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
```

## Continuous Integration

Tests should run automatically on:
- Pull requests
- Commits to main branch
- Pre-commit hooks (optional)
