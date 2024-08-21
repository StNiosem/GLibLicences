import hashlib
import base64
import secrets
import random
import string

strRange = string.ascii_letters + string.digits

#while True:
#    licSecret = ''.join(secrets.choice(strRange) for i in range(10))
#    if (any(c.islower() for c in licSecret)
#            and any(c.isupper() for c in licSecret)
#            and sum(c.isdigit() for c in licSecret) >= 3):
#        break

def createLicence(appName: str, appVersion: int, licMode: str, licHolderName: str, licHolderID: int, licSecret) :
    print("creating licence")