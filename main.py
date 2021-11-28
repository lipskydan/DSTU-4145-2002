import os

from ecc import EllipticCurve
from GF import GF
from signature import DigitalSignature

if __name__ == '__main__':
    ec = EllipticCurve(GF())
    base_point = ec.base_point()
    ds = DigitalSignature(ec, base_point)

    d = ds.gen_private_key()
    print(f'private key = {d}')

    Q = ds.gen_public_key(d)
    print(f'public key = {Q}')

    message = os.urandom(16)
    print(f'message = {message}')

    signature = ds.sign(message, d)[1]
    print(f'signature = {signature}')






