"""
Flask-DaisySMS
==============

A Flask Extension to bridge between `Flask <https://github.com/pallets/flask>`_
and sending receiving sms codes with `DaisySMS <https://daisysms.com/>`_

Installation
````````````

.. code:: bash

    $ pip install flask-sendgrid


Usage
`````

.. code:: python

        from flask import Flask
        from flask_daisy import DaisySMS

        app = Flask(__name__)
        app.config['DAISYSMS_API_KEY'] = 'your api key'
        daisy_sms = DaisySMS(app)
        balance = daisy_sms.get_balance()
        number = daisy_sms.get_number()

"""

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        rv = f.read().splitlines()
    return rv


def get_version():
    with open('flask_daisy.py', 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")


_version = get_version()


setup(
    name='Flask-SendGrid',
    version=_version,
    url='https://github.com/carrasquel/flask-daisy-sms',
    license='MIT',
    author='Nelson Carrasquel',
    author_email='carrasquel@outlook.com',
    description='Adds DaisySMS support to Flask applications',
    long_description=open('README.md').read(),
    keywords=['Flask', 'DaisySMS', 'SMS'],
    py_modules=['flask_daisy'],
    zip_safe=False,
    platforms='any',
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules']
)
