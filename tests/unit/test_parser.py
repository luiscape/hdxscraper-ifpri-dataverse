#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the dataset parser.

'''
import unittest

from scraper.parser import parse_dataset
from scraper.classes.dataset import Dataset
from scraper.classes.dataverse import Dataverse

class TestParser(unittest.TestCase):
  '''
  Performs unit tests on the parsers. Requires both
  the Dataset and the Dataverse classes to be loaded.

  '''
  def setUp(self):
    self.host = 'dataverse.harvard.edu'
    self.alias = 'IFPRI'
    self.dataset_id = 57641
    self.dataverse = Dataverse(host=self.host, alias=self.alias)

  def test_parser_returns_dataset_and_resource(self):
    '''
    parser: Tests that both the dataset and the resource objects are returned.

    '''
    d = Dataset(self.dataset_id).info()
    result = parse_dataset(d)

    self.assertIs(type(result), type({}))

    for key in ['metadata', 'resources']:
      self.assertIn(key, result.keys())
