import re
import html

def function1 ():


    f = open ('C:\\Users\\Настя\\Desktop\\ПОЛИТИКЭР.htm', 'r', encoding = 'utf-8')
    adyg = f.read ()
    f.close ()

    regexp1 = '<a href="http://www.adygvoice.ru/wp/category/news/">([\s\S]+?)Load more posts'
    text = re.search (regexp1, adyg)
    article = ''
    if text:
        print ('ok')
        article = text.group (1)

    t = article 
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)  # это рег. выражение находит все тэги
    regScript = re.compile('<script>.*?</script>', flags=re.U | re.DOTALL) # все скрипты
    regComment = re.compile('<!--.*?-->', flags=re.U | re.DOTALL)  # все комментарии


    clean_t = regScript.sub("", t)
    clean_t = regComment.sub("", clean_t)
    clean_t = regTag.sub("", clean_t)


    string = html.unescape(clean_t)


    string = string.lower ()
    string = string.split (' ')
    for x in range (len (string)):
        string [x] = string [x].strip ('.,;:!')





    f = open ('C:\\Users\\Настя\\Desktop\\adyghe-unparsed-words.txt', 'r', encoding = 'utf-8')
    forms = f.readlines ()
    f.close ()
    wordlist = []
    for form in forms:
        form = form.strip ()
        if form in string:
            if form not in wordlist:
                wordlist.append (form)


    wordstr = ''
    for w in wordlist:
        wordstr = wordstr + w + '\n'

    f = open ('C:\\Users\\Настя\\Desktop\\wordlist.txt', 'w', encoding = 'utf-8')
    f.write (wordstr)
    f.close ()


def main ():
    f1 = function1 ()

    
if __name__ == '__main__':
    main ()
