# Real-Time Algorithmic Trading System

## Overview

This repository contains code and resources for building a real-time algorithmic trading system using Apache Flink, Apache Kafka (with Redpanda), Python, SQL, and Docker. The project covers data ingestion, processing, and executing trades based on custom algorithms in real-time.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Integration with Alpaca API](#integration-with-alpaca-api)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

## Introduction

Algorithmic trading has revolutionized financial markets by leveraging technology to automate trading strategies, reduce latency, and increase efficiency. This project explores the implementation of a real-time algorithmic trading system using Apache Flink for stream processing, Apache Kafka for data ingestion and messaging, and Docker for containerization.

## Features

- **Real-Time Data Processing**: Utilize Apache Flink to process and analyze streaming stock price data.
- **Integration with Apache Kafka**: Efficiently ingest and stream data using Apache Kafka (and Redpanda).
- **Custom Trading Algorithms**: Implement and execute buy/sell orders based on custom algorithms.
- **Sentiment Analysis**: Perform sentiment analysis on historical news data to influence trading decisions.
- **End-to-End Workflow**: Covering data ingestion, processing, and real-time order execution.

## Technologies Used

- **Apache Flink**: Stream processing framework for real-time analytics and data processing.
- **Apache Kafka (with Redpanda)**: Distributed event streaming platform for handling real-time data feeds.
- **Python**: Programming language for scripting algorithms and integrating with APIs.
- **SQL**: Query language for data manipulation and analysis.
- **Docker**: Containerization platform for deploying and managing applications.

## Integration with Alpaca API

![Alpaca](https://miro.medium.com/v2/resize:fit:2000/1*hDQWsctiI00uCcp8Lc57NQ.png)

The project leverages the Alpaca Trading API for fetching stock price data and news articles. Alpaca provides a seamless interface to access market data, execute trades, and manage portfolios programmatically. 

API credentials (key_id and secret_key) have been included in the configuration (alpaca_config/keys.py) for demonstration purposes. These details are kept public since the project focuses solely on paper trading, simulating market conditions without actual financial risk.

## Project Structure

```
Real-Time-Algo-Trading/
│
├── historical-news-producer.py      # Script to fetch and publish historical news data to Kafka
├── price-producer.py                # Script to fetch and publish historical price data to Kafka
├── main.py                          # Main script for integrating and executing trading algorithms
├── utils.py                         # Utility functions, e.g., sentiment analysis
├── Dockerfile                       # Dockerfile for building the project environment
├── requirements.txt                 # Python dependencies for the project
└── README.md                        # Project documentation and setup guide
```

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/1Aditya7/Real-Time-Algo-Trading.git
   cd Real-Time-Algo-Trading
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Apache Flink and Kafka:**
   - Install Apache Flink and Apache Kafka according to their respective documentation.
   - Configure Kafka topics (`market-news`, `stock-prices`) as per your requirements.

4. **Run the Project:**
   - Start Apache Flink and Kafka services.
   - Execute the Python scripts (`historical-news-producer.py`, `price-producer.py`, `main.py`) to initiate data ingestion and processing.

## Usage

- **Running Scripts:**
  - Execute `historical-news-producer.py` to fetch and publish historical news data.
  - Run `price-producer.py` to fetch and publish historical price data.
  - Integrate and execute trading algorithms in `main.py` for real-time trading decisions.

- **Customization:**
  - Modify algorithms, adjust Kafka topics, or enhance data processing logic based on specific trading strategies.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
