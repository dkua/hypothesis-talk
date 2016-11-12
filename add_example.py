#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Unit Tests

def test_add_zero():
    assert 0 + 1 == 1 + 0

def test_add_single_digits():
    assert 1 + 2 == 2 + 1

def test_add_double_digits():
    assert 10 + 12 == 12 + 10


# Property-based Test

from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_add(x, y):
    assert x + y == y + x
