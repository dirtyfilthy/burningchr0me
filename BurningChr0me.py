#!/usr/bin/env python3

import os
import sys
import hashlib
import random
import string
import time
import subprocess
import shutil
import logging
import argparse
import gettext as _
from Crypto.Cipher import AES

## CONSTANDS
DEBUG = False
AUTHOR = "alhazred"
VERSION = "0.0.1"
NAME = "BurningChr0me"
ENCRYPTED_EXTENSION = ".enc"

LOGO = f"""

 ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓██████▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█████▓▒░   
 ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░  
  ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░         
 ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒▒███▓▒░  
 ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░  
░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░  
 ░▒▓██████▓▒░ ░▒▓█████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█████▓▒░   
                                                                                                                                                              
  ░▒▓█████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓██████▓▒░░▒▓███████▓▒░▒▓████████████▓▒░░▒▓███████▓▒░ 
 ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░     ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░     ░▒▓███████▓▒░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█████▓▒░   
 ░▒▓█▓▒░     ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░ 
                                                                                       
{NAME} v{VERSION} by {AUTHOR}                                                                                      
"""


## PRINTING FUNCTIONS

def print_warn(s):
    print(f"[!] {s}")

def print_error(s):
    print(f"[!] ERROR: {s}")
    sys.exit(1)

def print_debug(s):
    if not DEBUG:
        return
    print(f"DEBUG: {s}")

def print_info(s):
    print(f"[?] {s}")

def print_action(s):
    print(f"[+] {s}")

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="BurningChr0me")
    parser.add_argument("-e","--encrypt", action="store_true", help="Encrypt a file")
    parser.add_argument("-d","--decrypt", action="store_true", help="Decrypt a file")
    parser.add_argument("-k","--key", type=str,help="Key to use for encryption or decryption")
    parser.add_argument("-l","--list", action="store_true", help="interpret PATH as a file of newline separated paths")
    parser.add_argument("-v","--verbose", action="store_true", help="Verbose output")
    parser.add_argument("PATH", help="Path to encrypt or decrypt")
   
    return parser.parse_args()


def walk_path(path):
    """Walk a path and return a list of files"""
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)


def encrypt_path(path, key):
    for file in walk_path(path):
        if file.endswith(ENCRYPTED_EXTENSION):
            print_warn(f"Skipping {file} because it is already encrypted")
            continue
        try:
            encrypt_file(file, file + ENCRYPTED_EXTENSION, key)
            print_action(f"Encrypted {file}")
            # remove the original file
            os.remove(file)
            print_action(f"Removed {file}")
        except Exception as e:
            print_error(f"Error encrypting {file}: {e}")
            continue
     
            

def decrypt_path(path, key):
    for file in walk_path(path):
        print_debug(f"Decrypting {file}")
        if not file.endswith(ENCRYPTED_EXTENSION):
            print_warn(f"Skipping {file} because it is not encrypted")
            continue
        try:
            decrypt_file(file, file[:-len(ENCRYPTED_EXTENSION)], key)
            print_action(f"Decrypted {file}")
            # remove the encrypted file
            os.remove(file)
            print_action(f"Removed {file}")
        except Exception as e:
            print_error(f"Error decrypting {file}: {e}")
            continue
        print_debug(f"after decrypt {file}")
     
           

def main():
    """Main function"""
    global DEBUG
    print(LOGO)
    args = parse_args()
    if args.verbose:
        DEBUG = True
    print_debug(f"Args: {args}")
    if not args.encrypt and not args.decrypt:
        print_error("Please specify either --encrypt or --decrypt")
   

    if args.decrypt and args.encrypt:
        print_error("Cannot decrypt and encrypt at the same time")
       

    if not args.key:
        print_warn("No key specified")
        if not args.encrypt:
            print_error("Please specify a key for decryption")
        args.key = generate_key()
        print_action(f"Generated key: {args.key.hex()}")
    else:
        if len(args.key) != 64:
            print_error("Key must be 64 characters long")
        args.key = bytes.fromhex(args.key)
    print_debug(f"Key: {args.key}")
    print_info(f"Using key: {args.key.hex()}")
    if not os.path.exists(args.PATH):
        print_error(f"File {args.PATH} does not exist")
        sys.exit(1)
  
    paths = [args.PATH]

    if args.list:
        with open(args.PATH, "r") as f:
            paths = f.read().strip().split("\n")
        print_debug(f"Paths: {paths}")

    for path in paths:

        if not os.path.exists(path):
            print_error(f"File {path} does not exist")
        if args.encrypt:
            print_action(f"Encrypting {path}")
            encrypt_path(path, args.key)
        elif args.decrypt:
            print_action(f"Decrypting {path}")
            decrypt_path(path, args.key)


## encryption functions

def generate_key():
    """Generate a random 256-bit key"""
    return os.urandom(32)


def encrypt_file(src_path, dest_path, key):
    """Encrypt a file using AES-256-GCM"""
   
    # Read the file
    with open(src_path, 'rb') as f:
        data = f.read()

    # Generate a random IV
    iv = os.urandom(16)
    
    # Create AES cipher
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    
    # Encrypt the data
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    # Write the encrypted data to the destination file
    with open(dest_path, 'wb') as f:
        f.write(iv + tag + ciphertext)


def decrypt_file(src_path, dest_path, key):
    """Decrypt a file using AES-256-GCM"""
   
    # Read the file
    with open(src_path, 'rb') as f:
        data = f.read()

    # Extract IV, tag, and ciphertext
    iv = data[:16]
    tag = data[16:32]

    # Create AES cipher
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

    # Decrypt the data
    plaintext = cipher.decrypt_and_verify(data[32:], tag)

    # Write the decrypted data to the destination file
    with open(dest_path, 'wb') as f:
        f.write(plaintext)

if __name__ == "__main__":
    main()