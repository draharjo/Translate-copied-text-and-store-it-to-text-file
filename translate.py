# -*- coding: utf-8 -*-
"""
Program to translate a copied text & store the text to txt file
Resources to look out:
1. https://pyperclip.readthedocs.io/en/latest/
2. https://pypi.org/project/googletrans/

Need another language?
- Just change "dest" to another code language if you need to, just see google for the language code
- example --> english = "en", france = "fr"
- visit this https://developers.google.com/admin-sdk/directory/v1/languages
"""
import pyperclip
import time
from googletrans import Translator
translator = Translator()


print("==just copy the text, we do the rest :)==")
s_0 = pyperclip.copy("")
while True: 
    s_1 = pyperclip.paste()
    if s_0 != s_1:
        s_0 = s_1
        try:
            translated = translator.translate(s_0, dest='id').text
            print (s_1, translated)
            with open('dictionary.txt','a') as g:
                g.write(s_1 + "," + translated + "\n")
        except:
            pass
    time.sleep(2)
    