import hashlib
import base64
import secrets
import random
import string

strRange = string.ascii_letters + string.digits

licFile = open("demofile.txt", "a")
#while True:
#    licSecret = ''.join(secrets.choice(strRange) for i in range(10))
#    if (any(c.islower() for c in licSecret)
#            and any(c.isupper() for c in licSecret)
#            and sum(c.isdigit() for c in licSecret) >= 3):
#        break

def createLicence(appName: str, appVersion: int, licMode: int, licHolderName: str, licHolderID: int) :
    print("creating licence")
    
    licSecret = ''.join(secrets.choice(strRange) for i in range(10))
    print(licSecret)

    if licMode == 0 :
        hashedAppName = base64.b64encode(bytes(appName.encode("utf-8"))).decode("utf-8")
        hashedAppVersion = base64.b64encode(bytes(appName.encode("utf-8"))).decode("utf-8")
        hashedLicHolderName = base64.b64encode(bytes(licHolderName.encode("utf-8"))).decode("utf-8")
        hashedLicHolderID = base64.b64encode(bytes(licHolderID.encode("utf-8"))).decode("utf-8")
    elif licMode == 1 :
        hashedAppName = (hashlib.md5(appName.encode("utf-8"))).hexdigest()
        hashedAppVersion = (hashlib.md5(appVersion.encode("utf-8"))).hexdigest()
        hashedLicHolderName = (hashlib.md5(licHolderName.encode("utf-8"))).hexdigest()
        hashedLicHolderID = (hashlib.md5(licHolderID.encode("utf-8"))).hexdigest()
    else :
        print("Unknown Licencing Tech")     


    licFile.write(licSecret + "\n")

# createLicence("AAZZAZZAZ", 123, 0, "SKAS", 12)