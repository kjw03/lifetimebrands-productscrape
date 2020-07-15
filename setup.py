from setuptools import setup, find_namespace_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lifetimewebscrape',
    # Refer here for semantic versioning guidance: https://packaging.python.org/guides/distributing-packages-using-setuptools/#choosing-a-versioning-scheme
    version='0.1.0',
    description='Library intended to scrape lifetime brands product out of stock indicators from the walmart web site',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kjw03/lifetimebrands-productscrape',
    author='Kyle White',
    author_email='',
    license='',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: General Tools',
        'Programming Language :: Python :: 3',
    ],
    keywords='walmart lifetime scrape',
    packages=find_namespace_packages(where='src/python'),
    package_dir={"": "src/python"},
    extras_require={
    'test': ['pytest'],
    },
)
