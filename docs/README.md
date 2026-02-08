# Documentation

This directory contains project documentation, guides, and references.

## Contents

- **Architecture**: System design and component diagrams
- **API Reference**: Documentation for public APIs
- **Tutorials**: Step-by-step guides for common tasks
- **Best Practices**: Coding standards and conventions
- **Research Notes**: Literature reviews and research findings

## Documentation Tools

Consider using:
- **Sphinx**: Generate documentation from docstrings
- **MkDocs**: Create beautiful project documentation
- **Jupyter Book**: Create books from Jupyter notebooks
- **README-driven development**: Write documentation before code

## Suggested Structure

```
docs/
├── getting-started.md
├── architecture.md
├── api-reference.md
├── tutorials/
│   ├── 01-setup.md
│   ├── 02-first-experiment.md
│   └── 03-model-training.md
├── guides/
│   ├── data-preparation.md
│   └── model-deployment.md
└── research/
    ├── literature-review.md
    └── experiment-logs.md
```

## Building Documentation

If using Sphinx:
```bash
cd docs
make html
```

If using MkDocs:
```bash
mkdocs serve  # Local preview
mkdocs build  # Build static site
```

## Best Practices

1. Keep documentation close to code
2. Update docs when changing functionality
3. Include code examples and visuals
4. Use consistent formatting (Markdown)
5. Make documentation searchable
