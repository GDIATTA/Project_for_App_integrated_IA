import uuid
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from kafka import KafkaProducer, KafkaConsumer
from datetime import datetime
import random
import json
import time
from kafka import KafkaConsumer
from airflow.providers.amazon.aws.hooks.s3 import S3Hook# from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import logging

default_args = {
    'owner': 'gauss',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def fake_generate():
    return {
        "name":random.choice(['t-shirt','pantalon', 'chaussures','robe', 'jupe', 'chemise', 'short']),
        "price":"(random.uniform(1,1000))",
        "category":random.choice(['vetement hiver', 'vetement été', 'vetement automne', 'vetement printent']),
        "instock":random.choice(["true","false"]),
        "tags":random.choice(['version1','version2','version3']),
        "Descriiption":random.choice(['good for summer time','bon en hiver' 'stylé', 'confortable']),
        "Filename":random.choice(['product1.png', 'product2.png', 'product3.jpg', 'product4.jpeg', 'product5.gif'])
    }


def stream_data_from_Api_into_Kafka():

    producer = KafkaProducer(bootstrap_servers=['kafka1:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: #1 minute
            break
        try:
            res = fake_generate()

            producer.send('shopify.items1', json.dumps(res).encode('utf-8'))
            #wait for 5 seconds before sending the next transaction
            time.sleep(2)

        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

def stream_data_from_Kafka_into_S3_1(bucketname, sourcekey, destinationkey):
    s3_hook = S3Hook(aws_conn_id='aws_conn')

#Read data from Kafka3 
    consumer = KafkaConsumer('shopify.items1',
                           bootstrap_servers='kafka1:29092',
                           auto_offset_reset='earliest',
                           enable_auto_commit=False,
                           group_id='console-consumer-36523',
                           value_deserializer=lambda x: x.decode('utf-8')
                          )

# Apply custom Transformation and then Load S3 file
    curr_time = datetime.now()

    while (datetime.now() - curr_time).seconds < 60:
        try:
            for message in consumer:
                comment = message.value.decode('utf-8')
                s3_hook.load_string(comment, bucket_name=bucketname, Key=f'shopify.items1/{message.offset}.csv')
        except KeyboardInterrupt:
            print("Stopping consumer...")
    consumer.close()


def stream_data_from_Kafka_into_S3_2(bucketname, sourcekey, destinationkey):
    s3_hook = S3Hook(aws_conn_id='aws_conn')

#Read data from Kafka3 
    consumer = KafkaConsumer('shopify.items',
                           bootstrap_servers='kafka3:29094'
                           auto_offset_reset='earliest',
                           enable_auto_commit=False,
                           group_id='console-consumer-36523',
                           value_deserializer=lambda x: x.decode('utf-8')
                           )

# Apply custom Transformation and then Load S3 file
    curr_time = datetime.now()

    while (datetime.now() - curr_time).seconds < 60:
        try:
            for message in consumer:
                comment = message.value.decode('utf-8')
                s3_hook.load_string(comment, bucket_name=bucketname, Key=f'shopify.items1/{message.offset}.csv')
        except KeyboardInterrupt:
            print("Stopping consumer...")
    consumer.close()



with DAG(
         default_args=default_args,
         dag_id='shopify_user',
         description='Our first dag using python operator',
         start_date=datetime(2024,  6, 18),
         schedule_interval='@daily') as dag:

    streaming_task = PythonOperator(
        task_id='streaming_task',
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
