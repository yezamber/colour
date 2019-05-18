# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.models.rgb.transfer_functions.itur_bt_2100`
module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.models.rgb.transfer_functions import (
    oetf_PQ_BT2100, oetf_reverse_PQ_BT2100, eotf_PQ_BT2100,
    eotf_reverse_PQ_BT2100, ootf_PQ_BT2100, ootf_reverse_PQ_BT2100,
    oetf_HLG_BT2100, oetf_reverse_HLG_BT2100, eotf_HLG_BT2100,
    eotf_reverse_HLG_BT2100, ootf_HLG_BT2100, ootf_reverse_HLG_BT2100)
from colour.models.rgb.transfer_functions.itur_bt_2100 import (
    gamma_function_HLG_BT2100)
from colour.utilities import domain_range_scale, ignore_numpy_errors

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'TestOetf_PQ_BT2100', 'TestOetf_reverse_PQ_BT2100', 'TestEotf_PQ_BT2100',
    'TestEotf_reverse_PQ_BT2100', 'TestOotf_PQ_BT2100',
    'TestOotf_reverse_PQ_BT2100', 'TestGamma_function_HLG_BT2100',
    'TestOetf_HLG_BT2100', 'TestOetf_reverse_HLG_BT2100',
    'TestEotf_HLG_BT2100', 'TestEotf_reverse_HLG_BT2100',
    'TestOotf_HLG_BT2100', 'TestOotf_reverse_HLG_BT2100'
]


class TestOetf_PQ_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_PQ_BT2100` definition unit tests methods.
    """

    def test_oetf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_PQ_BT2100` definition.
        """

        self.assertAlmostEqual(
            oetf_PQ_BT2100(0.0), 0.000000730955903, places=7)

        self.assertAlmostEqual(
            oetf_PQ_BT2100(0.1), 0.724769816665726, places=7)

        self.assertAlmostEqual(
            oetf_PQ_BT2100(1.0), 0.999999934308041, places=7)

    def test_n_dimensional_oetf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_PQ_BT2100` definition n-dimensional arrays support.
        """

        E = 0.1
        E_p = oetf_PQ_BT2100(E)

        E = np.tile(E, 6)
        E_p = np.tile(E_p, 6)
        np.testing.assert_almost_equal(oetf_PQ_BT2100(E), E_p, decimal=7)

        E = np.reshape(E, (2, 3))
        E_p = np.reshape(E_p, (2, 3))
        np.testing.assert_almost_equal(oetf_PQ_BT2100(E), E_p, decimal=7)

        E = np.reshape(E, (2, 3, 1))
        E_p = np.reshape(E_p, (2, 3, 1))
        np.testing.assert_almost_equal(oetf_PQ_BT2100(E), E_p, decimal=7)

    def test_domain_range_scale_oetf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_PQ_BT2100` definition domain and range scale support.
        """

        E = 0.1
        E_p = oetf_PQ_BT2100(E)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    oetf_PQ_BT2100(E * factor), E_p * factor, decimal=7)

    @ignore_numpy_errors
    def test_nan_oetf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_PQ_BT2100` definition nan support.
        """

        oetf_PQ_BT2100(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestOetf_reverse_PQ_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_PQ_BT2100` definition unit tests methods.
    """

    def test_oetf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_PQ_BT2100` definition.
        """

        self.assertAlmostEqual(
            oetf_reverse_PQ_BT2100(0.000000730955903), 0.0, places=7)

        self.assertAlmostEqual(
            oetf_reverse_PQ_BT2100(0.724769816665726), 0.1, places=7)

        self.assertAlmostEqual(
            oetf_reverse_PQ_BT2100(0.999999934308041), 1.0, places=7)

    def test_n_dimensional_oetf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_PQ_BT2100` definition n-dimensional arrays support.
        """

        E_p = 0.724769816665726
        E = oetf_reverse_PQ_BT2100(E_p)

        E_p = np.tile(E_p, 6)
        E = np.tile(E, 6)
        np.testing.assert_almost_equal(
            oetf_reverse_PQ_BT2100(E_p), E, decimal=7)

        E_p = np.reshape(E_p, (2, 3))
        E = np.reshape(E, (2, 3))
        np.testing.assert_almost_equal(
            oetf_reverse_PQ_BT2100(E_p), E, decimal=7)

        E_p = np.reshape(E_p, (2, 3, 1))
        E = np.reshape(E, (2, 3, 1))
        np.testing.assert_almost_equal(
            oetf_reverse_PQ_BT2100(E_p), E, decimal=7)

    def test_domain_range_scale_oetf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_PQ_BT2100` definition domain and range scale support.
        """

        E_p = 0.724769816665726
        E = oetf_reverse_PQ_BT2100(E_p)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    oetf_reverse_PQ_BT2100(E_p * factor),
                    E * factor,
                    decimal=7)

    @ignore_numpy_errors
    def test_nan_oetf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_PQ_BT2100` definition nan support.
        """

        oetf_reverse_PQ_BT2100(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestEotf_PQ_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_PQ_BT2100` definition unit tests methods.
    """

    def test_eotf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_PQ_BT2100` definition.
        """

        self.assertAlmostEqual(eotf_PQ_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            eotf_PQ_BT2100(0.724769816665726), 779.98836083408537, places=7)

        self.assertAlmostEqual(eotf_PQ_BT2100(1.0), 10000.0, places=7)

    def test_n_dimensional_eotf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_PQ_BT2100` definition n-dimensional arrays support.
        """

        E_p = 0.724769816665726
        F_D = eotf_PQ_BT2100(E_p)

        E_p = np.tile(E_p, 6)
        F_D = np.tile(F_D, 6)
        np.testing.assert_almost_equal(eotf_PQ_BT2100(E_p), F_D, decimal=7)

        E_p = np.reshape(E_p, (2, 3))
        F_D = np.reshape(F_D, (2, 3))
        np.testing.assert_almost_equal(eotf_PQ_BT2100(E_p), F_D, decimal=7)

        E_p = np.reshape(E_p, (2, 3, 1))
        F_D = np.reshape(F_D, (2, 3, 1))
        np.testing.assert_almost_equal(eotf_PQ_BT2100(E_p), F_D, decimal=7)

    def test_domain_range_scale_eotf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_PQ_BT2100` definition domain and range scale support.
        """

        E_p = 0.724769816665726
        F_D = eotf_PQ_BT2100(E_p)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    eotf_PQ_BT2100(E_p * factor), F_D * factor, decimal=7)

    @ignore_numpy_errors
    def test_nan_eotf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_PQ_BT2100` definition nan support.
        """

        eotf_PQ_BT2100(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestEotf_reverse_PQ_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_PQ_BT2100` definition unit tests methods.
    """

    def test_eotf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_PQ_BT2100` definition.
        """

        self.assertAlmostEqual(
            eotf_reverse_PQ_BT2100(0.0), 0.000000730955903, places=7)

        self.assertAlmostEqual(
            eotf_reverse_PQ_BT2100(779.98836083408537),
            0.724769816665726,
            places=7)

        self.assertAlmostEqual(eotf_reverse_PQ_BT2100(10000.0), 1.0, places=7)

    def test_n_dimensional_eotf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_PQ_BT2100` definition n-dimensional arrays support.
        """

        F_D = 779.98836083408537
        E_p = eotf_reverse_PQ_BT2100(F_D)

        F_D = np.tile(F_D, 6)
        E_p = np.tile(E_p, 6)
        np.testing.assert_almost_equal(
            eotf_reverse_PQ_BT2100(F_D), E_p, decimal=7)

        F_D = np.reshape(F_D, (2, 3))
        E_p = np.reshape(E_p, (2, 3))
        np.testing.assert_almost_equal(
            eotf_reverse_PQ_BT2100(F_D), E_p, decimal=7)

        F_D = np.reshape(F_D, (2, 3, 1))
        E_p = np.reshape(E_p, (2, 3, 1))
        np.testing.assert_almost_equal(
            eotf_reverse_PQ_BT2100(F_D), E_p, decimal=7)

    def test_domain_range_scale_eotf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_PQ_BT2100` definition domain and range scale support.
        """

        F_D = 779.98836083408537
        E_p = eotf_reverse_PQ_BT2100(F_D)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    eotf_reverse_PQ_BT2100(F_D * factor),
                    E_p * factor,
                    decimal=7)

    @ignore_numpy_errors
    def test_nan_eotf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_PQ_BT2100` definition nan support.
        """

        eotf_reverse_PQ_BT2100(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestOotf_PQ_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_PQ_BT2100` definition unit tests methods.
    """

    def test_ootf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_PQ_BT2100` definition.
        """

        self.assertAlmostEqual(ootf_PQ_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            ootf_PQ_BT2100(0.1), 779.98836083411584, places=7)

        self.assertAlmostEqual(
            ootf_PQ_BT2100(1.0), 9999.993723673924300, places=7)

    def test_n_dimensional_ootf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_PQ_BT2100` definition n-dimensional arrays support.
        """

        E = 0.1
        F_D = ootf_PQ_BT2100(E)

        E = np.tile(E, 6)
        F_D = np.tile(F_D, 6)
        np.testing.assert_almost_equal(ootf_PQ_BT2100(E), F_D, decimal=7)

        E = np.reshape(E, (2, 3))
        F_D = np.reshape(F_D, (2, 3))
        np.testing.assert_almost_equal(ootf_PQ_BT2100(E), F_D, decimal=7)

        E = np.reshape(E, (2, 3, 1))
        F_D = np.reshape(F_D, (2, 3, 1))
        np.testing.assert_almost_equal(ootf_PQ_BT2100(E), F_D, decimal=7)

    def test_domain_range_scale_ootf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_PQ_BT2100` definition domain and range scale support.
        """

        E = 0.1
        F_D = ootf_PQ_BT2100(E)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    ootf_PQ_BT2100(E * factor), F_D * factor, decimal=7)

    @ignore_numpy_errors
    def test_nan_ootf_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_PQ_BT2100` definition nan support.
        """

        ootf_PQ_BT2100(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestOotf_reverse_PQ_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_PQ_BT2100` definition unit tests methods.
    """

    def test_ootf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_PQ_BT2100` definition.
        """

        self.assertAlmostEqual(ootf_reverse_PQ_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            ootf_reverse_PQ_BT2100(779.98836083411584), 0.1, places=7)

        self.assertAlmostEqual(
            ootf_reverse_PQ_BT2100(9999.993723673924300), 1.0, places=7)

    def test_n_dimensional_ootf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_PQ_BT2100` definition n-dimensional arrays support.
        """

        F_D = 779.98836083411584
        E = ootf_reverse_PQ_BT2100(F_D)

        F_D = np.tile(F_D, 6)
        E = np.tile(E, 6)
        np.testing.assert_almost_equal(
            ootf_reverse_PQ_BT2100(F_D), E, decimal=7)

        F_D = np.reshape(F_D, (2, 3))
        E = np.reshape(E, (2, 3))
        np.testing.assert_almost_equal(
            ootf_reverse_PQ_BT2100(F_D), E, decimal=7)

        F_D = np.reshape(F_D, (2, 3, 1))
        E = np.reshape(E, (2, 3, 1))
        np.testing.assert_almost_equal(
            ootf_reverse_PQ_BT2100(F_D), E, decimal=7)

    def test_domain_range_scale_ootf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_PQ_BT2100` definition domain and range scale support.
        """

        F_D = 779.98836083411584
        E = ootf_reverse_PQ_BT2100(F_D)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    ootf_reverse_PQ_BT2100(F_D * factor),
                    E * factor,
                    decimal=7)

    @ignore_numpy_errors
    def test_nan_ootf_reverse_PQ_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_PQ_BT2100` definition nan support.
        """

        ootf_reverse_PQ_BT2100(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestGamma_function_HLG_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
gamma_function_HLG_BT2100` definition unit tests methods.
    """

    def test_gamma_function_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
gamma_function_HLG_BT2100` definition.
        """

        self.assertAlmostEqual(
            gamma_function_HLG_BT2100(1000.0), 1.2, places=7)

        self.assertAlmostEqual(
            gamma_function_HLG_BT2100(2000.0), 1.326432598178872, places=7)

        self.assertAlmostEqual(
            gamma_function_HLG_BT2100(4000.0), 1.452865196357744, places=7)

        self.assertAlmostEqual(
            gamma_function_HLG_BT2100(10000.0), 1.619999999999999, places=7)


class TestOetf_HLG_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_HLG_BT2100` definition unit tests methods.
    """

    def test_oetf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_HLG_BT2100` definition.
        """

        self.assertAlmostEqual(oetf_HLG_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            oetf_HLG_BT2100(0.18 / 12), 0.212132034355964, places=7)

        self.assertAlmostEqual(
            oetf_HLG_BT2100(1.0), 0.999999995536569, places=7)

    def test_n_dimensional_oetf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_HLG_BT2100` definition n-dimensional arrays support.
        """

        E = 0.18 / 12
        E_p = oetf_HLG_BT2100(E)

        E = np.tile(E, 6)
        E_p = np.tile(E_p, 6)
        np.testing.assert_almost_equal(oetf_HLG_BT2100(E), E_p, decimal=7)

        E = np.reshape(E, (2, 3))
        E_p = np.reshape(E_p, (2, 3))
        np.testing.assert_almost_equal(oetf_HLG_BT2100(E), E_p, decimal=7)

        E = np.reshape(E, (2, 3, 1))
        E_p = np.reshape(E_p, (2, 3, 1))
        np.testing.assert_almost_equal(oetf_HLG_BT2100(E), E_p, decimal=7)

    def test_domain_range_scale_oetf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_HLG_BT2100` definition domain and range scale support.
        """

        E = 0.18 / 12
        E_p = oetf_HLG_BT2100(E)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    oetf_HLG_BT2100(E * factor), E_p * factor, decimal=7)

    @ignore_numpy_errors
    def test_nan_oetf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_HLG_BT2100` definition nan support.
        """

        oetf_HLG_BT2100(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestOetf_reverse_HLG_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_HLG_BT2100` definition unit tests methods.
    """

    def test_oetf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_HLG_BT2100` definition.
        """

        self.assertAlmostEqual(oetf_reverse_HLG_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            oetf_reverse_HLG_BT2100(0.212132034355964), 0.18 / 12, places=7)

        self.assertAlmostEqual(
            oetf_reverse_HLG_BT2100(0.999999995536569), 1.0, places=7)

    def test_n_dimensional_oetf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_HLG_BT2100` definition n-dimensional arrays support.
        """

        E_p = 0.212132034355964
        E = oetf_reverse_HLG_BT2100(E_p)

        E_p = np.tile(E_p, 6)
        E = np.tile(E, 6)
        np.testing.assert_almost_equal(
            oetf_reverse_HLG_BT2100(E_p), E, decimal=7)

        E_p = np.reshape(E_p, (2, 3))
        E = np.reshape(E, (2, 3))
        np.testing.assert_almost_equal(
            oetf_reverse_HLG_BT2100(E_p), E, decimal=7)

        E_p = np.reshape(E_p, (2, 3, 1))
        E = np.reshape(E, (2, 3, 1))
        np.testing.assert_almost_equal(
            oetf_reverse_HLG_BT2100(E_p), E, decimal=7)

    def test_domain_range_scale_oetf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_HLG_BT2100` definition domain and range scale support.
        """

        E_p = 0.212132034355964
        E = oetf_reverse_HLG_BT2100(E_p)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    oetf_reverse_HLG_BT2100(E_p * factor),
                    E * factor,
                    decimal=7)

    @ignore_numpy_errors
    def test_nan_oetf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
oetf_reverse_HLG_BT2100` definition nan support.
        """

        oetf_reverse_HLG_BT2100(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestEotf_HLG_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_HLG_BT2100` definition unit tests methods.
    """

    def test_eotf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_HLG_BT2100` definition.
        """

        self.assertAlmostEqual(eotf_HLG_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            eotf_HLG_BT2100(0.212132034355964), 6.476039825649814, places=7)

        self.assertAlmostEqual(
            eotf_HLG_BT2100(1.0), 1000.000029239784300, places=7)

        self.assertAlmostEqual(
            eotf_HLG_BT2100(0.212132034355964, 0.001, 10000, 1.4),
            27.96039175299561,
            places=7)

    def test_n_dimensional_eotf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_HLG_BT2100` definition n-dimensional arrays support.
        """

        E_p = 0.212132034355964
        F_D = eotf_HLG_BT2100(E_p)

        E_p = np.tile(E_p, 6)
        F_D = np.tile(F_D, 6)
        np.testing.assert_almost_equal(eotf_HLG_BT2100(E_p), F_D, decimal=7)

        E_p = np.reshape(E_p, (2, 3))
        F_D = np.reshape(F_D, (2, 3))
        np.testing.assert_almost_equal(eotf_HLG_BT2100(E_p), F_D, decimal=7)

        E_p = np.reshape(E_p, (2, 3, 1))
        F_D = np.reshape(F_D, (2, 3, 1))
        np.testing.assert_almost_equal(eotf_HLG_BT2100(E_p), F_D, decimal=7)

        E_p = np.reshape(E_p, (6, 1))
        F_D = np.reshape(F_D, (6, 1))
        np.testing.assert_almost_equal(eotf_HLG_BT2100(E_p), F_D, decimal=7)

        E_p = np.array([0.25, 0.50, 0.75])
        F_D = np.array([12.49759412, 49.99037650, 158.94693746])
        np.testing.assert_almost_equal(eotf_HLG_BT2100(E_p), F_D, decimal=7)

        E_p = np.tile(E_p, (6, 1))
        F_D = np.tile(F_D, (6, 1))
        np.testing.assert_almost_equal(eotf_HLG_BT2100(E_p), F_D, decimal=7)

        E_p = np.reshape(E_p, (2, 3, 3))
        F_D = np.reshape(F_D, (2, 3, 3))
        np.testing.assert_almost_equal(eotf_HLG_BT2100(E_p), F_D, decimal=7)

    def test_domain_range_scale_eotf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_HLG_BT2100` definition domain and range scale support.
        """

        E_p = 0.212132034355964
        F_D = eotf_HLG_BT2100(E_p)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    eotf_HLG_BT2100(E_p * factor), F_D * factor, decimal=7)

    @ignore_numpy_errors
    def test_nan_eotf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_HLG_BT2100` definition nan support.
        """

        eotf_HLG_BT2100(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestEotf_reverse_HLG_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_HLG_BT2100` definition unit tests methods.
    """

    def test_eotf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_HLG_BT2100` definition.
        """

        self.assertAlmostEqual(eotf_reverse_HLG_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            eotf_reverse_HLG_BT2100(6.476039825649814),
            0.212132034355964,
            places=7)

        self.assertAlmostEqual(
            eotf_reverse_HLG_BT2100(1000.000029239784300), 1.0, places=7)

        self.assertAlmostEqual(
            eotf_reverse_HLG_BT2100(6.476039825649814, 0.001, 10000, 1.4),
            0.125811012816761,
            places=7)

    def test_n_dimensional_eotf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_HLG_BT2100` definition n-dimensional arrays support.
        """

        F_D = 6.476039825649814
        E_p = eotf_reverse_HLG_BT2100(F_D)

        F_D = np.tile(F_D, 6)
        E_p = np.tile(E_p, 6)
        np.testing.assert_almost_equal(
            eotf_reverse_HLG_BT2100(F_D), E_p, decimal=7)

        F_D = np.reshape(F_D, (2, 3))
        E_p = np.reshape(E_p, (2, 3))
        np.testing.assert_almost_equal(
            eotf_reverse_HLG_BT2100(F_D), E_p, decimal=7)

        F_D = np.reshape(F_D, (2, 3, 1))
        E_p = np.reshape(E_p, (2, 3, 1))
        np.testing.assert_almost_equal(
            eotf_reverse_HLG_BT2100(F_D), E_p, decimal=7)

        F_D = np.reshape(F_D, (6, 1))
        E_p = np.reshape(E_p, (6, 1))
        np.testing.assert_almost_equal(
            eotf_reverse_HLG_BT2100(F_D), E_p, decimal=7)

        F_D = np.array([12.49759412, 49.99037650, 158.94693746])
        E_p = np.array([0.25, 0.50, 0.75])
        np.testing.assert_almost_equal(
            eotf_reverse_HLG_BT2100(F_D), E_p, decimal=7)

        F_D = np.tile(F_D, (6, 1))
        E_p = np.tile(E_p, (6, 1))
        np.testing.assert_almost_equal(
            eotf_reverse_HLG_BT2100(F_D), E_p, decimal=7)

        F_D = np.reshape(F_D, (2, 3, 3))
        E_p = np.reshape(E_p, (2, 3, 3))
        np.testing.assert_almost_equal(
            eotf_reverse_HLG_BT2100(F_D), E_p, decimal=7)

    def test_domain_range_scale_eotf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_HLG_BT2100` definition domain and range scale support.
        """

        F_D = 6.476039825649814
        E_p = eotf_reverse_HLG_BT2100(F_D)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    eotf_reverse_HLG_BT2100(F_D * factor),
                    E_p * factor,
                    decimal=7)

    @ignore_numpy_errors
    def test_nan_eotf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
eotf_reverse_HLG_BT2100` definition nan support.
        """

        eotf_reverse_HLG_BT2100(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestOotf_HLG_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_HLG_BT2100` definition unit tests methods.
    """

    def test_ootf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_HLG_BT2100` definition.
        """

        self.assertAlmostEqual(ootf_HLG_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            ootf_HLG_BT2100(0.1), 63.095734448019336, places=7)

        self.assertAlmostEqual(ootf_HLG_BT2100(1.0), 1000.0, places=7)

        self.assertAlmostEqual(
            ootf_HLG_BT2100(0.1, 0.001, 10000, 1.4),
            398.108130742780300,
            places=7)

        a = np.array(
            [[45.884942278760597, 0.000000000000000, -45.884942278760597],
             [-63.095734448019336, -63.095734448019336, -63.095734448019336],
             [63.095734448019336, 63.095734448019336, 63.095734448019336],
             [51.320396090100672, -51.320396090100672, 51.320396090100672]],
        )  # yapf: disable
        np.testing.assert_almost_equal(
            ootf_HLG_BT2100(
                np.array([[0.1, 0.0, -0.1], [-0.1, -0.1, -0.1],
                          [0.1, 0.1, 0.1], [0.1, -0.1, 0.1]])),
            a,
            decimal=7)

    def test_n_dimensional_ootf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_HLG_BT2100` definition n-dimensional arrays support.
        """

        E = 0.1
        F_D = ootf_HLG_BT2100(E)

        E = np.tile(E, 6)
        F_D = np.tile(F_D, 6)
        np.testing.assert_almost_equal(ootf_HLG_BT2100(E), F_D, decimal=7)

        E = np.reshape(E, (2, 3))
        F_D = np.reshape(F_D, (2, 3))
        np.testing.assert_almost_equal(ootf_HLG_BT2100(E), F_D, decimal=7)

        E = np.reshape(E, (2, 3, 1))
        F_D = np.reshape(F_D, (2, 3, 1))
        np.testing.assert_almost_equal(ootf_HLG_BT2100(E), F_D, decimal=7)

        E = np.reshape(E, (6, 1))
        F_D = np.reshape(F_D, (6, 1))
        np.testing.assert_almost_equal(ootf_HLG_BT2100(E), F_D, decimal=7)

        E = np.array([0.25, 0.50, 0.75])
        F_D = np.array([213.01897444, 426.03794887, 639.05692331])
        np.testing.assert_almost_equal(ootf_HLG_BT2100(E), F_D, decimal=7)

        E = np.tile(E, (6, 1))
        F_D = np.tile(F_D, (6, 1))
        np.testing.assert_almost_equal(ootf_HLG_BT2100(E), F_D, decimal=7)

        E = np.reshape(E, (2, 3, 3))
        F_D = np.reshape(F_D, (2, 3, 3))
        np.testing.assert_almost_equal(ootf_HLG_BT2100(E), F_D, decimal=7)

    def test_domain_range_scale_ootf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_HLG_BT2100` definition domain and range scale support.
        """

        E = 0.1
        F_D = ootf_HLG_BT2100(E)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    ootf_HLG_BT2100(E * factor), F_D * factor, decimal=7)

    @ignore_numpy_errors
    def test_nan_ootf_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_HLG_BT2100` definition nan support.
        """

        ootf_HLG_BT2100(np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


class TestOotf_reverse_HLG_BT2100(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_HLG_BT2100` definition unit tests methods.
    """

    def test_ootf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_HLG_BT2100` definition.
        """

        self.assertAlmostEqual(ootf_reverse_HLG_BT2100(0.0), 0.0, places=7)

        self.assertAlmostEqual(
            ootf_reverse_HLG_BT2100(63.095734448019336), 0.1, places=7)

        self.assertAlmostEqual(ootf_reverse_HLG_BT2100(1000.0), 1.0, places=7)

        self.assertAlmostEqual(
            ootf_reverse_HLG_BT2100(398.108130742780300, 0.001, 10000, 1.4),
            0.1,
            places=7)

        a = np.array(
            [[45.884942278760597, 0.000000000000000, -45.884942278760597],
             [-63.095734448019336, -63.095734448019336, -63.095734448019336],
             [63.095734448019336, 63.095734448019336, 63.095734448019336],
             [51.320396090100672, -51.320396090100672, 51.320396090100672]]
        )  # yapf: disable
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(a),
            np.array([[0.1, 0.0, -0.1], [-0.1, -0.1, -0.1], [0.1, 0.1, 0.1],
                      [0.1, -0.1, 0.1]]),
            decimal=7)

    def test_n_dimensional_ootf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_HLG_BT2100` definition n-dimensional arrays support.
        """

        F_D = 63.095734448019336
        E = ootf_reverse_HLG_BT2100(F_D)

        F_D = np.tile(F_D, 6)
        E = np.tile(E, 6)
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(F_D), E, decimal=7)

        F_D = np.reshape(F_D, (2, 3))
        E = np.reshape(E, (2, 3))
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(F_D), E, decimal=7)

        F_D = np.reshape(F_D, (2, 3, 1))
        E = np.reshape(E, (2, 3, 1))
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(F_D), E, decimal=7)

        F_D = np.reshape(F_D, (6, 1))
        E = np.reshape(E, (6, 1))
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(F_D), E, decimal=7)

        F_D = np.array([213.01897444, 426.03794887, 639.05692331])
        E = np.array([0.25, 0.50, 0.75])
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(F_D), E, decimal=7)

        F_D = np.tile(F_D, (6, 1))
        E = np.tile(E, (6, 1))
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(F_D), E, decimal=7)

        F_D = np.reshape(F_D, (2, 3, 3))
        E = np.reshape(E, (2, 3, 3))
        np.testing.assert_almost_equal(
            ootf_reverse_HLG_BT2100(F_D), E, decimal=7)

    def test_domain_range_scale_ootf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_HLG_BT2100` definition domain and range scale support.
        """

        F_D = 63.095734448019336
        E = ootf_reverse_HLG_BT2100(F_D)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    ootf_reverse_HLG_BT2100(F_D * factor),
                    E * factor,
                    decimal=7)

    @ignore_numpy_errors
    def test_nan_ootf_reverse_HLG_BT2100(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.itur_bt_2100.\
ootf_reverse_HLG_BT2100` definition nan support.
        """

        ootf_reverse_HLG_BT2100(
            np.array([-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]))


if __name__ == '__main__':
    unittest.main()
