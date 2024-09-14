import numpy as np

class DataStream:
    """
    Simulates a real-time data stream by adding trend, seasonality, noise, and anomalies.

    Here, I wanted to create a data stream that mimics real-world scenarios where data isn't just random but often has
    a trend (e.g., a gradual increase), seasonality (e.g., daily or Iekly patterns), and noise (random fluctuations).
    I am injecting anomalies randomly to simulate real-life unexpected events like outliers or spikes.

    Attributes:
        size (int): Total number of data points in the stream.
        noise (float): Noise level to simulate measurement errors or environmental variability.
        cycle (int): Length of the cycle in the data, used for simulating seasonality.
        index (int): Current index in the data stream, tracking how many data points have been generated.
    """
    def __init__(self, size: int, noise: float, cycle: int):
        if size <= 0 or noise < 0 or cycle <= 0:
            raise ValueError("Size, noise, and cycle must be valid integers!")
        self.size = size
        self.noise = noise
        self.cycle = cycle
        self.index = 0

    def next_point(self) -> tuple:
        """
        Generates the next data point in the stream with applied trend, seasonality, and potential anomalies.
        
        I generate each data point by combining a linear trend, a sine wave for seasonality, and some Gaussian noise.
        Occasionally, I introduce an anomaly to represent rare but significant deviations

        Returns:
            tuple: A tuple (time, value) if there are more data points to generate
        """
        if self.index < self.size:
            flow = np.arange(self.index, self.index + 1)
            trend = np.linspace(10, 100, self.size)[self.index]
            seasonal = 15 * np.sin(2 * np.pi * flow / self.cycle)
            noise = self.noise * np.random.randn(1)
            
            # Generate anomalies with a certain probability
            if np.random.rand() > 0.98:
                value = trend + seasonal + noise + 50  # significant spike
            elif np.random.rand() > 0.96:
                value = trend + seasonal + noise - 50  # significant drop
            else:
                value = trend + seasonal + noise  # usual behavior
                
            self.index += 1
            return flow, value
        else:
            return None, None