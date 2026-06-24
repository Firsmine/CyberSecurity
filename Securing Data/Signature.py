"""
First, install the library in the terminal
>>> pip install cryptography
Follow the step like, update the pip
>>> python.exe -m pip install --upgrade pip
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()