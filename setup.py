#!/usr/bin/env python3

import io
import os
from setuptools import setup, find_packages


def read(filename):
    with io.open(
            os.path.join(os.path.dirname(__file__), filename),
            encoding='utf-8') as f:
        return f.read()


setup(
    name='feincms3-downloads',
    version=__import__('feincms3_downloads').__version__,
    description='Downloads plugin for feincms3',
    long_description=read('README.rst'),
    author='Matthias Kestenholz',
    author_email='mk@feinheit.ch',
    url='https://github.com/matthiask/feincms3-downloads/',
    license='MIT License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    zip_safe=False,
)
