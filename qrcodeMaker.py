import qrcode

adat = 'mi legyen benne'

kep = qrcode.make(adat)

kep.save('hol legyen')
print('kész')