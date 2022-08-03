# -*- coding: utf-8 -*-

import pandas as pd
from kwnlp_sql_parser import WikipediaSqlDump

file_path = "enwiki-20210701-pagelinks.sql.gz" 
wsd = WikipediaSqlDump(
        file_path,
        keep_column_names=["pl_from", "pl_title"],
        allowlists={"pl_namespace": ["0"],
                    "pl_from_namespace": ["0"]})


file_path = "enwiki-20210701-categorylinks.sql.gz" 
wsd = WikipediaSqlDump(
        file_path,
        keep_column_names=["cl_from", "cl_to", "cl_type"])


file_path = "enwiki-20210701-page.sql.gz" 
wsd = WikipediaSqlDump(
        file_path,
        keep_column_names=['page_id', 'page_namespace', 'page_title','page_restrictions','page_is_redirect','page_is_new','page_touched','page_links_updated','page_latest','page_len','page_content_model'])

file_path = "enwiki-20210701-category.sql.gz" 
wsd = WikipediaSqlDump(
        file_path)

file_path = "enwiki-20210701-externallinks.sql.gz" 
wsd = WikipediaSqlDump(
        file_path)

file_path = "enwiki-20210701-page_props.sql.gz" 
wsd = WikipediaSqlDump(
        file_path,
        keep_column_names=["pp_page", "pp_propname", "pp_value"])


#wsd.to_csv(dialect='excel-tab')
#wsd.to_csv()