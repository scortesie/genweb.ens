# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.1'

README = open("README.rst").read()
HISTORY = open(os.path.join("docs", "HISTORY.rst")).read()

setup(name='genweb.ens',
      version=version,
      description="Gestor d'ens i càrrecs",
      long_description=README + "\n" + HISTORY,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='ens càrrec',
      author='Santiago Cortés & Corina Riba',
      author_email='santiago.cortes.vaillo@upcnet.es',
      url='https://github.com/UPCnet/genweb.ens',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['genweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.dexteritytextindexer == 2.0.1',
      ],
      extras_require={'test': ['plone.app.testing',
                               'plone.app.testing[robot]>=4.2.2',
                               'plone.app.robotframework[debug]',]},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
