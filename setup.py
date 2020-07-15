from setuptools import setup, find_namespace_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='service-commons',
    # Refer here for semantic versioning guidance: https://packaging.python.org/guides/distributing-packages-using-setuptools/#choosing-a-versioning-scheme
    version='0.1.0',
    description='Library intended to provide common classes and functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gecgithub01.walmart.com/SamsDSE/service-commons',
    author='Sam\'s Data Science',
    author_email='',
    license='',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: General Tools',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='walmart service commons databricks',
    packages=find_namespace_packages(where='src/python'),
    package_dir={"": "src/python"},
    extras_require={
    'test': ['pytest'],
    },
)
