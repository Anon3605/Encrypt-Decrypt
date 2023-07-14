def caeser_encryption():
    import random as random_key
    key=random_key.randint(99,127) #This Range is used as less error rate
                                   #As this is converting to ascii, there are
                                   #some fault with punctuations
    file01=open("Input Text.txt", "r")
    file02=open("Ciper Text.txt","w")
    for lines in file01:
        for words in lines.rstrip():
            file02.write(chr((ord(words)+key)%128))
        file02.write("\n")
    file01.close()
    file02.close()
    return key

def caeser_decryption(key):
    file01=open("Ciper Text.txt","r")
    file02=open("Plain Text.txt", "w")
    for lines in file01:
        for words in lines.rstrip():
            if (ord(words)-key)<0:
                file02.write(chr(ord(words)-key+128))
            else:
                file02.write(chr(ord(words)))
        file02.write("\n")
    file01.close()
    file02.close()
    print("Process Ended You can check your plain text in \"Plain Text.txt\"\nThank You")

#Main Code

breaker=""
while breaker!="stop":
    mode=input("Input the mode(e/d): ").lower()
    if mode=="e":
        key=caeser_encryption()
        print(f'Your Key is: {key}')
        print("Keep it safe. The encrypted file is stored in \"Ciper Text.txt\" file.")
        print("Decryption the same message run decryption mode and enter the key")
    elif mode=="d":
        print("Enter the Key")
        key=int(input("Key: "))
        file02=open("Ciper Text.txt","r")
        caeser_decryption(key)
    else:
        print("Input is Invalid, try again")
    breaker=input("Do you wanna stop the program?(Input \"Stop\"): ").lower()
