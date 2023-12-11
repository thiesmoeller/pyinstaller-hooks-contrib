#-----------------------------------------------------------------------------
# Copyright (c) 2023, PyInstaller Development Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

import os
import pypylon

# the automatic creation of links due to https://github.com/pyinstaller/pyinstaller/pull/7619
# breaks runtime search for libs of pypylon.
# setting `PYLON_TL_PATH` allows to find the transport layer libraries
pylon_tl_path = os.path.dirname(pypylon.__file__)

if os.path.exists(pylon_tl_path):
    os.environ["PYLON_TL_PATH"] = pylon_tl_path

