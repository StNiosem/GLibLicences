import base64
import hashlib
import os
import sys

def encodeLicenceContent_b64(hash: str, content: str, id: int) :
    completeString = ""
    completeString = hash + "--" + content + "--" + id
    b64encodedCompleteString = base64.b64encode(completeString)
    return b64encodedCompleteString

def encodeLicenceContent_sha512(hash: str, content: str, id: str) : 
    completeString = ""
    completeString = hash + "--" + content + "--" + str(id)
    sha512encodedHex = hashlib.sha512(completeString)
    sha512encodedStr = sha512encodedHex.hexdigest()
    return sha512encodedStr