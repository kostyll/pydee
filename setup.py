#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2009 Pierre Raybaut
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
formlayout
==========

Module creating PyQt4 form dialogs/layouts to edit various type of parameters

Copyright © 2009 Pierre Raybaut
This software is licensed under the terms of the GNU General Public
License version 2 as published by the Free Software Foundation.
"""

import formlayout as module
import os.path as osp
name = osp.split(osp.dirname(module.__file__))[-1]
version = module.__version__
py_modules = ['formlayout']
package_data = {}
description = 'Module creating PyQt4 form dialogs/widgets to edit various type of parameters'
keywords = 'PyQt4 GUI'
classifiers = ['Development Status :: 5 - Production/Stable',
               ]

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
      name = name,
      version = version,
      description = description,
      download_url = 'http://%s.googlecode.com/files/%s-%s-py2.5.egg' % (name, name, version),
      author = "Pierre Raybaut",
      author_email = 'contact@pythonxy.com',
      url = 'http://code.google.com/p/%s/' % name,
      license = 'GPLv3',
      keywords = keywords,
      platforms = ['any'],
      py_modules = py_modules,
      package_data = package_data,
      classifiers = classifiers + [
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.5',
        ],
    )
