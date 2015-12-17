#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the Dataverse class.
'''
import unittest

from scraper.classes.dataverse import Dataverse

class TestClassDataverse(unittest.TestCase):
  '''
  Performs tests on the Dataverse class.
  '''
  def setUp(self):
    self.host = 'dataverse.harvard.edu'
    self.alias = 'IFPRI'

  def test_info_is_collected_if_host_and_alias_are_correct(self):
    '''
    classes.dataverse: Tests that the Dataverse class returns info if initialized correctly.
    '''
    result = Dataverse(host=self.host, alias=self.alias).info()
    self.assertIs(type(result), type({}))

  def test_content_of_dataverse_returns_correctly(self):
    '''
    classes.dataverse: Tests that the content of a dataverse is returned correctly.
    '''
    result = Dataverse(host=self.host, alias=self.alias).contents()
    self.assertIs(type(result), type([]))
