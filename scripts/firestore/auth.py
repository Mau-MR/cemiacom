


# Receives the password and encrypts it
def encrypt_password(password):
    import hashlib
    encrypted_pass = hashlib.sha256().hexdigest()
    return encrypted_pass
