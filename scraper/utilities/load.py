#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import csv
import json

from os import path as p
from scraper.utilities.item import item

def LoadConfig(config_path='config/dev.json', verbose=True):
  '''Load configuration parameters.'''

  try:
    with open(config_path) as json_file:
      config = json.load(json_file)

  except Exception as e:
    print("%s Couldn't load configuration." % item('error'))
    if verbose:
      print(e)
    return False

  return config
