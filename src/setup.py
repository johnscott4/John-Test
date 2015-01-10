"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import time

APP = 'gui.py'
NAME = 'Argentum Control'

BASEVERSION = '0.15.1'
BUILDTIME = time.strftime('%Y%m%d')

VERSION = BASEVERSION + '+' + BUILDTIME

DATA_FILES = []

OPTIONS = {
    "bdist_esky": {
        "freezer_module": "py2app",
        "freezer_options": {
            'includes': [
                'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'
            ],
            'excludes': [
                'PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL',
                'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest',
                'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.phonon'
            ],

            'argv_emulation': True,
            'emulate-shell-environment': True,
            'iconfile': 'Icon.icns',
            'plist': 'Info.plist'
        }
    }
}