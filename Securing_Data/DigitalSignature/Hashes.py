"""
First, install the library in the terminal
>>> pip install cryptography
Follow the step like, update the pip
>>> python.exe -m pip install --upgrade pip
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# generate keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

message = input("\nMessage: ").encode()

# signature
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)
print("\nMessage Signed.")

# verify
try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Signature VALID")
except:
    print("Signature INVALID")