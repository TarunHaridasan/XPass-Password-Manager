from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import json
import os

#Vault Class
class Vault():
    records = {}
    
    #Class constructor 
    def __init__(self, authKey, username, password):
        self.vaultKey = self.generateVaultKey(authKey, username, password)
        self.fp = self.genVaultFilePath(authKey)
        self.records = {}
        #Check if vault exists
        if os.path.isfile(self.fp):            
            encVault = self.read()
            fernet = Fernet(self.vaultKey)
            vault = json.loads(fernet.decrypt(encVault).decode("utf-8"))
            self.records = vault
        else:
            try:
                open(self.fp, "x")
                self.encryptVault()
            except:
                pass
    
    #Read vault
    def read(self):
        try:
            with open(self.fp, "rb") as f:
                data = f.read()
            return data
        except:
            return False

    #Write vault
    def write(self, data):
        try:
            with open(self.fp, "wb") as f:
                f.write(data)
            return True
        except:
            return False
    
    #Add username-password record to the password manager
    def add(self, name, url, username, password):
        try:
            record = {"url": url, "username": username, "password": password}
            self.records[name] = record
            return True
        except:
            return False

    #Retrieve a record from the password manager
    def get(self, name):
        if name in self.records.keys():
            return self.records[name]
        return False

    #Remove a username-password record from the password manager
    def remove(self, name):
        if name in self.records.keys():
            del self.records[name]
            return True
        return False

    #Generate 32-byte b64_encoded vault key from auth key and password
    def generateVaultKey(self, authKey, username, password):
        key = username + authKey + password
        kdf = PBKDF2HMAC(hashes.SHA512, 32, username.encode("utf-8"), 250000)
        vaultKey = urlsafe_b64encode(kdf.derive(key.encode("utf-8")))
        return vaultKey

    #Encrypt vault
    def encryptVault(self):
        fernet = Fernet(self.vaultKey)
        vault = fernet.encrypt(json.dumps(self.records, indent=4).encode("utf-8"))
        return self.write(vault)    

    #Generate vault file path
    @staticmethod
    def genVaultFilePath(hashedPassword):
        fName = hashedPassword.split("$")[4].replace("/", "").replace(".", "") + ".txt"
        fp = "./data/vaults/{}".format(fName)
        return fp