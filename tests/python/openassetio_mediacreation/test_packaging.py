# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 The Foundry Visionmongers Ltd
"""
Test the package is generated as we expect
"""

# pylint: disable=no-self-use
# pylint: disable=invalid-name
# pylint: disable=unused-import,import-outside-toplevel
# pylint: disable=missing-class-docstring,missing-function-docstring

import os
import pytest


class Test_packaging:
    def test_traits_file_is_present(self):
        # Verify the package is installed
        import openassetio_mediacreation

        # Find traits file in the mediacreation install
        traits_file = os.path.join(
            os.path.dirname(openassetio_mediacreation.__file__), "traits.yml"
        )

        assert os.path.exists(traits_file)
