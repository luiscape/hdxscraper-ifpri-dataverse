#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the item() utility function.
'''
import unittest

from scraper.utilities.item import item

class TestUtilityItem(unittest.TestCase):
  '''
  Tests for the item() utility function.
  '''
  def test_item_returns_correct_type(self):
    '''
    item() utility function returns the right type.
    '''
    result = item('bullet')
    self.assertIs(type(result), str)
