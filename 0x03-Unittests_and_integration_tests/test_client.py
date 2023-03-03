#!/usr/bin/env python3

"""Test client.py"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_get):
        """Test org"""
        test_url = f"https://api.github.com/orgs/{test_org}"
        test_payload = {"payload": True}
        mock_get.return_value = test_payload
        test_client = GithubOrgClient(test_org)
        self.assertEqual(test_client.org, test_payload)
        mock_get.assert_called_once_with(test_url)

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get):
        """Test public repos url"""
        test_payload = {"repos_url": "holberton.io"}
        mock_get.return_value = test_payload
        test_client = GithubOrgClient("google")
        test_client.org = test_payload
        self.assertEqual(test_client._public_repos_url,
                         test_payload["repos_url"])
        mock_get.assert_not_called()

    @parameterized.expand([
        ("google", {"repos_url": "holberton.io"}),
        ("abc", {"repos_url": "example.com"}),
    ])
    @patch('client.get_json')
    def test_public_repos(self, test_org, test_payload, mock_get):
        """Test public repos"""
        test_client = GithubOrgClient(test_org)
        test_client.org = test_payload
        test_client._public_repos_url = test_payload["repos_url"]
        test_repos = ["holberton", "school"]
        mock_get.return_value = test_repos
        self.assertEqual(test_client.public_repos(), test_repos)
        mock_get.assert_called_once_with(test_payload["repos_url"])

    @parameterized.expand([
        ("google", {"repos_url": "holberton.io"}, "MIT", ["holberton"]),
        ("abc", {"repos_url": "example.com"}, "BSD", []),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license(self, test_org, test_payload,
                                       test_license,
                                       test_repos, mock_get):
        """Test public repos with license"""
        test_client = GithubOrgClient(test_org)
        test_client.org = test_payload
        test_client._public_repos_url = test_payload["repos_url"]
        mock_get.return_value = test_repos
        self.assertEqual(test_client.public_repos(test_license), test_repos)
