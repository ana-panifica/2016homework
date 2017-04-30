import requests
import json
import re
import matplotlib.pyplot as plt
from matplotlib import style
import sys
#style.use('ggplot') 
from collections import Counter

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

def aver(lst):
    s = 0
    for i in lst:
        s += i
    return round(s / len(lst))

def name_id ():
    group_info = vk_api('groups.getById', group_id='academyawards', v='5.63')
    group_id = group_info['response'][0]['id']
    print (group_id)
    return group_id

def download_posts (group_id):
    posts_dict = {}
    posts = []
    ids = []
    item_count = 100

    while len(posts) < item_count:
        result = vk_api('wall.get', owner_id=-group_id, v='5.63', count=100, offset=len(posts))
        posts += result['response']["items"]


    print(len(posts))
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    for p in posts:
        print (p["id"])
        ids.append (p["id"])
        posts_dict [p["id"]] = length (p['text'].translate(non_bmp_map))
    for t in ids:
        print (t)
    print (posts_dict)
    
    for i in ids:
        print (i)
    comm_dict = {}
    from_ids = {}
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
                if a["from_id"] != -group_id:
                    from_ids [a["from_id"]] = length (a['text'].translate(non_bmp_map))
            average = summa/len (comments_zero)
        average = round (average)
        comm_dict [i] = average
    print (from_ids)
    age = {}
    cities = {}
    city_dict = {}
    for r in from_ids:
        print (r)
        user_info = vk_api('users.get', user_ids=r, fields='city', v='5.63')
        cities [r] = [c["city"]['title'] for c in user_info['response'] 
               if 'city' in c]
        city = cities [r]
        if city != []:
            gorod = str (city[0])
            if gorod not in city_dict:
                dop_list = []
                dop_list.append (from_ids [r])
                city_dict [gorod] = dop_list
            else:
                city_dict[gorod].append (from_ids [r])

        print (city_dict [gorod])
    print (cities)
    print (city_dict)
    
    for e in city_dict:
        city_dict [e] = aver (city_dict [e])
    print (city_dict)

    cities_list = []
    lencom_list = []
    for s in city_dict:
        cities_list.append (s)
        lencom_list.append (city_dict[s])

    print (cities_list)
    print (lencom_list)

    #plt.figure(figsize=(20,10))
    plt.bar(range(len(city_dict)), 
    [city_dict[j] for j in city_dict])
    plt.xticks(range(len(city_dict)), 
    city_dict, 
    rotation='vertical')

    plt.title('Средняя длина поста/комментария в разных городах')
    plt.ylabel('Средняя длина')
    plt.xlabel('Города')

    plt.show()

def main ():
    
    f1 = name_id ()
    f2 = download_posts (f1)
    
if __name__ == '__main__':
    main ()


