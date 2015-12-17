#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
DATASET CLASS:
---------------

Defines what a dataset is. It inherits from a dataverse class.

'''
import requests

class Dataset(object):
  '''
  Dataset class contains the dataset fetching functions.
  It must be initialized with a dataset ID.

  '''
  def __init__(self, id):
    self.id = id

  def info(self):
    '''
    Fetches basic information from a dataset by ID.

    '''
    r = requests.get('https://dataverse.harvard.edu/api/datasets/{id}'.format(id=self.id))

    if r.json()['status'] == 'OK':
      return r.json()['data']

    else:
      return { 'status': 'ERROR', 'id': self.id }
