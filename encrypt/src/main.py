# importing libraries
from cryptography.fernet import Fernet
import os
'''
mention your target file and if you want to encrypt all data then 
create a '.hrk' file and if you want to decrypt the remove this file.
'''

# mention your target directory
TARGET_FILE = '/Users/pan/desktop/neww'

'''
if you want to change the cryptography key
then run this line of code (11-17).
'''
# # generating key
# key = Fernet.generate_key()
# print(key)

# # saving key in key.txt
# with open('key.txt', 'wb') as file:
#     file.write(key)

# encrypting file
def encrypt():
    # reading key
    with open('key.txt', 'rb') as file:
        key = file.read()

    # storing key
    cipher = Fernet(key)
    global TARGET_FILE

    # accessing target files
    for root, dirs, files in os.walk(TARGET_FILE):
        for file in files:
            # mention all files
            print(file)
            '''
            if you have some extra file then add here in the given manner
            '''
            if file.endswith('.py') or file.endswith('.html') or file.endswith('.css') or file.endswith(
                    '.txt') or file.endswith('.js') or file.endswith('.c') or file.endswith('.md') or file.endswith('.cpp') or file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                try:
                    file1 = os.path.join(root, file)
                    with open(file1, 'rb') as f:
                        e_file = f.read()
                    encrypt_file = cipher.encrypt(e_file)
                    with open(file1, 'wb') as f:
                        f.write(encrypt_file)
                except: pass

# decrypting file
def decrypt():
    with open('key.txt', 'rb') as file:
        key = file.read()

    global TARGET_FILE
    # storing key
    cipher = Fernet(key)

    for root, dirs, files in os.walk(TARGET_FILE):
        for file in files:
            # mention all files
            if file.endswith('.py') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.html') or file.endswith('.css') or file.endswith('.txt') or file.endswith('.js') or file.endswith('.c') or file.endswith('.md') or file.endswith('.cpp') or file.endswith('.jpg'):
                file1 = os.path.join(root, file)
                try:
                    with open(file1, 'rb') as f:
                        e_file = f.read()
                    encrypt_file = cipher.decrypt(e_file)
                    with open(file1, 'wb') as f:
                        f.write(encrypt_file)
                except: pass

# program starts from here
if __name__ == '__main__':
    is_encrypted = False

    # if .hrk file is presented then encrypt
    for root, dirs, files in os.walk(TARGET_FILE):
        for file in files:
            '''
            if you want to change this extension then write something else
            '''
            if file.endswith('.hrk'):
                is_encrypted = True

    # execute it
    if is_encrypted:
        encrypt()
    else: decrypt()



''' 
if you have some optimized way then send me the pull request
'''