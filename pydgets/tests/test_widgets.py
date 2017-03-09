#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Copyright (C) since 2016 Jan Mach <honza.mach.ml@gmail.com>
# Use of this source is governed by the MIT license, see LICENSE file.
#-------------------------------------------------------------------------------

import unittest
from unittest.mock import Mock, MagicMock, call
from pprint import pformat, pprint

import os
import sys
import shutil

# Generate the path to custom 'lib' directory
#lib = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
#sys.path.insert(0, lib)

import pydgets.widgets

class TestWidgets(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_01_basic(self):
        """
        Perform the basic operativity tests.
        """
        self.assertTrue(True)
        self.assertEqual(0, 0)

if __name__ == "__main__":
    unittest.main()
