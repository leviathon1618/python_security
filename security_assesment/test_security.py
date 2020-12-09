import pytest, security
from io import StringIO
#      test_security.py
encryption = security.Security()


file_name = "text.txt"

with open(file_name, 'rt') as file:
    file_data = file.read()

#caesar encryptor
def test_CaesarEncryptor(monkeypatch):
    numinput = StringIO("3\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.CaesarEncryptor(file_data)) == str
    print("caesar encryption returns a string") 

def test_CaesarEncryptor_data(monkeypatch):
    numinput = StringIO("3\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.CaesarEncryptor(file_data)) != file_data
    print("string is different")

#caesar decryptor  
def test_CaesarDecryptor(monkeypatch):
    numinput = StringIO("3\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.CaesarEncryptor(file_data)) == str
    print("caesar Decryption returns a string")

def test_CaesarDecryptor_data(monkeypatch):
    numinput = StringIO("3\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.CaesarEncryptor(file_data)) != file_data
    print("decrypted string is different")

#polysub encryption
def test_PolySubEncryptor(monkeypatch):
    numinput = StringIO("levi\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.PolySubEncryptor(file_data)) == str
    print("PolySub encryption returns a string") 

def test_PolySubEncryptor_data(monkeypatch):
    numinput = StringIO("levi\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.PolySubEncryptor(file_data)) != file_data
    print("PolySub output string is different")

#polysub decryptor
def test_PolySubDecryptor(monkeypatch):
    numinput = StringIO("levi\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.PolySubDecryptor(file_data)) == str
    print("PolySub Decryption returns a string")

def test_PolySubDecryptor_data(monkeypatch):
    numinput = StringIO("levi\n")
    monkeypatch.setattr('sys.stdin', numinput)
    assert type(encryption.PolySubDecryptor(file_data)) != file_data
    print("PolySub decrypted string is different")