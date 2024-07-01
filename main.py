import json
from datetime import datetime
from typing import List

from alpaca_trade_api import REST
from alpaca_trade_api.common import URL
from alpaca.common import Sort
from kafka import KafkaProducer

from alpaca_config.keys import config


def get_producer(brokers: List[str]):
    producer = KafkaProducer(
        bootstrap_servers=brokers,
        key_serializer=str.encode,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer
def produce_historical_news(
        redpanda_client: KafkaProducer,
        start_date: str,
        end_date: str,
        symbols: List[str],
        topic: str
    ):
    key_id = config['key_id']
    secret_key = config['secret_key']
    base_url = config['base_url']

    api = REST( key_id=key_id, secret_key=secret_key, base_url=URL(base_url))

    for symbol in symbols:
        news = api.get_news(
            symbol=symbol,
            start=start_date,
            end=end_date,
            limit=5,
            sort= Sort.ASC,
            include_content= False,
        )

        for i, row in enumerate(news):
            article = row._raw
            should_proceed = any(term in article['headline'] for term in symbols)
            if not should_proceed:
                continue

            timestamp_ms = int(row.created_at.timestap() * 1000)
            timestamp = datetime.fromtimestamp(row.created_at.timestamp())

            article['timestamp'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            article['timestamp_ms'] = timestamp_ms
            article['data_provider'] = 'alpaca'
            article['sentiment'] = get_senitment(article['headline'])

if __name__ == '__main__':
    produce_historical_news(
        get_producer(config['redpanda_brokers']),
        topic= 'market-news',
        start_date='2024-01-01',
        end_date='2024-06-28',
        symbols=['AAPL' , 'Apple'],
    )