#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
PARSER:
-------

This parser will intake dataverse dataset classes and
generate an HDX-like dictionary. It was designed to
register datasets in HDX in a posterior process.

'''

## 'files' contain the files.
## country will be inside geospatial > fields > country > value -- will give full name
##   need to parse into ISO3 codes.
## title will be in 'fields' > 'typeName':'title'
## in order to download files, you'll need to append https://dataverse.harvard.edu/api/access/datafile/
## to all file IDs -- those that have file names.
## value > dsDescriptionValue contains the description

import os
import sys
import json
import requests

from copy import copy
from slugify import slugify
from datetime import datetime
from countrycode import countrycode

def parse_dataset(data, private=True):
  '''
  Function that parses a dataset.

  '''
  resource = {
    "package_id": None,
    "url": None,
    "name": None,
    "format": None,
    "description": None
  }

  metadata = {
    'name': None,
    'title': None,
    'owner_org': 'ifpri',
    'author': 'ifpridata',
    'author_email': 'ifpri-data@cgiar.org',
    'maintainer': 'ifpridata',
    'maintainer_email': 'ifpri-data@cgiar.org',
    'license_id': 'hdx-other',
    'license_other': '',
    'dataset_date': None,  # has to be MM/DD/YYYY
    'subnational': 1,  # has to be 0 or 1. Default 1 for IFPRI.
    'notes': None,
    'caveats': None,
    'methodology': 'Other',
    'methodology_other': None,
    'dataset_source': '',
    'package_creator': 'luiscape',
    'private': private,  # has to be True or False
    'url': None,
    'state': 'active',  # always "active".
    'tags': [{ 'name': 'Food' }, { 'name': 'Security' }],  # has to be a list with { 'name': None }
    'groups': []  # has to be ISO-3-letter-code. { 'id': None }
    }

  #
  #  Parsing for:
  #    - metadata name
  #    - metadata title
  #    - metadata dataset_date
  #    - metadata notes
  #    - metadata groups (countries)
  #    - metadata source
  #
  for field in data['latestVersion']['metadataBlocks']['citation']['fields']:

    if field.get('typeName') == 'title':
      metadata['title'] = str(field['value'])
      metadata['name'] = str(slugify(field['value']))

    if field.get('typeName') == 'timePeriodCovered':
      for f in field['value']:
        if f.get('timePeriodCoveredStart') is not None:
          metadata['dataset_date'] = str(f['timePeriodCoveredStart']['value'])
        else:
          metadata['dataset_date'] = ''

    authors = []
    if field.get('typeName') == 'author':
      for f in field['value']:
        if f.get('value') is not None:
          authors.append(f.get('value'))

      metadata['dataset_source'] = ', '.join(authors)


    if field.get('typeName') == 'dsDescription':
      metadata['notes'] = str(field.get('value')[0].get('dsDescriptionValue').get('value'))


  for location in data['latestVersion']['metadataBlocks']['geospatial']['fields']:
    if location.get('typeName') == 'geographicCoverage':
      for country in location.get('value'):
        name = country[list(country)[0]]['value']
        result = { 'id': countrycode(codes='Vietnam', origin='country_name', target='iso3c') }
        metadata['groups'].append(result)


  resources = []
  desired_file_extensions = ['xls', 'xlsx', 'csv', 'zip', 'tsv', 'shp', 'geojson', 'json']
  for file in data['latestVersion']['files']:

    #
    #  Checking for data file.
    #
    file_name = file.get('datafile').get('name')

    if file_name is not None:
      extension = os.path.splitext(file_name)[1][1:].lower()
      if extension in desired_file_extensions:
        resource['package_id'] = metadata['name']
        resource['url'] = 'https://dataverse.harvard.edu/api/access/datafile/' + str(file['datafile'].get('id'))
        resource['name'] = file_name
        resource['format'] = extension.upper()

        resources.append(copy(resource))

    else:
      continue


  return { 'metadata': metadata, 'resources': resources }
