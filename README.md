# BurningChr0me
```
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
            
```
A ransomware simulation tool that recursively encrypts and decrypts files using AES-256-GCM encryption.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/BurningChr0me.git
cd BurningChr0me
```

2. Install the required dependencies:
```bash
python -m venv venv
source ./venv/bin/activate
pip install pycryptodome
```

## Usage

### Basic Usage

Encrypt a file or directory:
```bash
python BurningChr0me.py -e path/to/file_or_directory
```

Decrypt a file or directory:
```bash
python BurningChr0me.py -d path/to/file_or_directory -k your_encryption_key
```

### Command Line Options

- `-e, --encrypt`: Encrypt the specified path
- `-d, --decrypt`: Decrypt the specified path
- `-k, --key`: Specify the encryption/decryption key (64 characters hex string)
- `-v, --verbose`: Enable verbose output for debugging
- `path`: Path to the file or directory to encrypt/decrypt

### Examples

1. Encrypt a directory with auto-generated key:
```bash
python BurningChr0me.py -e /path/to/directory
```

2. Decrypt a directory with a specific key:
```bash
python BurningChr0me.py -d /path/to/directory -k 0123456789abcdef...
```

3. Enable verbose mode:
```bash
python BurningChr0me.py -e /path/to/directory -v
```

## Security Notes

- The tool uses AES-256-GCM encryption, which provides both confidentiality and authenticity
- Each file is encrypted with a unique initialization vector (IV)
- The encryption key must be 64 characters long (32 bytes in hex format)
- Original files are automatically deleted after successful encryption
- Encrypted files are automatically deleted after successful decryption and restored to original file name
- Encrypted files are marked with the `.enc` extension

## Warning

⚠️ **IMPORTANT**: Always keep your encryption key safe. If you lose the key, you will not be able to decrypt your files.

## Author

Created by alhazred

## Version

Current version: 0.0.1