#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mwxml
import glob
import pandas as pd
import csv
from datetime import date

def process_dump(dump, path):
  for page in dump:
      for revision in page:
          try:
              yield page.id, revision.timestamp, revision.user.text
          except:
              print(page.id)
              yield page.id, revision.timestamp, None


# Step 1 (repeat with each dump)
paths = glob.glob('edits/enwiki-20210701-stub-meta-history27.xml.gz')

ids=[]
dates=[]
contributors=[]
for page_id, revision_timestamp, revision_contributor in mwxml.map(process_dump, paths):
    ids.append(page_id)
    dates.append(str(revision_timestamp)[0:10])
    contributors.append(revision_contributor)
    


pages = pd.DataFrame({'page_id':ids, 'timestamp':dates, 'contributor':contributors})
pages['timestamp'] = pd.to_datetime(pages['timestamp'])

pages2 = pages.groupby('page_id').agg(count=('page_id', 'count'), time=('timestamp', 'min'), contributor=('contributor','nunique')).reset_index()
pages2.to_csv(('edits/dumps/'+'enwiki-20210701-stub-meta-history27.csv'), sep=';', index=False, quoting=csv.QUOTE_NONE)



# Step 2 (after processing all dumps)
df = pd.DataFrame()

for dumpfile in os.listdir('edits/dumps/'):
    df_aux = pd.read_csv(('edits/dumps/' + dumpfile), sep=';', quoting=csv.QUOTE_NONE)
    df = pd.concat([df, df_aux])

df.shape
df.info()
len(set(df['page_id']))


df.to_csv('edits/page_edits.tsv', sep='\t', index=False, quoting=csv.QUOTE_NONE)