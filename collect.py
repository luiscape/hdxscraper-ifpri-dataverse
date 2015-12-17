#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
COLLECTOR:
---------

Here includes the main part of the collector program.
We list all the contents of a particular Dataverse and
proceed to instantiate its results.

'''
from scraper.utilities.item import item
from scraper.utilities.export import exportJson

from scraper.classes.dataset import Dataset
from scraper.classes.dataverse import Dataverse

def main():
  '''
  Program wrapper.

  '''
  print('%s Creating Dataverse instance.' % item('bullet'))
  d = Dataverse('dataverse.harvard.edu', 'IFPRI')

  print('%s Collecting all contenst from Dataverse.' % item('bullet'))
  contents = d.contents()

  datasets = []
  for dataset in contents:
    print('%s Collecting data for ID %s.' % (item('bullet'), dataset['id']))
    o = Dataset(dataset['id']).info()

    if o.get('status', None) == 'ERROR':
      continue
    else:
      datasets.append(o)

  exportJson(datasets)
  print('%s Total datasets downloaded %s' % (item('success'), str(len(datasets))))

if __name__ == '__main__':
  main()
