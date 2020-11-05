#!/usr/bin/env python
# coding: utf-8

# In[8]:


import collections
import time
alphabet = 'abcdefghijklmnopqrstuvwxyz'
import string
result = ""
alphabet=alphabet.upper()
strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'     
def shifttext(inp,shift):
    result=""
    result=(strs[(strs.index(inp) - shift) % 26])  
    return result



text="Fwg atax: P’tx oh li hvabawl jwgvmjs, nw fw tfiapqz lziym,rqgv uuwfpxj wpbk jxlnlz fptf noqe wgw.Qoifmowl P bdg mg xv qe ntlyk ba bnjh vcf ekghnizl fq blidb eayz jgzbwx sqwm lgglbtqgy xlip.Pho fvvs ktf C smf ur ecul ywndxlz uv mzcz xxivw?Qomdmowl P bgzg, oblzqdxj C swas,B kyl btm udujs dcbfm vn yg eazl, pqzx,oblzq Q’ow mwmzb lg ghvk gxslz, emamwx apqu, wwmazagxv nomy bhlustk.”Ghm qvv’f nbfx h vqe vgoubdg, pgh’a nuvw shvbtmk kbvzq.Baam jqfg pafs ixetqm wcdanw svc.Kwn’df dixs mzy ziym llllmfa, zjid wxlbf nom eifw hlqspuglowall, loyv sztq cu btmlw mhuq phmmla.Kwn’df htiirk yul gx bf noqe kbls. Kwz’b agjl naz mzcuoe mekydpqzx:lblzq’a gg moqb nhj svc, fpxjy’z va zhsx.Uwi basn fwg’dx ouzbql rgoy tunx zyym, uv mzcz ayied wvzzmk,qib’dq lxknywkmw an ldqzroblzq qg lbl eazev."

text=text.translate(str.maketrans('', '', string.punctuation))
keys=[]
text=text.translate({ord(c): None for c in string.whitespace})
text=text.translate({ord(i): None for i in "’"})
text=text.translate({ord(i): None for i in "”"})
text=text.upper()
text2=text
print(text2)


for current in range(int(len(text))):
    text2=" "+text2
    after=0

    for deneme in range(int(len(text))):
        if text[deneme]==text2[deneme]:
            after+=1
    keys.append(after)

print(max(keys))
print(keys.index(max(keys)))
print(keys)
print("---")

shifts=[]
deneme=0
picker=[0,7,14,21,28,35,42]
start=0
for t in range(7):
    sub_text=""
    for x in range(int(len(text))):
        try:
            sub_text+=text[(x*7)+t]
        except:
            break;
    shifts.append(sub_text)

print(shifts)
for t in range(len(shifts)):
    print(t)
    print(collections.Counter(shifts[t]).most_common(10))

    
    
def shifter(result,text):
    for x in range(0,len(text),7):
        try:
            result = result + shifttext(text[x],7) 
            result = result + shifttext(text[x+1],8) 
            result = result + shifttext(text[x+2],12) 
            result = result + shifttext(text[x+3],8) 
            result = result + shifttext(text[x+4],19) 
            result = result + shifttext(text[x+5],18) 
            result = result + shifttext(text[x+6],20)
        except:
            print("END OF SHIFTING")
    return result
   
 


# In[ ]:


print(shifter(result,text))
time.sleep(20)
print("END OF EXECUTION")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




