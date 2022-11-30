#!/usr/bin/python3.5
"""Module uses Numpy to multiply two matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a = matrix a
        m_b = matrix b
    Returns:
        multiplication result
    """

    return (np.matmul(m_a, m_b))
