# train_time

[![Downloads](https://static.pepy.tech/badge/train-time)](https://pepy.tech/project/train-time)  [![Downloads](https://static.pepy.tech/badge/train-time/month)](https://pepy.tech/project/train-time)  [![Downloads](https://static.pepy.tech/badge/train-time/week)](https://pepy.tech/project/train-time)


`train_time` is a Python package that provides a callback for machine learning training processes, particularly useful when using TensorFlow/Keras. It estimates and displays the remaining training time for each epoch during the model training process. The package allows users to view the remaining time in their preferred format: seconds, minutes, hours, or days.

## Features

- Easy integration with TensorFlow/Keras training loops.
- Customizable time format for estimated training time display.
- Lightweight and easy to use.

## Installation

Note: this doesnt work with python 3.12 for now

You can install `train_time` directly from PyPI:

```bash
pip install train_time
```

## Usage

To use `train_time` in your machine learning project, simply import the package and add it to your model's callbacks. Here is a basic example:

```python
import tensorflow as tf
from train_time import train_time

# Define your model
model = tf.keras.models.Sequential([
    # ... your model layers ...
])

# Compile your model
model.compile(optimizer='adam', loss='loss_function')

# Instantiate the callback
time_callback = train_time(time_format='minutes')

# Train the model with the callback
model.fit(x_train, y_train, epochs=10, callbacks=[time_callback])
```

In this example, `time_format` can be 'seconds', 'minutes', 'hours', or 'days', depending on your preference.

## Contributing

Contributions to `train_time` are welcome! 

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Akinyemi Arabambi** - [GitHub](https://github.com/2abet) <!-- Add actual GitHub links -->
- **Oluwanubkunmi Aluko** - [GitHub](https://github.com/bukunmialuko) <!-- Add actual GitHub links -->

## 🙏 Acknowledgments

- Thanks to all contributors who have helped improve this package
- Special thanks to the TensorFlow and Keras communities for their excellent documentation and resources
- Inspired by the need for better training time visibility in long-running ML experiments

## 📮 Support

- **Issues**: [GitHub Issues](https://github.com/2abet/TrainTime/issues)
- ⭐ : Star this repository if you find it helpful!
