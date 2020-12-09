class Security:

    def __init__(self):
        self.data = []
        self.str = ""

    def CaesarEncryptor(self, text): 
        key = int(input("please enter an integer number as a key "))                 
        enc_result = ""    
        for i in range(len(text)):   
            char = text[i]                                
            enc_result += chr((ord(char) + key)) 
        f = open("caesar_encrypted.txt", "w")
        f.write(enc_result)
        f.close()     
        return enc_result

    def CeasarDecryptor(self, text=""):
        key = int(input("please enter an integer number as a key "))        
        enc_result = ""
        key = -key
        for i in range(len(text)):   
            char = text[i]       
            enc_result += chr((ord(char) + key))
            
            newLine = chr((ord(char) + key))
            if ord(newLine) == 7:  
                enc_result += "\n"
                
        f = open("caesar_decrypted.txt", "w")
        f.write(enc_result)
        f.close()            
        return enc_result

    def PolySubEncryptor(self,text=""):
        key = input("please enter an string as a key ")
        k_len = len(key)
        k_ints = [ord(i) for i in key]
        txt_ints = [ord(i) for i in text]
        ret_txt = ''

        for i in range(len(txt_ints)):
            adder = k_ints[i % k_len]
            v = (txt_ints[i] - 10 + adder) % 117
            ret_txt += chr(v + 10)

        
        f = open("polysub_encrypted.txt", "w")
        f.write(ret_txt)
        f.close() 
        return ret_txt

    def PolySubDecryptor(self,text=""):
        key = input("please enter an string as a key ")
        k_len = len(key)
        k_ints = [ord(i) for i in key]
        txt_ints = [ord(i) for i in text]
        ret_txt = ''

        for i in range(len(txt_ints)):
            adder = k_ints[i % k_len]
            adder *= -1           
            v = (txt_ints[i] - 10 + adder) % 117
            ret_txt += chr(v + 10)

        f = open("polysub_decrypted.txt", "w")
        f.write(ret_txt)
        f.close()
        return ret_txt
