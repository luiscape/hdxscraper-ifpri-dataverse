#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import yajl as json
import progressbar as pb

from termcolor import colored as color
from scraper.utilities.item import item as I

def LoadData(p, verbose=True):
  '''Loading data from a local JSON resource.'''

  if verbose:
    print("--------------------------------------------------")
    print("%s Loading JSON data from %s." % (I('bullet'), p))

  try:
      data = json.load(open(p))

      if verbose:
          print("%s Data loaded successully. %s entities in dataset." % (I('bullet'), len(data)))
          print("--------------------------------------------------")


  except Exception as e:
      print("%s Could not load %s file." % (I('error'), p))
      return None


  #
  # Return data.
  #
  return data
