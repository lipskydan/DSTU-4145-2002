import os
import unittest

from ecc import EllipticCurve
from GF import GF
from signature import DigitalSignature


class TestDigitalSignature(unittest.TestCase):
    def test_sign(self):
        ec = EllipticCurve(GF())
        base_point = ec.base_point()
        ds = DigitalSignature(ec, base_point)
        d = ds.gen_private_key()
        Q = ds.gen_public_key(d)
        message = os.urandom(16)
        message, signature = ds.sign(message, d)
        self.assertTrue(ds.verify(message, signature, Q))


if __name__ == '__main__':
    unittest.main()
