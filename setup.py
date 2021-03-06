'''
Created on May 26, 2014

@author: bijay
'''
#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='SparrowSDK',
    #packages=find_packages(),
    description='This client library is designed to support the sparrow sms api and '
                'is the canonical way to implement sparrow authentication.',
    author='sparrow',
    maintainer='Bijay Pant',
    maintainer_email='bijay@janakitech.com',
    url='https://github.com/bant4u/SparrowSDK',
    license='Apache',
    packages=find_packages(),
    long_description=open("README.rst").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    install_requires=[
        'requests',
    ],
    version="1.0.0-alpha",


)
