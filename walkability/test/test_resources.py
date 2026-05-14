# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'a@a.a'
__date__ = '2026-04-14'
__copyright__ = 'Copyright 2026, Student'

import unittest

from qgis.PyQt.QtGui import QIcon



class Urban_researchDialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/Urban_research/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(Urban_researchResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



