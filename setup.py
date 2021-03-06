#!/usr/bin/env python
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from setuptools import setup
import re
import os
import ConfigParser


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = ConfigParser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version, _ = info.get('version', '0.0.1').split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

requires = ['python-dateutil', 'python-sql']
for dep in info.get('depends', []):
    if not re.match(r'(ir|res|webdav)(\W|$)', dep):
        requires.append('tryton_%s >= %s.%s, < %s.%s' %
                (dep, major_version, minor_version, major_version,
                    minor_version + 1))
requires.append('trytond >= %s.%s.dev0, < %s.%s.dev0' %
        (major_version, minor_version, major_version, minor_version + 1))

setup(name='tryton_account_invoice',
    version=info.get('version', '0.0.1'),
    description='Tryton module for invoicing',
    long_description=open('README').read(),
    author='Tryton',
    url='http://www.tryton.org/',
    download_url=("http://downloads.tryton.org/" +
        info.get('version', '0.0.1').rsplit('.', 1)[0] + '/'),
    package_dir={'trytond.modules.account_invoice': '.'},
    packages=[
        'trytond.modules.account_invoice',
        'trytond.modules.account_invoice.tests',
        ],
    package_data={
        'trytond.modules.account_invoice': (info.get('xml', [])
            + ['tryton.cfg', 'view/*.xml', 'locale/*.po', 'invoice.odt']),
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Bulgarian',
        'Natural Language :: Catalan',
        'Natural Language :: Czech',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: French',
        'Natural Language :: German',
        'Natural Language :: Russian',
        'Natural Language :: Slovenian',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial :: Accounting',
        ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    account_invoice = trytond.modules.account_invoice
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    )
