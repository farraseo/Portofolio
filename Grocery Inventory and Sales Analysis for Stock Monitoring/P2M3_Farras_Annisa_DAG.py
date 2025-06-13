'''
=================================================
Milestone 3

Name  : Farras Annisa
Batch : HCK-027

This program is designed to automate stock monitoring for a grocery store. 
The dataset contains inventory data of items in the grocery store.
=================================================
'''

# import libraries
import pandas as pd
import datetime as dt
import time
from datetime import timedelta
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.decorators import task
from elasticsearch import Elasticsearch

default_args = {
    'owner': 'farraseo',
    'start_date': dt.datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=10),
}

with DAG(dag_id='P2M3_Farras_Annisa_DAGS',
         description='Milestone 3',
         default_args= default_args,
         schedule_interval="10,20,30 09 * * 6",
         catchup = False
         ) as dag:

    start = EmptyOperator(task_id='start')
    

    @task()
    def fetchFromSQL():
        '''

        This function is use for fetching data from SQL, and save the data to csv format
        
        '''
        # database, username, password, and host from docker sql
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        # postgres url
        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
        
        # create engine and connect it
        engine = create_engine(postgres_url)
        conn = engine.connect()

        # fetch daa from sql and save it to csv format
        df = pd.read_sql("select * from table_m3", conn)
        df.to_csv('/opt/airflow/data/P2M3_Farras_Annisa_data_raw.csv', index = False)

    @task()  
    def cleanData():
        # load data
        df = pd.read_csv('/opt/airflow/data/P2M3_Farras_Annisa_data_raw.csv')

        # lowercase column name
        df.columns = df.columns.str.lower()

        # add underscore to columns name
        df.columns = [
        'product_id', 'product_name', 'category', 'supplier_id', 
        'supplier_name', 'stock_quantity', 'reorder_level', 'reorder_quantity', 
        'unit_price', 'date_received', 'last_order_date', 'expiration_date', 
        'warehouse_location', 'sales_volume', 'inventory_turnover_rate', 'status'
        ]
     
        # drop duplicates
        df = df.drop_duplicates()

        # handle missing value
        df['category'] = df['category'].fillna('Fruits & Vegetables')

        # change values in column 
        df['unit_price'] = df['unit_price'].str.replace('$','')
        df['product_id'] = df['product_id'].str.replace('-','')
        
        # change data type for categorical value in number
        df['product_id'] = df['product_id'].astype(int)
        df['unit_price'] = df['unit_price'].astype(float)
        df['date_received'] = df['date_received'].astype('datetime64[ns]')
        df['last_order_date'] = df['last_order_date'].astype('datetime64[ns]')
        df['expiration_date'] = df['expiration_date'].astype('datetime64[ns]')
        df.dropna(inplace=True)
        

        # save to csv
        df.to_csv('/opt/airflow/data/P2M3_Farras_Annisa_data_clean.csv', index = False)
    
    @task()
    def postElastic():

        '''

        This function is use for posting data to ElasticSearch
        
        '''


        # load data
        df = pd.read_csv('data/P2M3_Farras_Annisa_data_clean.csv')
        time.sleep(10)
        # define elastic search method
        es = Elasticsearch(['http://elasticsearch:9200'])
        print(es.ping())

        # iterating dataframe
        for index, row in df.iterrows():
            res = es.index(index="milestone_3", id=index+1, body=row.to_json())

 
        #return res
    
    end = EmptyOperator(task_id='end')
 

    # prorcess order
    start >> fetchFromSQL() >> cleanData() >> postElastic() >> end