# Source Code

This directory contains reusable Python modules and packages for the project.

## Structure

Organize code into logical modules:
```
src/
├── __init__.py
├── data/
│   ├── __init__.py
│   ├── loaders.py
│   └── preprocessors.py
├── models/
│   ├── __init__.py
│   ├── architectures.py
│   └── training.py
├── evaluation/
│   ├── __init__.py
│   └── metrics.py
└── utils/
    ├── __init__.py
    ├── config.py
    └── logging.py
```

## Best Practices

1. **Modular Design**: Create small, focused modules with single responsibilities
2. **Type Hints**: Use Python type hints for better code clarity
3. **Documentation**: Use docstrings (Google or NumPy style)
4. **Testing**: Write unit tests in the `tests/` directory
5. **Code Style**: Follow PEP 8 and use tools like `black`, `ruff`, or `pylint`

## Installation

To use the code as a package:
```bash
pip install -e .
```

Then import in your code:
```python
from src.data import loaders
from src.models import architectures
```

## Example Module

```python
"""Data loading utilities."""

from typing import Tuple
import pandas as pd


def load_dataset(path: str) -> Tuple[pd.DataFrame, pd.Series]:
    """Load dataset from CSV file.
    
    Args:
        path: Path to CSV file
        
    Returns:
        Tuple of features DataFrame and target Series
    """
    # Implementation here
    pass
```
