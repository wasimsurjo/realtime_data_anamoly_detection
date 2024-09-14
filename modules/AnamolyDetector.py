from collections import deque
import logging
import numpy as np

class AnomalyDetection:
    """
    Detects anomalies using Double Exponential Moving Average (DEMA) based on dynamically adjusting thresholds.

    I chose DEMA for anomaly detection because it provides a good balance between capturing trends and smoothing
    seasonal patterns, making it more adaptive to concept drift than simpler methods like moving averages. 
    The dynamically adjusting threshold helps us respond to varying volatility in the data.

    Attributes:
        length (int): Length of the window for the moving averages.
        alpha (float): Smoothing factor for exponential calculations.
        history (int): Number of recent data points to consider for dynamic threshold calculation.
        factor (float): Multiplier for the dynamic threshold, adjusting sensitivity.
    """
    def __init__(self, length: int, alpha: float, history: int, factor: float):
        if length <= 0 or alpha <= 0 or alpha > 1 or history <= 0 or factor <= 0:
            raise ValueError("All parameters must be positive, and alpha should be between 0 and 1!")
        self.length = length
        self.alpha = alpha
        self.history = history
        self.factor = factor
        self.ema = None
        self.dema = None
        self.past_data = deque(maxlen=history)

    def get_dema(self, point: float) -> float:
        """
        Computes Double Exponential Moving Average of the data points.
        
        I start with a basic Exponential Moving Average (EMA) and then apply another level of smoothing to 
        get the DEMA. This approach helps us reduce lag and get a more responsive indicator for anomaly detection.

        Args:
            point (float): The latest data point.
        
        Returns:
            float: The current DEMA value, tracking the trend and seasonal adjustments.
        """
        if self.ema is None:
            self.ema = point
        else:
            self.ema = self.alpha * point + (1 - self.alpha) * self.ema
        
        if self.dema is None:
            self.dema = self.ema
        else:
            self.dema = self.alpha * self.ema + (1 - self.alpha) * self.dema
        
        return self.dema

    def is_anomaly(self, point: float, time_flow: float) -> bool:
        """
        Checks if the latest data point is an anomaly by comparing it against the computed DEMA and a dynamic threshold.
        
        I determine anomalies by calculating how far a point deviates from the DEMA. If it exceeds a dynamic threshold
        based on recent volatility (standard deviation), I flag it as an anomaly.

        Args:
            point (float): The current data point.
            time_flow (float): The timestamp or index for the data point.
        
        Returns:
            bool: True if an anomaly is detected, otherwise False.
        """
        dema = self.get_dema(point)
        self.past_data.append(point)
        
        # Dynamically adjust threshold based on historical data
        if len(self.past_data) == self.history:
            threshold = self.factor * np.std(self.past_data)
        else:
            threshold = 10.0  # Default threshold for early data points
        
        if abs(point - dema) > threshold:
            logging.info(f"Anomaly detected: {point} at time {time_flow} deviates significantly from expected DEMA {dema}.")
            return True
        return False