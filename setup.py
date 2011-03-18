#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  18-Mar-2011.
#
from setuptools import setup, find_packages

version = "0.1rc2"

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()
setup(
        name="django-markitup-widget",
        version=version,
        description = "django-markitup-widget is Django's textarea like widget for using markItUp! on textarea",
        long_description=read('README.mkd'),
        classifiers = [
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
        ],
        keywords = "django widget textarea markItUp!",
        author = "Alisue",
        author_email = "alisue@hashnote.net",
        url=r"https://github.com/alisue/django-markitup-widget",
        download_url = r"https://github.com/alisue/django-markitup-widget/tarball/master",
        license = 'BSD',
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        install_requires=['setuptools'],
)
