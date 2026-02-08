# Contributing to Sweven Labs

Thank you for your interest in contributing to Sweven Labs! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. Create a new issue with a descriptive title
3. Include steps to reproduce, expected behavior, and actual behavior
4. Add relevant labels (bug, enhancement, documentation, etc.)

### Suggesting Enhancements

1. Check if the enhancement has been suggested
2. Create an issue describing the enhancement
3. Explain why this enhancement would be useful
4. Provide examples if possible

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes following the coding standards
4. Write or update tests as needed
5. Update documentation if needed
6. Commit with clear, descriptive messages
7. Push to your fork
8. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/sweven-labs.git
cd sweven-labs

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .

# Check code quality
ruff check .
```

## Coding Standards

### Python Style

- Follow PEP 8 guidelines
- Use `black` for code formatting (line length: 100)
- Use `ruff` for linting
- Add type hints where appropriate
- Write docstrings for functions and classes

### Example

```python
def process_data(input_path: str, output_path: str) -> pd.DataFrame:
    """Process raw data and save to output file.
    
    Args:
        input_path: Path to input CSV file
        output_path: Path to save processed data
        
    Returns:
        Processed DataFrame
        
    Raises:
        FileNotFoundError: If input file doesn't exist
    """
    # Implementation
    pass
```

### Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage
- Use pytest for testing

### Documentation

- Update README.md if adding new features
- Add docstrings to new functions and classes
- Create or update documentation in `docs/`
- Include examples where helpful

## Project Structure Guidelines

- **experiments/**: Each experiment in its own directory with README
- **scripts/**: Standalone scripts with CLI arguments
- **src/**: Reusable code organized into modules
- **tests/**: Mirror the structure of src/
- **notebooks/**: Use numbered prefixes (01_, 02_, etc.)

## Commit Messages

Use clear, descriptive commit messages:

```
feat: Add new data preprocessing pipeline
fix: Resolve issue with model serialization
docs: Update installation instructions
test: Add tests for data loaders
refactor: Simplify training loop logic
```

## Review Process

1. Maintainers will review your PR
2. Address any feedback or requested changes
3. Once approved, your PR will be merged
4. Your contribution will be credited

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion in GitHub Discussions
- Reach out to maintainers

Thank you for contributing to Sweven Labs! 🎉
