"""Unit tests for rps.

Author: Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor: Masateru Nakanishi
* TU/e ID number: 1559206
* Date: 29/04/2020

This software is made available under the terms of the MIT License.
"""

import rps


def test_RPS() -> None:
    """Test constant initialization."""
    assert rps.RPS == "rps"


def test_what_beats_2() -> None:
    """Test rps.what_beats(1)."""
    assert rps.what_beats(2) == 0


def test_beats_0_2() -> None:
    """Test rps.beats(0, 2)."""
    assert rps.beats(0, 2)
