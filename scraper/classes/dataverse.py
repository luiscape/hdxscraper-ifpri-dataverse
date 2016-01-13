#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
DATAVERSE CLASS:
---------------

It helps define what is a dataverse in relationship
with other objects (i.e. datasets).

'''
import requests
from simplejson import JSONDecodeError

class Dataverse(object):
  '''
  Creates a dataverse object. The object collects basic information
  for other more granular objects (i.e. Dataset), and helps them inherit
  those.

  '''
  def __init__(self, host, alias):
    self.host = host
    self.alias = alias
    self.connection = 'https://{host}/api/dataverses/{alias}'.format(host=self.host, alias=self.alias)

  def info(self):
    '''
    Collects basic information about the dataverse alias.

    '''
    r = requests.get(self.connection)
    return r.json()['data']

  def contents(self):
    '''
    Fetches a list of available datasets.

    '''
    r = requests.get(self.connection + '/contents')
    try:
      return r.json()['data']

    except JSONDecodeError:
      print(r.text)
      raise ValueError('Could not fetch data from Dataverse.')

