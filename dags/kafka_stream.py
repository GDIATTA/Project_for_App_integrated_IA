import uuid
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
from kafka import KafkaProducer, KafkaConsumer
from airflow.providers.amazon.aws.hooks.s3 import S3Hook# from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import time
import logging

default_args = {
    'owner': 'gauss',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    #data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data_from_Api_into_Kafka():

    producer = KafkaProducer(bootstrap_servers=['kafka1:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: #1 minute
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

def stream_data_from_Kafka_into_S3_1(bucketname, sourcekey, destinationkey):

 s3_hook = S3Hook(aws_conn_id='aws_conn')

#Read data from Kafka3 
 consumer = KafkaConsumer('users.items', bootstrap_servers='kafka1:29092')

# Apply custom Transformation and then Load S3 file
 for message in consumer:
        comment = message.value.decode('utf-8')
        s3_hook.load_string(comment, bucket_name=bucketname, Key=f'shopify.items/{message.offset}.csv')


def stream_data_from_Kafka_into_S3_2(bucketname, sourcekey, destinationkey):

 s3_hook = S3Hook(aws_conn_id='aws_conn')

#Read data from Kafka3 
 consumer = KafkaConsumer('shopify.items', bootstrap_servers='kafka3:29094')

# Apply custom Transformation and then Load S3 file
 for message in consumer:
        comment = message.value.decode('utf-8')
        s3_hook.load_string(comment, bucket_name=bucketname, Key=f'shopify.items/{message.offset}.csv')


with DAG(
         default_args=default_args,
         dag_id='user_automation',
         description='Our first dag using python operator',
         start_date=datetime(2024,  6, 3),
         schedule_interval='@daily') as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data_from_Api_into_Kafka
    )

    streaming_task_1 = PythonOperator(
        task_id='stream_data_from_api_into_Kafka_S3',
        python_callable=stream_data_from_Kafka_into_S3_1
    )

    streaming_task_2 = PythonOperator(
        task_id='stream_data_from_Mongo_into_Kafka_S3',
        python_callable=stream_data_from_Kafka_into_S3_2
    )

    streaming_task >> streaming_task_1 >> streaming_task_2