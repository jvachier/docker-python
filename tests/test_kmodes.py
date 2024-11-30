import unittest

import numpy as np
from kmodes.kmodes import KModes


class TestKmodes(unittest.TestCase):
    def test_plot(self):
        data = np.array(
            [
                ["A", "B", "C"],
                ["B", "C", "A"],
                ["C", "A", "B"],
                ["A", "C", "B"],
                ["A", "A", "B"],
            ]
        )
        km = KModes(n_clusters=3, init="Huang", n_init=5, verbose=0)
        clusters = km.fit_predict(data)
        self.assertEqual(len(np.unique(clusters)), 3)
