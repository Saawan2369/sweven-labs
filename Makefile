.PHONY: help install install-dev test format lint clean

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies
	pip install -r requirements.txt

install-dev:  ## Install development dependencies
	pip install -e ".[dev]"

test:  ## Run tests
	pytest tests/ -v

test-cov:  ## Run tests with coverage
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

format:  ## Format code with black
	black .

lint:  ## Run linting checks
	ruff check .

clean:  ## Clean up generated files
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

notebook:  ## Start Jupyter Lab
	jupyter lab

example:  ## Run example experiment
	python experiments/example_regression.py
