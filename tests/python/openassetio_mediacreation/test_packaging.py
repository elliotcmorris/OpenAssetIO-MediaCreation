# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 The Foundry Visionmongers Ltd
"""
Test the package is generated as we expect
"""

# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=unused-import,import-outside-toplevel
# pylint: disable=missing-class-docstring,missing-function-docstring

import site
from pathlib import Path
import pytest


class Test_packaging:
    def test_traits_file_is_present(self):
        # Verify the package is installed
        import openassetio_mediacreation

        # Find the site-packages directory for the current interpreter
        site_packages_dir = site.getsitepackages()[0]

        # Build path to the openassetio-mediacreation package directory
        package_dir = Path(site_packages_dir) / "openassetio_mediacreation"

        # Check if the traits.yml file exists in the package directory
        traits_file = package_dir / "traits.yml"
        assert traits_file.exists()
