from google.cloud import firestore_v1 as firestore

USERS = u'Users'


def create_user(mail, pwd, institution, phone, name, surname):
    db = firestore.Client()
    db.collection(USERS).add({
        u'Mail': mail,
        u'Password': encrypt_password(pwd),
        u'Phone': phone,
        u'Name': name,
        u'Surname': surname,
        u'Institution': institution,
    })


# Receives the password and encrypts it
def encrypt_password(password):
    import hashlib
    encrypted_pass = hashlib.sha256().hexdigest()
    return encrypted_pass
