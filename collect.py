#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
COLLECTOR:
---------

Here includes the main part of the collector program.
We list all the contents of a particular Dataverse and
proceed to instantiate its results.

'''
from scraper.parser import parse_dataset

from scraper.utilities.item import item
from scraper.utilities.export import export_json

from scraper.classes.dataset import Dataset
from scraper.classes.dataverse import Dataverse

def main():
  '''
  Program wrapper.

  '''
  print('%s Creating Dataverse instance.' % item('bullet'))
  d = Dataverse('dataverse.harvard.edu', 'IFPRI')

  print('%s Collecting all content from Dataverse.' % item('bullet'))
  contents = d.contents()

  #
  #  Collects data and organizes
  #  in lists and dictionaries.
  #
  datasets = []
  resources = []
  for dataset in contents:
    print('%s Collecting data for ID %s.' % (item('bullet'), dataset['id']))

    o = Dataset(dataset['id']).info()
    if o.get('status') is 'ERROR' or None:
      continue

    try:
      parsed_data = parse_dataset(o)
    except ValueError:
      print('%s Missing metadata. Not parsing.' % item('warn'))
      continue

    else:
      datasets.append(parsed_data['metadata'])
      resources += parsed_data['resources']

  #
  #  Exports JSON files to disk..
  #
  export_json(datasets, 'data/datasets.json')
  export_json(resources, 'data/resources.json')
  print('%s Total datasets downloaded %s' % (item('success'), str(len(datasets))))

if __name__ == '__main__':
  main()
