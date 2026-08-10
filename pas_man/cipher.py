import secrets

from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_pass(master_pass, password): 
    master_pass = master_pass.encode("utf-8")
    password = password.encode("utf-8")

    salt = secrets.token_bytes(16)  # Save this with the vault

    key = hash_secret_raw(
    secret=master_pass,
    salt=salt,
    time_cost=3,
    memory_cost=65536,  # 64 MB
    parallelism=4,
    hash_len=32,        # 32-byte key for AES-256
    type=Type.ID        # Argon2id
    )

    aes = AESGCM(key)
    nonce = secrets.token_bytes(12)  # Generate a new random nonce for every encryption

    ciphertext = aes.encrypt(
        nonce=nonce,
        data=password,
        associated_data=None
    )

    return ciphertext , salt, nonce


def decrypt_pass(master_pass, password, salt, nonce):
    master_pass = master_pass.encode("utf-8")
    # password = password.encode()
    
    key = hash_secret_raw(
    secret=master_pass,
    salt=salt,
    time_cost=3,
    memory_cost=65536,  # 64 MB
    parallelism=4,
    hash_len=32,        # 32-byte key for AES-256
    type=Type.ID        # Argon2id
    )

    aes = AESGCM(key)
     
    plaintext = aes.decrypt(
    nonce=nonce,
    data=password,
    associated_data=None
    )

    return plaintext.decode("utf-8")
