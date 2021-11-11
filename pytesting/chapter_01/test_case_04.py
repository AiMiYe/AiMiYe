#!/usr/bin/env python
import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_case():
    pass


if __name__ == '__main__':
    pytest.main(['-s', '-v'])
