from google.cloud import firestore_v1 as firestore

USERS = u'Users'


# Todo check for exeption in case that the user already exist
def create_user(mail, pwd, institution, phone, name, surname):
    doc = get_user(mail)
    if doc is not None:
        # todo throw exception here
        print('User already exist')
    else:
        db = firestore.Client()
        db.collection(USERS).add({
            u'Mail': mail,
            u'Password': encrypt_password(pwd),
            u'Phone': phone,
            u'Name': name,
            u'Surname': surname,
            u'Institution': institution,
        })


# Returns the information of the user in case that the  mail and password match
def login(mail, pwd):
    doc = get_user(mail)
    if doc is not None:
        if doc['Password'] == encrypt_password(pwd):
            return doc
    return None


def get_user(mail):
    db = firestore.Client()
    docs = db.collection(USERS).where(u'Mail', u'==', mail).stream()
    for doc in docs:
        # returns the first object
        return doc.to_dict()

    return None


# Receives the password and encrypts it
def encrypt_password(password):
    import hashlib
    encrypted_pass = hashlib.sha256().hexdigest()
    return encrypted_pass
