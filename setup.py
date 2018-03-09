# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='LED Project',
    version='0.1.0',
    description='Assessment 3 for comp30670',
    long_description=readme,
    author='Martin Casey',
    author_email='martin.casey@ucdconnect.ie',
    url='https://github.com/MartinC20xx/comp30670-assessment3',
    license=license,
    include_package_data=True,
    install_requires=[
        'Click',
        ],
    packages=find_packages(exclude=('tests', 'docs'))
   
    #entry_points={
     #   "console_scripts":[
      #      'led_tester = led_project.cli:main']
       # }

)

