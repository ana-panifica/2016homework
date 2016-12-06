import os
import urllib.request
import re
import html
def function1 ():
    d = {'https://regnum.ru/news/innovatio/2211264.html': '<div class="news_body" data-id="2211264">([\s\S]+?)</div>',
         'https://rg.ru/2016/11/29/na-marse-obnaruzhen-labirint.html': '<div itemprop="articleBody">([\s\S]+?)<!--incut b-read-more_width-->',
         'http://www.rosbalt.ru/style/2016/11/29/1571387.html': '<div class="newstext">([\s\S]+?)</div>',
         'http://www.vesti.ru/doc.html?id=2827056': '<div class="article__text">([\s\S]+?)</div>'}
    d2 = []

    for i in d:

        #print ('kk')
        req = urllib.request.Request(i)
        with urllib.request.urlopen(req) as response:
           htmlnew = response.read().decode('utf-8')

                        
           
           regexp1 = d [i]
           text = re.search (regexp1, htmlnew)
           article = ''
           if text:
               #print ('ok')
               article = text.group (1)
           else:
               print ('not ok')

           
           t = article  # тут какой-то html
           regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)  # это рег. выражение находит все тэги
           regScript = re.compile('<script>.*?</script>', flags=re.U | re.DOTALL) # все скрипты
           regComment = re.compile('<!--.*?-->', flags=re.U | re.DOTALL)  # все комментарии


# а дальше заменяем ненужные куски на пустую строку
           clean_t = regScript.sub("", t)
           clean_t = regComment.sub("", clean_t)
           clean_t = regTag.sub("", clean_t)


           clean_t = html.unescape(clean_t)

           clean_t = clean_t.replace ('\n', ' ')
           clean_t = clean_t.replace ('\t', ' ')
           clean_t = clean_t.replace ('\r', ' ')
           string = clean_t.strip ()

           string = string.lower ()
           string = string.split (' ')
           for x in range (len (string)):
                string [x] = string [x].strip ('.,;:!')
            
           #for y in string:
               #print (y)
               
           d2.append (string)

           
    #print (d2)
    
    return d2
           

def function2 (d2):
    items1 = set ()
    for i in d2 [0]:
        items1.add (i)

    items2 = set ()
    for i in d2 [1]:
        items2.add (i)

    items3 = set ()
    for i in d2 [2]:
        items3.add (i)

    items4 = set ()
    for i in d2 [3]:
        items4.add (i)

    #print (items4)

    inters_mn = items1&items2&items3&items4
    inters_mas = []
    for w in inters_mn:
        inters_mas.append (w)
    inters_mas.sort()
    print (type (inters_mas))
    string_inters = ''
    for t in inters_mas:
        string_inters = string_inters + t +'\n'

    f = open ('C:\\Users\\Настя\\Desktop\\labirint.txt', 'w', encoding = 'utf-8')
    f.write('Эти словоформы для всех заметок в сюжете являются общими:' + '\n' + string_inters)
    f.close()
    
    #print (string_inters)

    sym_dif_mn = items1^items2^items3^items4
    sym_dif_mas = []
    for ws in sym_dif_mn:
        sym_dif_mas.append (ws)
    sym_dif_mas.sort()
    print (type (sym_dif_mas))
    string_sym_dif = ''
    for ts in sym_dif_mas:
        string_sym_dif = string_sym_dif + ts +'\n'

    f = open ('C:\\Users\\Настя\\Desktop\\labirint.txt', 'a', encoding = 'utf-8')
    f.write('\n' + 'А эти словоформы являются уникальными для новостных заметок в пределах сюжета:' + '\n' + string_sym_dif)
    f.close()

    #print (string_sym_dif)
    
def main ():
    f1 = function1 ()
    f2 = function2 (f1)

    
if __name__ == '__main__':
    main ()
