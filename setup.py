#
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2024-01-27 22:36
# * Last modified : 2024-01-27 22:36
# * Filename      : setup.py
# * Description   : 
# *********************************************************
import setuptools
import sys
import codecs

from distutils.core import setup

version_number = input("Input the new version number you are going to use: ")


# Get the long description
with codecs.open('README.rst' ,'r') as f:
    long_description = f.read()


#setuptools.setup(
setup(
    name="autoesp",
    version=version_number,
    author="Sen LEI",
    author_email="sen.lei@outlook.com",
    description="An useful CLT for auto-test espressif boards. ",
    long_description=long_description,
    url="https://github.com/Dual-Points/espressif-auto-test",
    packages=setuptools.find_packages(),
    include_package_data=False,
    install_requires=[
          'esptool',
          'adafruit-ampy', 
      ],
    license="BSD 3-clause",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    keywords='espressif, iot, serial, clt, boards, mcu, mpu, test',
)