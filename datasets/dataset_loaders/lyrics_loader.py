import json
import csv
import pandas as pd
import numpy as np
from scipy import sparse as sps

from elasticsearch import Elasticsearch

# Paths and other constants
# TODO: move config constants to config file
csv_path = 'subsets_for_debugging/songid_lyrics-mxm-dataset_train_subset.txt'
csv_delimiter = ','
csv_column_names = ['track_id', 'mxm_id', 'lyrics_vector']

# ES constants
es_genres_index = 'lyrics'
clean_genres_index = True

rows, columns = 5000, 2
matrix = sps.lil_matrix((rows, columns))

# es = Elasticsearch()

# def matrix_row_to_json(row):
#     json_item = json.dumps(row.to_dict())
#     return json_item

# -------------- LOAD CSV INTO SCIPY MATRIX ----------------
# For this, we load the csv data into a scipy list of list matrix, 
# then into a pandas dataframe as a sparse matrix

# do it for 1 item only 
source = 'TRAABJV128F1460C49,851082,1:6,2:5,3:10,4:4,5:6,6:2,7:6,8:6,9:1,11:2,12:1,16:2,17:4,19:3,20:1,21:4,22:1,24:1,25:5,26:3,27:1,28:2,31:1,34:1,39:1,40:2,41:2,46:2,50:1,51:1,55:2,56:1,61:1,62:2,63:2,64:1,66:3,67:1,73:5,81:1,82:1,87:1,89:1,95:5,96:2,99:2,100:2,101:2,108:2,118:1,120:2,125:2,127:1,129:4,130:1,135:2,138:3,170:1,171:1,196:1,204:3,210:1,217:1,237:1,257:2,258:1,289:1,318:1,337:1,344:1,360:1,371:1,379:13,431:1,434:3,469:1,574:1,593:2,633:1,670:3,677:1,701:1,745:1,1086:1,1365:1,1535:1'

values = source.split(',')
for word_count in values[2:]:
    row, column = map(int, word_count.split(':'))
    matrix.data[row].append(column)

# csvreader = csv.reader(open(csv_path))
# for line in csvreader:
#     row, column = map(str, line)
#     matrix.data[row].append(column)

print(matrix.data)
# genres.columns = csv_column_names
# json_list = genres.apply(matrix_row_to_json, 'columns')

# # -------------- DUMP JSONS INTRO ELASTICSEARCH ----------------
# if clean_genres_index:
#     es.indices.delete(index=es_genres_index, ignore=[400, 404])

# result_list = [es.index(index=es_genres_index, body=json_item) for json_item in json_list]

