import unittest
from unittest.mock import patch, MagicMock
from cli_api import compare_packages


class TestComparePackages(unittest.TestCase):
    @patch('cli_api.get_packages')
    def test_compare_packages(self, mock_get_packages):
        branches = ['branch1', 'branch2']
        arch = 'x86_64'
        mock_get_packages.side_effect = [
            {
                'package1': {'version': '1.0', 'release': '1'},
                'package2': {'version': '2.0', 'release': '1'}
            },
            {
                'package1': {'version': '1.0', 'release': '2'},
                'package3': {'version': '3.0', 'release': '1'}
            }
        ]
        expected_result = {
            'only_in_1st': {'package1': {'version': '2.0', 'release': '1'}},
            'only_in_2nd': {'package2': {'version': '3.0', 'release': '1'}},
            'higher_in_1st': {'package3': {'version': '1.0', 'release': '1'}}
        }
        self.assertEqual(compare_packages(branches, arch), expected_result)

    @patch('cli_api.get_packages', MagicMock(return_value={}))
    def test_compare_packages_empty(self):
        branches = ['branch1', 'branch2']
        arch = 'x86_64'
        expected_result = {
            'only_in_1st': {},
            'only_in_2nd': {},
            'higher_in_1st': {}
        }
        self.assertEqual(compare_packages(branches, arch), expected_result)