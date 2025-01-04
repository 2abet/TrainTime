import pathlib

import setuptools

from setuptools import setup, find_packages

setup(
    name='train_time',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'keras',
    ],
    author='Akinyemi Arabambi',
    description='A Tensorflow Keras callback to estimate remaining training time',
    long_description= pathlib.Path('README.md').read_text(),
    long_description_content_type = 'text/markdown',
    url='https://github.com/2abet/TrainTime',
)
