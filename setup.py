from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.rst').read()
)

setup(name='fabtools.recipes.jenkins',
      version=version,
      description="Fabric task to install jenkins",
      long_description=long_description,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Topic :: System :: Systems Administration",
        ],
      keywords='',
      author='Alexandru Plugaru',
      author_email='alexandru.plugaru@gmail.com',
      url='http://github.com/humanfromearth/fabtools.recipes.jenkins',
      license='BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['fabtools', 'fabtools.recipes'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'fabtools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
