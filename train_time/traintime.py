import time
from tensorflow.keras.callbacks import Callback

class train_time(Callback):
    """
    Keras Callback that tracks and estimates training time per epoch.

    Parameters:
        time_format (str): Unit of time to display for estimated remaining time.
                           Options are 'seconds', 'minutes', 'hours', or 'days'.
                           Default is 'seconds'.
    """
    
    def __init__(self, time_format='seconds'):
        """
        Initialize the callback with the preferred time format.

        Args:
            time_format (str): Format to report the estimated remaining time.
        """
        super().__init__()
        self.time_format = time_format

    def on_train_begin(self, logs=None):
        """
        Called at the beginning of training. Initializes time tracking variables.

        Args:
            logs (dict): Currently unused. Included for compatibility.
        """
        self.times = []
        self.total_time = 0.0

    def on_epoch_begin(self, epoch, logs=None):
        """
        Called at the beginning of each epoch. Starts the epoch timer.

        Args:
            epoch (int): Index of the epoch.
            logs (dict): Currently unused. Included for compatibility.
        """
        self.epoch_start_time = time.time()

    def on_epoch_end(self, epoch, logs=None):
        """
        Called at the end of each epoch. Records the time taken for the epoch
        and prints the estimated remaining time in the chosen format.

        Args:
            epoch (int): Index of the completed epoch.
            logs (dict): Dictionary of metrics from the training epoch.
        """
        epoch_time = time.time() - self.epoch_start_time
        self.times.append(epoch_time)
        self.total_time += epoch_time
        remaining_epochs = self.params['epochs'] - epoch - 1
        remaining_time = self.total_time / (epoch + 1) * remaining_epochs

        # Convert remaining time based on user preference
        if self.time_format == 'minutes':
            remaining_time /= 60
            time_unit = "minutes"
        elif self.time_format == 'hours':
            remaining_time /= 3600
            time_unit = "hours"
        elif self.time_format == 'days':
            remaining_time /= 86400
            time_unit = "days"
        else:
            time_unit = "seconds"

        print(f"\nEpoch: {epoch + 1}/{self.params['epochs']}. Estimated time remaining: {remaining_time:.2f} {time_unit}.")
