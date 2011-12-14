# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

version = '20111209.01'

setup(
    name='sc.templer.docs',
    version=version,
    description="Documentation templates for Simples Consultoria projects.",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='simples_consultoria web command-line skeleton documentation',
    author='Simples Consultoria',
    author_email='products@simplesconsultoria.com.br',
    url='http://www.simplesconsultoria.com.br/',
    namespace_packages=['sc', 'sc.templer'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "Sphinx",
        "sc.templer.core",
    ],
    entry_points="""
    [templer.templer_structure]
    sphinx_base = sc.templer.docs.structures:SphinxStructure

    [paste.paster_create_template]
    project_documentation = sc.templer.docs.template:ProjectDocumentation
    infra_documentation = sc.templer.docs.template:InfraDocumentation

    """,
    )
