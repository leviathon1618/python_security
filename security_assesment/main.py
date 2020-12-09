import glob
from security import Security

#     caesar_encrypted.txt
#     polysub_encrypted.txt
data_module = Security()

def main():
    file_name = input("please input the filename.txt to transfer securely ")
    file_name = str(file_name)

    with open(file_name, 'rt') as file:
        file_data = file.read()
        
    enc_or_dec = input("you can either encrypt or decrypt.\nplease enter encrypt: E or decrypt: D ")
    enc_or_dec = str(enc_or_dec)



    if enc_or_dec == "E":
        cypher = input("are you using the ceasar cypher: C or the Polysub cypher: P? ")
        cypher = str(cypher)
        if cypher == "C":
            print("caesar cypher selected")
            
            
            data_module.CaesarEncryptor(file_data) 
            print("*** caesar cypher encryption done ***")
        
        if cypher == "P":
            print("polysub cypher selected")
            
            
            data_module.PolySubEncryptor(file_data) 
            print("*** polysub encryption done ***")



    if enc_or_dec == "D":
        cypher = input("are you using the ceasar cypher: C or the Polysub cypher: P? ")
        cypher = str(cypher)

        if cypher == "C":
            print("caesar cypher selected")
            

            data_module.CeasarDecryptor(file_data)
            print("*** caesar cypher decryption done ***")

        if cypher == "P":
            print("polysub cypher selected")
            
            
            data_module.PolySubDecryptor(file_data)
            print("*** polysub decryption done ***")

main()