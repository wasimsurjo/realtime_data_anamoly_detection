# Efficient Data Stream Anomaly Detection

This project is designed to develop a Python script capable of detecting anomalies in a continuous data stream, simulating real-time sequences of floating-point numbers that could represent various metrics such as financial transactions or system metrics.

## Project Overview

The focus of this project is to identify unusual patterns, such as exceptionally high values or deviations from the norm, through the development of an efficient and robust anomaly detection system using Python.

### Features

- **Algorithm Selection**: Implements Double Exponential Moving Average (DEMA) for efficient anomaly detection.
- **Data Stream Simulation**: Simulates real-time data with trends, seasonality, and injected anomalies.
- **Real-time Anomaly Detection**: Flags anomalies dynamically as data is streamed.
- **Optimization**: Ensures the algorithm is optimized for speed and efficiency.
- **Visualization**: Provides a real-time visualization tool to display both the data stream and detected anomalies.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.x
- Pip (Python package installer)

### Installing

A step by step series of examples that tell you how to get a development env running:

1. Clone the repository:
git clone https://github.com/wasimsurjo/realtime_data_anamoly_detection.git


2. Install the required packages:
pip install -r requirements.txt


### Running

To run the project, navigate to the project directory and execute:

python3 main.py


## Configuration

Modify `config/config.json` to adjust the data stream and anomaly detection parameters:
```json
{
    "data_stream_size": 2000,
    "noise_level": 5.0,
    "seasonality": 50,
    "window_size": 100,
    "ema_alpha": 0.3,
    "lookback": 20,
    "threshold_factor": 2.0,
    "batch_size": 50
}

```

Each parameter's role is explained in the configuration section of the documentation.

Built With:
Python - The programming language used.
Matplotlib - The library used for generating visualizations.

Authors
Wasim Mahmud Surjo - Initial work - wasimsurjo
