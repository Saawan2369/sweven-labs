"""
Sample test file

This demonstrates the structure for tests in Sweven Labs.
"""

import pytest


def test_example():
    """Example test case."""
    assert 1 + 1 == 2


def test_another_example():
    """Another example test case."""
    result = sum([1, 2, 3, 4])
    assert result == 10


@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return [1, 2, 3, 4, 5]


def test_with_fixture(sample_data):
    """Test using a fixture."""
    assert len(sample_data) == 5
    assert sum(sample_data) == 15
