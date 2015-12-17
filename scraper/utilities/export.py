#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Exports datasets to a directory on the right HDX format.

'''
import json

def exportJson(data=None):
  '''
  Function to export a dictionary into a JSON file.

  '''
  with open('data/data.json', 'w') as file:
    json.dump(data, file)
