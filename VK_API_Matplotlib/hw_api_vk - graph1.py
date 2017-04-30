import requests
import json
import re
import matplotlib.pyplot as plt
from matplotlib import style
import sys
#style.use('ggplot') 


def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)

def length (string):
    num_w = 0
    string = string.split (' ')
    for word in string:
        num_w += 1
    return num_w


def name_id ():
    group_info = vk_api('groups.getById', group_id='academyawards', v='5.63')
    group_id = group_info['response'][0]['id']
    print (group_id)
    return group_id

def download_posts (group_id):
    posts_dict = {}
    posts = []
    ids = []
    item_count = 110

    while len(posts) < item_count:
        result = vk_api('wall.get', owner_id=-group_id, v='5.63', count=100, offset=len(posts))
        posts += result['response']["items"]

    print(len(posts))
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    for p in posts:
        print (p["id"])
        ids.append (p["id"])
        posts_dict [p["id"]] = length (p['text'].translate(non_bmp_map))
        f = open ('C:\\Users\\Настя\\Desktop\\posts.txt', 'a', encoding = 'utf-8')
        f.write(p['text'])
        f.close ()
    for t in ids:
        print (t)
    print (posts_dict)
    
    for i in ids:
        print (i)
    comm_dict = {}
    
    comments = []
    for i in ids:
        comments_zero = []
        result = vk_api('wall.getComments', owner_id=-group_id, post_id=i, v='5.63', count=100)
        comments_count = result['response']['count']
        comments_zero += result['response']['items']
        
        while len(comments_zero) < comments_count:
            result = vk_api('wall.getComments', owner_id=-group_id, v='5.63', post_id=i['id'],count=100, offset=len(comments))
            comments_zero += result['response']["items"]

        comments.append (comments_zero)
        summa = 0
        if len (comments_zero) == 0:
            average = 0
        else:
            for a in comments_zero:
                summa += length (a['text'].translate(non_bmp_map))
            average = summa/len (comments_zero)
        average = round (average)
        comm_dict [i] = average
    print (comm_dict)
    for x in comments:
        f = open ('C:\\Users\\Настя\\Desktop\\comments.txt', 'a', encoding = 'utf-8')
        for y in x:            
            print (y["text"].translate(non_bmp_map))
            f.write(y['text'])
        f.close ()

    print (posts_dict)
    print (comm_dict)

    posts_list = []
    comm_list = []
    for s in posts_dict:
        number = posts_dict[s]
        posts_list.append (number)
    for z in comm_dict:
        number2 = comm_dict[z]
        comm_list.append (number2)
    print (posts_list)
    print (comm_list)

    for w in posts:
        print (w["text"].translate(non_bmp_map))
    for b in comments:
        for c in b:            
            print (c["text"].translate(non_bmp_map))

    plt.scatter(comm_list, posts_list)

    plt.title('Зависимость средней длины комментариев от длины поста')
    plt.ylabel('Длина поста')
    plt.xlabel('Средняя длина комментариев')
    plt.xlim(0,30)
    plt.ylim(0,250)

    plt.show()

def main ():
    
    f1 = name_id ()
    f2 = download_posts (f1)
    
if __name__ == '__main__':
    main ()


