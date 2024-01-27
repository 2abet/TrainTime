import time
from tensorflow.keras.callbacks import Callback

class train_time(Callback):
    def __init__(self, time_format='seconds'):
        super().__init__()
        self.time_format = time_format

    def on_train_begin(self, logs=None):
        self.times = []
        self.total_time = 0.0

    def on_epoch_end(self, epoch, logs=None):
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

    def on_epoch_begin(self, epoch, logs=None):
        self.epoch_start_time = time.time()
