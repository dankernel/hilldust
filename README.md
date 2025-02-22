# Hilldust [![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/) 
(UNOFFICIAL) Yet another implementation of *Hillstone™ Secure Connect VPN Client* for Linux

and for macOS later.

## Install
```sh
pip install hillstone-client
```
or
```
pip install git+https://github.com/dankernel/hilldust.git
```
## Usage
```
sudo hillstone-client <vpn.yourdomain.com:port> <username> <password>
```
**note** : If <username> or <password> contains shell speacial keywords such as '!' or '@'
wrap up string with single quote. Ex. 'abcd!@'
  ![image](https://user-images.githubusercontent.com/8120041/152638891-9c1390ec-1fa6-4d4f-af25-29f92f0ac673.png)

## Notes
For now, it is only a proof-of-concept and may be not available for all the users,
because it only supports auth: `HMAC-SHA1-96`, crypto: `3DES-CBC`.

## Dependencies
- Python 3
- scapy (Python module)
- cryptography (Python module)
- iproute2

Please note different systems may have different names for Python 3.
It can be: `python3` with `pip3`, or `python` with `pip`,

You may use the shortcut: `pip3 install -r requirements.txt` to install all
Python modules the program needs.

You may use `ip -Version` to check if your system is missing iproute2 utility.
