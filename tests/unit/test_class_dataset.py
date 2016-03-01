#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the Dataset class.

'''
import unittest

from scraper.classes.dataset import Dataset
from scraper.classes.dataverse import Dataverse

class TestClassDataset(unittest.TestCase):
  '''
  Performs tests on the Dataverse class.

  '''
  def setUp(self):
    self.host = 'dataverse.harvard.edu'
    self.alias = 'IFPRI'
    self.dataset_id = 57641
    self.dataset_id_error = 23748295482569256
    self.dataverse = Dataverse(host=self.host, alias=self.alias)

  def test_dataset_info_is_returned_correctly(self):
    '''
    Dataset information is returned correctly.

    '''
    result = Dataset(self.dataset_id).info()
    self.assertIs(type(result), type({}))

  def test_dataset_info_returns_error_if_doesnt_exist(self):
    '''
    Dataset returns an error message if it doesn't exist.

    '''
    result = Dataset(self.dataset_id_error).info()
    self.assertTrue(result['status'] == 'ERROR')
