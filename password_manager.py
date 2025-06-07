from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


'''def write_key():
    key= Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()'''    

master_pwd= input("What is your master password? ")
key= load_key()+master_pwd.encode()
fer= Fernet(key)

def view():
    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:  # Ensure the line contains "|"
                parts = data.split("|", 1)
                if len(parts) == 2:  # Check if split resulted in two values
                    user, passw = parts
                    print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())
            
def add():
    name = input("Enter account name: ")
    pwd= input("Enter password: ")
    with open("Password.txt","a") as f:
        f.writelines(name+":"+fer.encrypt(pwd.encode()).decode()+"\n")


while True:
    mode= input("Do you want to add a new password or view existing password (view/add)? \nPress q to quit ")
    if str.lower(mode) =="q":
        break
    if mode=="view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")