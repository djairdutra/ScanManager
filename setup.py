from setuptools import setup
from codecs import open
from os import path
import glob

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="scan_manager",
    version="0.0.1",

    description="GUI app for collating images produced by a document scanner",

    long_description=long_description,

    url="https://github.com/timmartin/ScanManager",

    author="Tim Martin",
    author_email="tim@asymptotic.co.uk",

    license="MIT",

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: End Users/Desktop',
        'Topic :: Office/Business',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords="scanner",

    packages=['scan_manager'],

    install_requires=['PySide~=1.2.4',
                      'fpdf~=1.7.2'],

    data_files=[('images', glob.glob('images/*.svg'))],

    entry_points={
        'console_scripts': [
            'scan_manager=scan_manager:main'
        ]
    }
)
