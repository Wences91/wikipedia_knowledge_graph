#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bz2
import pandas as pd
import csv
import os

# Step 1 (repeat with each daily dump)
file = 'pageviews/pageviews-20210526-user'

a = pd.read_csv((file+'.bz2'), compression='bz2', sep='\s+',
                names=["wiki_code", "title", "page_id", "type", "daily_total", "hourly_counts"], header=None,
                quoting=csv.QUOTE_NONE, converters={2: str})

b = a[a['wiki_code'] == 'en.wikipedia']
b = b[["title", "daily_total"]]


b = b.groupby(["title"]).sum().reset_index()
b.to_csv(('pageviews/dumps/'+file+'.tsv'), sep='\t', index=False, quoting=csv.QUOTE_NONE)


# Step 2 (after processing the daily files)
df = pd.DataFrame()

for dumpfile in os.listdir('pageviews/dumps/'):
    df_aux = pd.read_csv(('pageviews/dumps/' + dumpfile), sep='\t', quoting=csv.QUOTE_NONE)
    df = pd.concat([df, df_aux])
    df = df.groupby(["title"]).sum().reset_index()


df.to_csv(('pageviews/page_views.tsv'), sep='\t', index=False, quoting=csv.QUOTE_NONE)