# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['limco']
install_requires = \
['fire>=0.4.0,<0.5.0',
 'ginza>=5.0.1,<6.0.0',
 'ja-ginza>=5.0.0,<6.0.0',
 'numpy>=1.21.2,<2.0.0',
 'pandas>=1.3.0,<2.0.0',
 'spacy>=3.1.2,<4.0.0']

entry_points = \
{'console_scripts': ['limco = limco:main']}

setup_kwargs = {
    'name': 'limco',
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
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
