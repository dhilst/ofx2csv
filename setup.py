from setuptools import setup

setup(name='ofx2csv',
      version='1.0',
      scripts=['ofx2csv.py'],
      description='Python Distribution Utilities',
      author='Daniel Hilst Selli',
      author_email='danielhilst@gmail.com',
      requires=['ofxparse'],
     )
