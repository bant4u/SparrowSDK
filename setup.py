'''
Created on May 26, 2014

@author: bijay
'''
#!/usr/bin/env python
from setuptools import setup, find_packages
from sparrow.version import __version__

exec(open("sparrow/version.py").read())

setup(
    name='sparrow-sdk',
    packages=find_packages(),
    version=__version__,
    description='This client library is designed to support the sparrow sms api and '
                'is the canonical way to implement sparrow authentication.',
    author='sparrow',
    maintainer='Bijay Pant',
    maintainer_email='bijay@janakitech.com',
    url='https://github.com/',
    license='Apache',
    packages=["sparrow"],
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
)
