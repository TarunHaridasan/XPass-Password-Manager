import json
from passlib.hash import pbkdf2_sha512
from . import manager

#Read json file
def read():
    try:
        with open("./data/login.json") as f:
            data = json.load(f)
        return data
    except:
        return False

#Write json file
def write(data):
    try:
        with open("./data/login.json", "w") as f:
            json.dump(data, f, indent=4)
        return True
    except:
        return False

#Check if username exists in database
def userExists(username):
    data = read()
    if username in data.keys():
        return True
    return False

#Check user credentials when logging in
def verifyLogin(username, password):
    data = read()
    if username in data.keys() and pbkdf2_sha512.verify(password, data[username]):        
        return data[username]
    return False

#Add a new user to the database and make them a vault
def addUser(username, password):
    #Add user to database
    data = read()
    if username in data.keys():
        return False 
    hashedPassword = pbkdf2_sha512.using(rounds=30000, salt_size=32).hash(password)   
    data[username] = hashedPassword

    #Make new vault file 
    fName = hashedPassword.split("$")[4].replace("/", "").replace(".", "") + ".txt"
    vault = manager.Vault(hashedPassword, username, password)    
    print(hashedPassword + "\n" + username + "\n" + password)
    return write(data)

#addUser("Tarun", "dog123")