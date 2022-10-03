# File: Project2.py
# Student: Arshia Riaz
 
# Date Created: 11/01/2021
# Date Last Modified: 11/08/2021
# Description of Program: This program generates a substitution cipher. 

import random

# A global constant defining the alphabet. 
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or 
# define your own. You don't need to understand this code at this
# point in the semester. 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

# There may be some additional auxiliary functions defined here.
# I had several others, mainly used in encrypt and decrypt. 

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        self.key = key
        if len(key)!=26:
            print("Key entered is not legal")
            

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        """Getter for the stored key."""
        return self.key

    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        self.key = newKey

    def encryptText( self, plaintext ):
        """Return the plaintext encrypted with respect to the stored key."""
        ciphertext = ""
        lowerplaintext = plaintext.lower()
        for i in range(len(plaintext)):
            if not lowerplaintext[i].isalpha():
                ciphertext += lowerplaintext[i]
            else:
                newletter = self.key[LCLETTERS.index(lowerplaintext[i])]
                if plaintext[i].isupper():
                    newletter = newletter.upper()
                ciphertext += newletter
        return ciphertext

    def decryptText( self, ciphertext ):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        plaintext = ""
        lowerciphertext = ciphertext.lower()
        for i in range(len(ciphertext)):
            if not lowerciphertext[i].isalpha():
                plaintext += lowerciphertext[i]
            else:
                newletter = LCLETTERS[self.key.index(lowerciphertext[i])]
                if ciphertext[i].isupper():
                    newletter = newletter.upper()
                plaintext += newletter
        return plaintext

def main():
    """ This implements the top level command loop.  It
    creates an instance of the SubstitutionCipher class and allows the user
    to invoke within a loop the following commands: getKey, changeKey,
    encrypt, decrypt, quit."""
    cipherObject = SubstitutionCipher()
    command = ""
    while command != "quit":
        command = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
        command = command.lower()
        if command == "getkey":
            print("  Current cipher key:", cipherObject.getKey())
        elif command == "changekey":
            yesKey = False
            while not yesKey:
                newKey = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                if newKey == "random":
                    newKey = makeRandomKey()
                    cipherObject.setKey(newKey)
                    print("    New cipher key:", newKey)
                    yesKey = True
                elif newKey == "quit":
                    yesKey = True
                else:
                    if isLegalKey(newKey):
                        cipherObject.setKey(newKey)
                        print("    New cipher key:", newKey)
                        yesKey = True
                    else:
                        print("    Illegal key entered. Try again!")
        elif command == "encrypt":
            plaintext = input("  Enter a text to encrypt: ")
            ciphertext = cipherObject.encryptText(plaintext)
            print("    The encrypted text is:", ciphertext)
        elif command == "decrypt":
            ciphertext = input("  Enter a text to decrypt: ")
            plaintext = cipherObject.decryptText(ciphertext)
            print("    The decrypted text is:", plaintext)
        elif command == "quit":
            print("Thanks for visiting!")
            break
        else:
            print("  Command not recognized. Try again!")
        
