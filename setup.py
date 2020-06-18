#!/usr/bin/env python
# # coding: utf-8

from setuptools import setup
from xcov import __version__

setup(
    name='xcov',
    description='Juewuer/xcov',
    long_description='py3 version of gcovr&dcovr',
    version=__version__,
    author='Juewuer',
    author_email='lihechao@gmail.com',
    url='https://github.com/juewuer/xcov',
	platforms=["linux"],
    py_modules=['ddt2'],
    python_requires='>=3.5',
    packages=['xcov'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
		'Topic :: Software Development :: white box',
		'Topic :: Software Development :: code Coverage',
    ],
	install_requires=[
          'jinja2',
          'lxml',
    ],	
    package_data={
         'gcovr': ['templates/*.css', 'templates/*.html'],
    },
    entry_points={
        'console_scripts': [
            'gcovr=gcovr.__main__:main',
         ],
    },
)
