import statistics as s #agar tidak selalu mengetik statistics
from statistics import  variance as v #jika hanya ingin menggunakan satu fungsi pada module
#from statistics import * ->contoh mengimport semua fungsi pada module
data = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
hasilrata = s.mean(data)
hasilmedian = s.median(data)
hasilvarian = v(data)
hasilstandardeviasi = s.stdev(data)

print(hasilrata)
print(hasilmedian)
print(hasilvarian)
print(hasilstandardeviasi)