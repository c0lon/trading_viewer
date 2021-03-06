import os
from setuptools import (
        find_packages,
        setup,
        )


here = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read().strip()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read().strip()
with open(os.path.join(here, 'VERSION')) as f:
    VERSION = f.read().strip()

dependency_links = [
    ]
install_requires = [
    'aiohttp<1.1.0', # required by discord
    'discord',
    'bs4',
    'psycopg2',
    'pyyaml',
    'sqlalchemy',
    ]
test_requires = [
    'pytest',
    ]

data_files = [
    ('', ['README.md', 'CHANGES.md', 'VERSION']),
    ]
entry_points = {
    'console_scripts': [
        'initializedb = scripts.initialize_database:main',
        'watch-posts = scripts.watch_for_posts:main',
        'add-accounts = scripts.add_accounts:main',
    ]
}

setup(name='tradingviewer',
      description='Watch TradingView accounts',
      long_description=README + '\n\n' + CHANGES,
      version=VERSION,
      author='c0lon',
      author_email='',
      dependency_links=dependency_links,
      install_requires=install_requires,
      test_requires=test_requires,
      packages=find_packages(),
      data_files=data_files,
      include_package_data=True,
      entry_points=entry_points
      )
