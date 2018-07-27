from django.shortcuts import render

import requests   # Web からデータを取ってくる時に使う

import bs4        # スクレイピング

import re         # 正規表現によるマッチングを使う



def appmain(request):

#    while True:

        # 表示する各サイトのURLを入れる

    yomiuri = requests.get('https://www.yomiuri.co.jp/latestnews/')
    mainichi = requests.get('https://mainichi.jp/flash/1')
    asahi = requests.get('http://www.asahi.com/news/')
    nikkei = requests.get('http://www.nikkei.com/news/category')
    content_type_encoding = asahi.encoding

    kyodo = requests.get('https://this.kiji.is/-/units/39166665832988672')



        # 「おまかせ表示」に現われたページをスクレイピング

    soupy = bs4.BeautifulSoup(yomiuri.text, "html.parser")
    soupm = bs4.BeautifulSoup(mainichi.text, "html.parser")
    soupa = bs4.BeautifulSoup(asahi.text, "html.parser",from_encoding='Shift_JIS')
    soupn = bs4.BeautifulSoup(nikkei.text, "html.parser")


        # この Wiki エントリのタイトルの文字列を変数 title に代入

    ytitle1 = soupy.select('.headline')[0].getText
    ytitle2 = soupy.select('.headline')[1].getText
    ytitle3 = soupy.select('.headline')[2].getText
    mtitle1 = soupm.select('.midashi')[0].getText
    mtitle2 = soupm.select('.midashi')[1].getText
    mtitle3 = soupm.select('.midashi')[2].getText
    atitle1 = soupa.select('.SW')[0].getText
    atitle2 = soupa.select('.SW')[1].getText
    atitle3 = soupa.select('.SW')[2].getText
    ntitle1 = soupn.select('.m-miM09_titleL')[0].getText
    ntitle2 = soupn.select('.m-miM09_titleL')[1].getText
    ntitle3 = soupn.select('.m-miM09_titleL')[2].getText
    #for i in ['1','2','3','4']:
    #    li = ytitle_index.find('li',attrs={'class': 'no'+i})
    #    a = li.find('a')

        #ytitle_spam = a.find('spam', attrs={'class': 'headline'})
        #ytitle.append([ytitle_spam.contents[0],a.get('href')])




        # この Wiki エントリのトップにある説明文だけ取り出して変数 description に代入

        #description = soup.select('div.mw-parser-output p')[0].getText()



        # ( ) 内に答えにつながる言葉があるエントリが多いので，( ) は取り除いてしまう．最短マッチが重要

        #description2 = re.sub(r"（.*?）", ' ', description)



        # 答えに当たる部分を ◯ で置き換える．文字数が同じなのはヒントのため

        #description3 = description2.replace(title, '◯' * len(title))



        # 答えが置き換わったときだけクイズにする

        #if description2 != description3:

            #break



    # demo/main.hml に値を渡す

    return render(request, 'demo/main.html', {

        'yomiuri1' : ytitle1,
        'yomiuri2' : ytitle2,
        'yomiuri3' : ytitle3,
        'mainichi1' : mtitle1,
        'mainichi2' : mtitle2,
        'mainichi3' : mtitle3,
        'asahi1' : atitle1,
        'asahi2' : atitle2,
        'asahi3' : atitle3,
        'nikkei1' : ntitle1,
        'nikkei2' : ntitle2,
        'nikkei3' : ntitle3,

        #'descr' : description3,

    })
