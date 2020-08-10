import json
import pandas as pd
import numpy as np

from elasticsearch import Elasticsearch

# Paths and other constants
# TODO: move config constants to config file
csv_path = 'songid_genre.tsv'
csv_delimiter = '\t'
csv_column_names = ['track_id', 'track_genre']

# ES constants
es_genres_index = 'genres'
clean_genres_index = True

es = Elasticsearch()


def matrix_row_to_json(row):
    json_item = json.dumps(row.to_dict())
    return json_item

# -------------- LOAD CSV INTO PANDAS MATRIX THEN INTO JSON ----------------
genres = pd.read_csv(csv_path, csv_delimiter, header=None)
genres.columns = csv_column_names
json_list = genres.apply(matrix_row_to_json, 'columns')

# -------------- DUMP JSONS INTRO ELASTICSEARCH ----------------
if clean_genres_index:
    es.indices.delete(index=es_genres_index, ignore=[400, 404])

result_list = [es.index(index=es_genres_index, body=json_item) for json_item in json_list]

