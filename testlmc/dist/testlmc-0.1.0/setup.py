# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['testlmc']
install_requires = \
['fire',
 'ginza>=5.0.1,<6.0.0',
 'numpy>=1.21.2,<2.0.0',
 'pandas>=1.3.2,<2.0.0',
 'spacy>=3.1.2,<4.0.0']

entry_points = \
{'console_scripts': ['testlmc = testlmc:main']}

setup_kwargs = {
    'name': 'testlmc',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Itaru Ota',
    'author_email': 'ota.itaru.og4@is.naist.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
