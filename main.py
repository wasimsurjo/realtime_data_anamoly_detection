# AUTHOR: WASIM MAHMUD SURJO
# Screenshots in the docs will not have docstrings
# Detailed explanations have been provided in almost all sections
# config.json is explained in the docs

from modules.AnamolyDetector import AnomalyDetection
from modules.DataPlotter import Plotter
from modules.DataStreamer import DataStream
import logging
import warnings
import matplotlib.pyplot as plt
import json


# Using 'Agg' backend for environments without GUI support
plt.switch_backend('Agg')
warnings.filterwarnings("ignore", message="known type.*")

# basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to load configuration, initialize components, and run the data stream simulation and anomaly detection.
    
    I use a configuration file(config.json) to make it easier to adjust parameters without changing the code. This approach 
    allows for flexibility and easier experimentation with different settings.
    """

    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        logging.error("Configuration file not found. Please provide a valid 'config.json' file.")
        return
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the configuration file. Please check the file format.")
        return
    
    try:
        stream = DataStream(config['data_stream_size'], config['noise_level'], config['seasonality'])
        detector = AnomalyDetection(config['window_size'], config['ema_alpha'], config['lookback'], config['threshold_factor'])
    except KeyError as e:
        logging.error(f"Configuration is missing a required key: {e}")
        return
    except ValueError as e:
        logging.error(f"Invalid configuration parameter: {e}")
        return

    plotter = Plotter()

    # Run the data stream simulation and anomaly detection
    while True:
        time_flow, value = stream.next_point()
        if time_flow is None:
            break

        anomaly = detector.is_anomaly(value[0], time_flow[0])
        plotter.update_plots(time_flow, value, anomaly)

    plotter.close_plot()

if __name__ == "__main__":
    main()

