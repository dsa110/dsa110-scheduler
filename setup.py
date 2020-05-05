from setuptools import setup, find_packages

setup(name="scheduler",
      packages=find_packages(),
      version='0.0.1',
      scripts=['scripts/start_workers.py'])
