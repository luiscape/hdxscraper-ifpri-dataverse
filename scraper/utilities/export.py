#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Exports datasets to a directory on the right HDX format.

'''
import json

def export_json(data=None, path='data/data.json'):
  '''
  Function to export a dictionary into a JSON file.

  '''
  with open(path, 'w') as file:
    json.dump(data, file)
