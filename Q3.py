#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests # if this lib isn't installed yet --> pip install requests or pip3 intall requests
import time
import collections
#Dont forget to open vpn
API_URL = 'http://10.36.52.109:5000' # ATTN: This is the current server (do not change unless being told so)
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

# The extended Euclidean algorithm (EEA)
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Modular inverse algorithm that uses EEA
def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def deneme(query):
        # Below is the sample code for sending your response back to the server
            endpoint = '{}/{}/{}/{}'.format(API_URL, "affine_game", my_id, query)
            response = requests.put(endpoint)
            if response.ok:
                c = response.json()
                print(c)
                query="yeter"
            elif (response.status_code == 404):
                print("check paramater types")
            elif(response.status_code == 406):
                print("Nope, Try again")
            elif(response.status_code == 401):
                print("Check your ID number")
            else:
                print("How did you get in here? Contact your TA")


if __name__ == '__main__':
    my_id = 20659	# ATTN: change this to your id number. it should be 5 digit number
    
    cipher_text = None
    letter = None

    endpoint = '{}/{}/{}'.format(API_URL, "affine_game", my_id )
    response = requests.get(endpoint) 	#get your ciphertext and most freq. letter
    if response.ok:	#if you get your ciphertext succesfully
        c = response.json()
        cipher_text = c[0]    #this is your ciphertext
        letter = c[1] 	#the most frequent letter in your plaintext
        print(cipher_text)
        print(letter)
        print(collections.Counter(cipher_text).most_common(1)[0][0])
    
        turkish_alphabet ={'A':0, 'B':1, 'C':2, 'Ç':3, 'D':4, 'E':5, 'F':6, 'G':7, 'Ğ':8, 'H':9, 'I':10,
             'İ': 11, 'J':12, 'K':13, 'L':14, 'M':15, 'N':16, 'O':17, 'Ö':18, 'P':19, 
             'R':20, 'S':21,  'Ş':22, 'T':23, 'U':24, 'Ü':25, 'V':26, 'Y':27,
             'Z':28}

        inv_turkish_alphabet = {0:'A', 1:'B', 2:'C', 3:'Ç', 4:'D', 5:'E', 6:'F', 7:'G', 8:'Ğ', 9:'H',
                      10:'I', 11:'İ', 12:'J', 13:'K', 14:'L', 15:'M', 16:'N', 17:'O', 18:'Ö',
                      19:'P', 20:'R', 21:'S',  22:'Ş', 23:'T', 24:'U', 25:'Ü', 26:'V',
                      27:'Y', 28:'Z'}
    
        
############ write decryption code for affine cipher here ##########
        def Affine_Dec(ptext, key):
                plen = len(ptext)
                ctext = ''
                for i in range (0,plen):
                    letter = ptext[i]
                    if letter in turkish_alphabet:
                        poz = turkish_alphabet[letter]
                        poz = (gamma*poz+theta)%29
                        ctext += inv_turkish_alphabet[poz]
                    else:
                        ctext += ptext[i]
                return ctext
        
       
        for x in range(1,29):
            try:
                alpha=x
                beta=12
                gamma=modinv(alpha,29)
                theta=29-(gamma*beta)%29
                key=[gamma,theta]
                new_word1=Affine_Dec(cipher_text,key)
                query=new_word1
                catch=deneme(query)
                print(" Current Key is "+str(alpha)+" "+str(beta))
            except Exception as e:
                print("This key is not correct")
          


####################################################################

    elif(response.status_code == 404):
        print("We dont have a student with this ID. Check your id num")
    else:
        print("It was supposed to work:( Contact your TA")



    
    


#CHECK YOUR ANSWER HERE
# ATTN: change this into the decrypted plaintext to be checked by the server. should be a string


# In[ ]:





# In[ ]:




