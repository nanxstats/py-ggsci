"""Shared pytest fixtures."""

from collections.abc import Iterator

import numpy as np
import pytest


@pytest.fixture
def preserve_numpy_random_state() -> Iterator[None]:
    """Restore NumPy's global RNG state after a test."""
    state = np.random.get_state()
    try:
        yield
    finally:
        np.random.set_state(state)
