#этот код собирает текст для корпуса из субтитров, лежащих на диске

import os
import re

def make_corpus ():
    lst = os.listdir ('D:\\OneDrive\\Documents\\2016-2017\\Python16-17\\exam_project\\Once_Upon_a_Time_TV_2011_Rus')
    corpus = ''
    regex = '\n(.*?\n.*? --> .*?)\n'
    regex2 = 'Перевод.*?\n'
    regex3 = 'Синхронизация.*?\n'
    for name in lst:
        path = 'D:\\OneDrive\\Documents\\2016-2017\\Python16-17\\exam_project\\Once_Upon_a_Time_TV_2011_Rus\\' + name
        lst2 = os.listdir (path)
        for name2 in lst2:
            print (name2)
            path2 = path + "\\" + name2
            try:
                f = open (path2, 'r', encoding = 'cp1251')
                text = f.read ()
            except:
                f = open (path2, 'r', encoding = 'utf-8')
                text = f.read ()
            text = replacing (regex, text)
            text = replacing (regex2, text)
            text = replacing (regex3, text)
            text = text.replace ('\n\n', ' ')
            text = text.replace ('</i>', '')
            text = text.replace ('<\i>', '')
            text = text.replace ('<i>', '')
            text = text.replace ('Переведено на Нотабеноиде', '') 
            corpus = corpus + text
    f = open ('D:\\OneDrive\\Documents\\2016-2017\\Python16-17\\exam_project\\corpus.txt', 'w', encoding = 'utf-8')
    f.write (corpus)
        

def replacing (regex, text):
    res = re.findall (regex, text)
    if res:
        for x in res:
            text = text.replace (x, '')
    return text

def main ():
    make_corpus ()
    
if __name__ == '__main__':
    main ()
