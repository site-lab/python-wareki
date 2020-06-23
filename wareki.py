import datetime
now = datetime.date.today()
#now = datetime.date(2000,2,29)

# 令和の開始日
reiwa_year = datetime.date(2019,5,1)
#平成の開始日
heisei_year = datetime.date(1989,1,8)
#昭和の開始日
showa_year = datetime.date(1926,12,25)

now_month = now.month
now_day = now.day


if now >= reiwa_year:
     #令和の和暦を計算。下二桁から18を引くことで令和になる
     reiwa = now.year % 100 - 18 #100で割ることで下二桁出す。
     now = now.strftime('%Y年%m月%d日')
     if reiwa == 1:
         reiwa = "元"

     print("{}を和暦にすると令和{}年{}月{}日です".format(now,reiwa,now_month,now_day))

elif now >= heisei_year:
    #平成の和暦を計算。西暦下二桁から12を足す
    heisei = now.year % 100 + 12 #100で割ることで下二桁出す。
    now = now.strftime('%Y年%m月%d日')
    if heisei == 1:
        heisei = "元"
    print("{}を和暦にすると平成{}年{}月{}日です".format(now,heisei,now_month,now_day))

elif now >= showa_year:
    #昭和の和暦を計算。西暦下二桁から25を引く
    showa = now.year % 100 - 25 #100で割ることで下二桁出す。
    now = now.strftime('%Y年%m月%d日')
    if showa == 1:
        showa = "元"
    print("{}を和暦にすると昭和{}年{}月{}日です".format(now,showa,now_month,now_day))
else:
    print("令和、平成、昭和ではない和暦となります。")
