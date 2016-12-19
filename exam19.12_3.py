import os
import re

def function1 ():


    os.system("C:\\Users\\Настя\\Desktop\\mystem.exe " + " rus_nouns.txt" + " rus_nouns_ms.txt" + ' -cn')

    f = open ('C:\\Users\\Настя\\Desktop\\rus_nouns_ms.txt', 'r', encoding = 'utf-8')
    razbory = f.readlines ()
    f.close ()

    d = {}
    strings = []
    for word in razbory:
        regexp = '(.*?){(.*?)}'
        res = re.search (regexp, word)
        token = ''
        if res:
            token = res.group(1)
            if token not in d:
                d[token] = res.group (2)
                if '|' in d[token]:
                    lemmy = d[token].split ('|')
                    for x in range (len (lemmy)):
                        strings.append (token + '\t' + lemmy[x])
                else:
                    strings.append (token + '\t' + d[token])
    
    command = ''
    for string in strings:
        kletki = string.split ('\t')
        values = '\'' + kletki [0] + '\', \'' + kletki [1] + '\''
        command = command + 'INSERT INTO rus_words (wordform, lemma) VALUES (%s)'%values + ';\n'
    command = command[0: -2]
    print (command)
    f = open ('C:\\Users\\Настя\\Desktop\\sql.txt', 'w', encoding = 'utf-8')
    f.write(command)
    f.close       

    

def main ():
    f1 = function1 ()

    
if __name__ == '__main__':
    main ()
