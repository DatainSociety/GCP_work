import pandas as pd 
import numpy as np
import requests
import os
from scipy import stats
import time
from datetime import datetime
import pytz
from google.cloud import bigquery
from google.cloud import storage
import pyarrow
import alpaca_trade_api as tradeapi
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/stal/Documents/GCP/GCPProject470def85999d.json"

from google.cloud import bigquery as bq

#TODO
#Finish 

client = bq.Client()

query_job = client.query(
    """
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10"""
)

results = query_job.result() 


