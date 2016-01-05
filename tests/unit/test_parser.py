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

    self.metadata_types = {
      'name': str,
      'title': str,
      'owner_org': str,
      'author': str,
      'author_email': str,
      'maintainer': str,
      'maintainer_email': str,
      'license_id': str,
      'license_other': str,
      'dataset_date': str,
      'subnational': int,
      'notes': str,
      'caveats': type(None),
      'methodology': str,
      'methodology_other': type(None),
      'dataset_source': str,
      'package_creator': str,
      'private': bool,
      'url': type(None),
      'state': str,
      'tags': list,
      'groups': list
    }

    self.resource_types = {
      "package_id": str,
      "url": str,
      "name": str,
      "format": str,
      "description": type(None)
    }

  def test_parser_returns_metadata_and_resource(self):
    '''
    parser: Tests that both the dataset and the resource objects are returned.

    '''
    d = Dataset(self.dataset_id).info()
    result = parse_dataset(d)

    self.assertIs(type(result), type({}))

    for key in ['metadata', 'resources']:
      self.assertIn(key, result.keys())


  def test_metadata_is_complete(self):
    '''
    parser: Tests that the metadata property is complete.

    '''
    d = Dataset(self.dataset_id).info()
    result = parse_dataset(d)

    for key in self.metadata_types.keys():
      print(key)
      print(result['metadata'][key])
      self.assertIs(type(result['metadata'][key]), self.metadata_types[key])
