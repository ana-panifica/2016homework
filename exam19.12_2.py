import os
import re

def function1 ():


    os.system("C:\\Users\\Настя\\Desktop\\mystem.exe " + " adyghe-unparsed-words.txt" + " adyghe-unparsed-words_ms.txt" + ' -cnid')

    f = open ('C:\\Users\\Настя\\Desktop\\adyghe-unparsed-words_ms.txt', 'r', encoding = 'utf-8')
    arr = f.readlines ()
    f.close ()


    rus_nouns = []
    regexp1 = '(.*?){.*?=S.*?,ед,.*?=им.*?}'
    for word in arr:
        text = re.search (regexp1, word)
        if text:
            #print ('ok')
            rus_noun = text.group (1)
            rus_nouns.append (rus_noun)
            
    rus_nouns_str = ''
    for x in rus_nouns:
        rus_nouns_str = rus_nouns_str + x + '\n'
        print (x)
        
        
    f = open ('C:\\Users\\Настя\\Desktop\\rus_nouns.txt', 'w', encoding = 'utf-8')
    f.write(rus_nouns_str)
    f.close ()    

def main ():
    f1 = function1 ()

    
if __name__ == '__main__':
    main ()
