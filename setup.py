# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='simple-apps',
    version='0.1.0',
    long_description='Long description',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
