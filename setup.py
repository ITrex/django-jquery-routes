#!/bin/env python
# -*- coding: utf-8 -*-

'''Django package for jquery-routes:
Routing in javascript using hashchange event.
'''

from setuptools import setup

setup(
    name='django-jquery-routes',
    version='2.0',
    url='https://github.com/thorsteinsson/jquery-routes',
    description=globals()['__doc__'],
    author='Ægir Þorsteinsson',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT License',
    keywords=['django', 'jquery', 'jquery-routes'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_jquery_routes'],
    zip_safe=False,
    package_data={
        'django_jquery_routes':
        ['static/django_jquery_routes/js/*',]
    }
)
