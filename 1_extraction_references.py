# -*- coding: utf-8 -*-
import pandas as pd

citations = pd.read_parquet('dataset.parquet')
print('Total number of rows in the minimal dataset: {}'.format(citations.count()))


citations = citations[['id', 'type_of_citation', 'TitleType', 'Title', 'ID_list', 'URL', 'updated_identifier']]
citations.head()
citations.to_csv('references/ref_data.csv', index=False)