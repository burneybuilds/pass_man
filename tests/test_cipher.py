from pas_man.cipher import decrypt_pass, encrypt_pass


def test_encrypt_decrypt_round_trip():
    encrypted, salt, nonce = encrypt_pass("master-key", "secret-password")

    assert decrypt_pass("master-key", encrypted, salt, nonce) == "secret-password"