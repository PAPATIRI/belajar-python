Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> var x = "sekolah"
SyntaxError: invalid syntax
>>> x = "sekolah"
>>> y = "koding"
>>> print(x+""+y)
sekolahkoding
>>> x.capitalize()
'Sekolah'
>>> print(x.capitalize)
<built-in method capitalize of str object at 0x033B7940>
>>> print(x.capitalize()+""+y)
Sekolahkoding
>>>  print(x.capitalize()+" "+y)
SyntaxError: unexpected indent
>>> print(x.capitalize()+" "+y)
Sekolah koding
>>> x.replace("sekolah","rumah")
'rumah'
>>> print(x.replace("sekolah","rumah")+" "+y)
rumah koding
>>> harga = 2500
>>> print("tptal harganya", harga)
tptal harganya 2500
>>> print("total harganya"+str(harga))
total harganya2500
>>> print("total harganya"+""+str(harga))
total harganya2500
>>> print("total harganya"+" "+str(harga))
total harganya 2500
>>> q = "3"
>>> print(x+int(q))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(x+int(q))
TypeError: can only concatenate str (not "int") to str
>>> w = 20
>>> print(int(q)+w)
23
>>> 
