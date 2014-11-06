from setuptools import setup, find_packages
import sys

name = 'scheduling'
description = 'Scheduling web application'
long_description = 'Allows for the generation and editing of a monthly schedule'
version = '0.0.0'
maintainer = ''
maintainer_email = ''
url = ''
packages = find_packages()
include_package_data = True
package_data = {'': ['static/*', 'views/*']}
install_requires = ['Flask', 'Flask-SQLAlchemy', 'Flask-Admin']
data_files = None
if getattr(sys, 'real_prefix', None) is None:
    data_files = [('/etc/scheduling', ['scheduling.wsgi'])]

if __name__ == '__main__':
    setup(name=name,
          description=description,
          long_description=long_description,
          version=version,
          maintainer=maintainer,
          maintainer_email=maintainer_email,
          url=url,
          packages=packages,
          include_package_data=include_package_data,
          package_data=package_data,
          install_requires=install_requires,
          data_files=data_files)
