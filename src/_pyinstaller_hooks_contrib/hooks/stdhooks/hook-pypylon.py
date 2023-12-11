# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# pypylon encapsulates the Basler pylon C++ SDK inside.
# Some of the library loads are handled during runtime
# and are collected in this hook


import os

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_dynamic_libs

# collect all dynamic libs that are loaded during runtime
datas = collect_dynamic_libs('pypylon')
# collect further files used in e.g. pylon dataprocessing
datas += collect_data_files('pypylon')
