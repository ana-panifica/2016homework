from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()
import json

def make_arr ():
    f = open ('1grams-3.txt', 'r', encoding = 'utf-8')
    string = f.read()
    string = string.split ('\n')
    f.close ()
    arr = []
    for word in string:
        a = word.split ('\t')
        arr.append (a[-1])
    print (arr)
    return arr

def parsing_arr (arr):
    gramrazbs = {}
    gramrazb = ''
    for a in arr:
        ana = morph.parse(a)
        first = ana[0]
        print (a)
        print(first.tag)
        lemma = first.normal_form
        gramm = str(first.tag)
        if ' ' in gramm:
            grammarr = gramm.split (' ')
            gramrazb = grammarr [-2]
        else:
            gramrazb = gramm
        if gramrazb not in gramrazbs:
            aarr = []
            aarr.append (lemma)
            gramrazbs [gramrazb] = aarr
            
        else:
            if lemma not in gramrazbs[gramrazb]:
                gramrazbs[gramrazb].append (lemma)
    print (gramrazbs)
    return (gramrazbs)

def writing_arr (gramrazbs):
    grams = json.dumps (gramrazbs)
    f = open ('grams.txt', 'w', encoding = 'utf-8')
    f.write(grams)
    f.close ()
 
def main ():
    f1 = make_arr ()
    f2 = parsing_arr (f1)
    f3 = writing_arr (f2)

if __name__ == '__main__':
    main ()
