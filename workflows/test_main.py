"""A module for testing main detective_password function."""

from typing import Tuple

import pytest

from main import detective

test_data = [
            (('35'), ('35', '32', '34', '36', '38', '25', '65')),
            (('00'), ('00', '08', '80')),
            (('123'), ('123', '423', '223', '113', '153', '133', '122', '126')),
            (('56'), ('56', '53', '55', '59', '26', '46', '86', '66'))
            ]


@pytest.mark.parametrize('numbers, expected', test_data)

def test_detective(numbers: Tuple, expected: str) -> None:
    """Test detective function with test_data.

    Args:
        numbers: numbers to be passed to detective.
        expected: an actual expected detective result.

    Asserts:
        True if detective returns expected answers.
    """
    assert detective(*numbers) == expected
