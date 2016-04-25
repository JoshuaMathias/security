from Crypto.Cipher import AES
import binascii
import time

if __name__ == "__main__":
    key='oihre9w7y9e7whu8'
    iv='ufew788ewh47dhy7'
    start=time.clock()
    plaintext = open('plaintext.txt','r').read()
    padding='1'
    if (len(plaintext)%16!=0):
        dif=15-len(plaintext)%16
        for i in range(dif):
            padding+='0'
    message = plaintext+padding
    encoder = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = encoder.encrypt(message)
    print "CBC ciphertext: \n"+binascii.hexlify(ciphertext)
    decoder = AES.new(key, AES.MODE_CBC, iv)
    plaintext = decoder.decrypt(ciphertext)
    end=time.clock()
    measure=(end-start)
    print "CBC decrypted plaintext: \n"+plaintext
    print "Time taken: "+str(measure)
    start=time.clock()
    encoder = AES.new(key, AES.MODE_ECB, iv)
    ciphertext = encoder.encrypt(message)
    print "ECB ciphertext: \n"+binascii.hexlify(ciphertext)
    decoder = AES.new(key, AES.MODE_ECB, iv)
    plaintext = decoder.decrypt(ciphertext)
    print "ECB decrypted plaintext: \n"+plaintext
    end=time.clock()
    measure=(end-start)
    print "Time taken: "+str(measure)