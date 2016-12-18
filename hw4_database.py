import os
import re

def function1 ():

    os.system("C:\\Users\\Настя\\Desktop\\mystem.exe " + " bd_lucomor.txt" + " bd_lucomor_ms.txt" + ' -cn')
    f = open ('C:\\Users\\Настя\\Desktop\\bd_lucomor_ms.txt', 'r', encoding = 'utf-8')
    words = f.readlines()
    f.close ()
    strings = []
    d = {}
    #num = 0
    for word in words:
        word = word.lower ()
        #num += 1
        regexp = '(.*?){(.*?)}'
        res = re.search (regexp, word)
        token = ''
        if res:
            token = res.group(1)
            if token not in d:
                d[token] = res.group (2)
                strings.append (token + '\t' + d [token] + '\t' + '1')
            
        else:
            regexp2 = '(.).*?'
            res = re.search (regexp2, word)
            punct = ''
            if res:
                punct = res.group(1)
                if punct not in d and punct != '_':
                    d[punct] = punct
                    strings.append (punct + '\t' + d [punct] + '\t' + '0')

##    print (d)
##    for x in strings:
##        print (x)

    return strings

def function2 (strings):
    command = ''
    for string in strings:
        kletki = string.split ('\t')
        values = '\'' + kletki [0] + '\', \'' + kletki [1] + '\', \'' + kletki [2] + '\''
        command = command + 'INSERT INTO Tokens (token, lemma, type) VALUES (%s)'%values + ';\n'
    command = command[0: -2]
    print (command)
    f = open ('C:\\Users\\Настя\\Desktop\\inserts.txt', 'w', encoding = 'utf-8')
    f.write(command)
    f.close
    
    
def main ():
    f1 = function1 ()
    f2 = function2 (f1)

    
if __name__ == '__main__':
    main ()
