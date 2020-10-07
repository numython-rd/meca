from setuptools import setup
import os

dir_setup = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_setup, 'meca', 'version.py')) as f:
    # Defines __version__
    exec(f.read())

setup(name='meca',
      version=__version__,
      description='Python library for mechanical engineering design',
      author='Pedro Jorge De Los Santos',
      author_email='delossantosmfq@gmail.com',
      license = "MIT",
      keywords=["Mechanics","Machine","Mechanical Design"],
      url='https://github.com/numython-rd/meca',
      packages=['meca',],
      install_requires=['numpy','matplotlib'],
      classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: Implementation :: CPython",
      ]
      )
