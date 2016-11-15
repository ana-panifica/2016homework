

from flask import Flask
from flask import url_for, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():

    if request.args:
        name = request.args['name']
        language = request.args['language']
        sex = request.args['sex']
        age = request.args['age']
        town = request.args['town']
        lisa = request.args['lisa']
        vetka = request.args['vetka']
        tsveti = request.args['tsveti']
        platie = request.args['platie']
        apelsin = request.args['apelsin']
        solntse = request.args['solntse']
        ibis = request.args['ibis']
        tsvetok = request.args['tsvetok']
        maki = request.args['maki']
        rabina = request.args['rabina']
        parusa = request.args['parusa']
        lenta = request.args['lenta']
        comment = request.args['comment']
        f = open ('C:\\Users\\Настя\\Desktop\\Flask\\templates\\stat.csv', 'a', encoding = 'utf-8')
        f.write(name + '\t' + language + '\t' + sex + '\t' + age + '\t' + town + '\t' + lisa + '\t' + vetka + '\t' + tsveti
                 + '\t' + platie + '\t' + apelsin + '\t' + solntse + '\t' + ibis + '\t' +
                tsvetok + '\t' + maki + '\t' + rabina + '\t' + parusa + '\t' +
                lenta + '\t' + comment + '\n')
        f.close()

           
        return render_template('thanks1.html', name=name)


    return render_template('index.html')

@app.route('/stats')
def stats():
    with open("C:\\Users\\Настя\\Desktop\\Flask\\templates\\stat.csv", "rt", encoding = 'utf-8') as f:
        tmp = [line.strip('\n').split('\t') for line in f]
        ora_ryz = []
        vsego = len (tmp)
        ryz_arr = {}
        t = 1
        for n in range (5, 11):
            orange = 0
            ryz = 0
            for i in range (0, len(tmp)):
                word = tmp[i][n]
                if word.startswith('рыж'):
                    ryz += 1
                else:
                    orange += 1
            prryz = round(ryz/(0.01*len(tmp)))
            ryz_arr [t] = prryz
            t += 1
        kr_arr = {}
        t = 1
        for n in range (11, 17):
            kras = 0
            al = 0
            for i in range (0, len(tmp)):
                word = tmp[i][n]
                if word.startswith('красн'):
                    kras += 1
                else:
                    al += 1
            prkras = round(kras/(0.01*len(tmp)))
            kr_arr [t] = prkras
            t += 1


    return render_template('stats.html', vsego=vsego, rlisa = ryz_arr[1], olisa = 100 - ryz_arr[1], rvetka = ryz_arr[2], ovetka = 100 - ryz_arr [2],
                           rtsveti = ryz_arr[3], otsveti = 100 - ryz_arr[3], rplatie = ryz_arr[4], oplatie = 100 - ryz_arr[4],
                           rapelsin = ryz_arr[5], oapelsin = 100 - ryz_arr[5], rsolntse = ryz_arr[6], osolntse = 100 - ryz_arr[6],
                           kibis = kr_arr[1], aibis = 100 - kr_arr[1], ktsvetok = kr_arr[2], atsvetok = 100 - kr_arr[2],
                           kmaki = kr_arr[3], amaki = 100 - kr_arr[3], krabina = kr_arr[4], arabina = 100 - kr_arr[4],
                           kparusa = kr_arr[5], aparusa = 100 - kr_arr[5], klenta = kr_arr[6], alenta = 100 - kr_arr[6])


@app.route('/search')
def search():

    if request.args:
        sword = request.args['sword']
        rus = True if 'rus' in request.args else False
        if sword == '':
            sword = 'None'
        return redirect(url_for('results', sword=sword, rus=rus))


    return render_template('search.html')

@app.route('/results/<sword>/<rus>')
def results(sword, rus):
    a = False
    meta = {}
    n = 0
    with open("C:\\Users\\Настя\\Desktop\\Flask\\templates\\stat.csv", "rt", encoding = 'utf-8') as f:
        tmp = [line.strip('\n').split('\t') for line in f]
       
        for line in tmp:
            b = False
            if rus == 'False':
                for word in line:
                    if word == sword:
                        a = True
                        b = True
                        i = 0
                        metastr = ''
                        while i <= 4:
                            metastr = metastr + line [i] + ', '
                            i += 1
                if b == True:
                    meta[n] = metastr
                n += 1
            else:
                if line [1] == 'русский':
                    for word in line:
                        if word == sword:
                            a = True
                            b = True
                            i = 0
                            metastr = ''
                            while i <= 4:
                                metastr = metastr + line [i] + ', '
                                i += 1
                    if b == True:
                        meta[n] = metastr
                    n += 1  
      
    if sword == 'None':
        meta[0] = 'Вы задали пустой запрос.'
        return render_template('results.html', meta=meta, sword=sword)
    if a == False:
        meta[0] = 'Нам ничего не удалось найти. Либо этого словосочетания нет в анкете, либо никто из информантов не выбрал его в качестве более правильного варианта.'
        return render_template('results.html', meta=meta, sword=sword)
    else:
        return render_template('results.html', meta=meta, sword=sword)

    
@app.route('/json')
def json_string():
    with open("C:\\Users\\Настя\\Desktop\\Flask\\templates\\stat.csv", "rt", encoding = 'utf-8') as f:
        tmp = [line.strip('\n').split('\t') for line in f]
        json_string = json.dumps(tmp)
        json_ideal = json_string.encode("cp1251")


    return json_ideal
        

if __name__ == '__main__':
    app.run(debug=True)
