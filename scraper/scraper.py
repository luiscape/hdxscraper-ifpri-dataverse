import os
from dataverse import Connection

host = 'dataverse.harvard.edu'                  # All clients >4.0 are supported
token = os.getenv('DATAVERSE_KEY', None)

connection = Connection(host, token)

dataverse = connection.get_dataverse('ALIAS')
dataset = dataverse.get_dataset_by_doi('DOI:10.5072/FK2/ABC123')
files = dataset.get_files('latest')

print(files)
