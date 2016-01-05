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
from datetime import datetime

def parse_dataset(data):
  '''
  Function that parses a dataset.

  '''

  data['latestVersion']['metadataBlocks']

  #
  # Default resource.
  #
  default_resource = {
    "package_id": None,
    "url": None,
    "name": None,
    "format": None,
    "description": None
  }

  #
  # Default dataset.
  #
  default_metadata = {
    'name': None,
    'title': None,
    'owner_org': 'opennepal',  # default for OpenNepal
    'author': '',
    'author_email': '',  # default for OpenNepal
    'maintainer': '',  # default for OpenNepal
    'maintainer_email': '',  # default for OpenNepal
    'license_id': 'hdx-other',  # default for OpenNepal
    'license_other': None,
    'dataset_date': None,  # has to be in MM/DD/YYYY format.
    'subnational': 0,  # has to be 0 or 1. Default 1 for OpenNepal.
    'notes': None,
    'caveats': None,
    'methodology': 'Other',  # default for OpenNepal
    'methodology_other': None,
    'dataset_source': 'OpenNepal',
    'package_creator': 'luiscape',
    'private': False,  # has to be True or False
    'url': None,
    'state': 'active',  # always "active"
    'tags': [],  # has to be a list with {'name': None}
    'groups': []  # has to be ISO-3-letter-code. {'id': None}
    }

  return { 'metadata': default_metadata, 'resources': [ default_resource ]}
