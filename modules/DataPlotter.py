import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    """
    Handles the plotting of data and anomalies in real-time.
    
    I wanted to visualize the data stream along with the detected anomalies in real-time. This helps us better
    understand how the detection algorithm is performing and where it might need adjustments.

    Methods:
        update_plots: Refresh the plot with new data in real-time.
        close_plot: Close the plot properly when done.
    """
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.ax.set_title('Data Stream with Anomalies')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Data Points')
        self.times = []
        self.values = []
        self.anomalies = []

        # Initialize plot lines
        self.line, = self.ax.plot([], [], label='Normal Data', color='blue')
        self.anomaly_scatter = self.ax.scatter([], [], color='red', label='Anomaly')

    def update_plots(self, time_flow:list, value:list, anomaly: bool) -> None:
        """
        Updates the plot with new data points and marks anomalies.

        Here, I refresh the plot with new data points each time I receive them and mark any anomalies in red.

        Args:
            time_flow (list): The timestamp for the data point.
            value (list): The data point's value.
            anomaly (bool): Flag indicating whether the point is an anomaly.
        """
        self.times.append(time_flow[0])
        self.values.append(value[0])

        # Update the data for the line plot
        self.line.set_data(self.times, self.values)

        if anomaly:
            self.anomalies.append((time_flow[0], value[0]))

        if self.anomalies:  # Update scatter plot for anomalies
            x, y = zip(*self.anomalies)
            self.anomaly_scatter.set_offsets(list(zip(x, y)))

        # Adjust the plot limits dynamically
        self.ax.set_xlim(left=max(0, time_flow[0] - 50), right=time_flow[0] + 10)
        self.ax.set_ylim(min(self.values) - 10, max(self.values) + 10)

        self.ax.legend()
        self.fig.canvas.draw()
        self.fig.savefig(f'anomaly_detection_plot.png') # this image will also update in real time in case there are issues with the canva.draw()

    def close_plot(self):
        """
        Closes the plot to release resources.

        I close the plot properly to ensure I don't leave any resources hanging and to avoid memory leaks.
        """
        plt.close(self.fig)
