#!/usr/bin/env python3
"""Test utils.py
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""
    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({'a': 1}, ['b']),
        ({'a': {'b': 2}}, ['a', 'c']),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
