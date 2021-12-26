saniye = int(input(' input saniyeha '))
saat = saniye // 3600
daghigheh =(saniye % saat)// 60
saniye = saniye - saat*3600 - daghigheh*60
if saniye > 60:
    daghigheh =daghigheh + int(saniye / 60)
    saniye =saniye - int(saniye % 60)
elif daghigheh > 60 :
    saat = saat + int(daghigheh / 60)
    daghigheh = daghigheh - int(daghigheh % 60)
print(int(saat) ,":",int(daghigheh),":",int(saniye))
