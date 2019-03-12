#variabel pada python
#bersifat case sensitive, harus berawal huruf atau underscore
namadepan = "syarif"
namabelakang = "taufik"
print(namadepan+" "+namabelakang)

#kondisi ifelse dan elif dalam python
nilai = 7
if(nilai>3):
    print("yap nilai benar")
else:
    print("maafkeun aing")


hari = "minggu"
if(hari=="senin"):
    print("kuliah coeg")
elif(hari=="selasa"):
    print("kuliah coeg")
elif(hari=="rabu"):
    print("kuliah coeg")
elif(hari=="kamis"):
    print("kuliah coeg")
elif(hari=="jumat"):
    print("kuliah coeg")
elif(hari=="sabtu"):
    print("kuliah coeg")
elif(hari=="minggu"):
    print("libur coeg")

#loop pda pythom
#while loop, for loop, nested loop
#while
count = 0
while(count<9):
    print("the count is", count)
    count=count+1;
print("goodbye")

#for loop pada python -> kemampuan untuk mengulang item dari urutan apapun
angka=[1,2,3,4,5]
for y in angka:
    print(y)

buah=["nanas","semangka","durian"]
for makanan in buah:
    print(makanan)

#nested loop -> perulangan di dalam perulangan
i=3
while(i<100):
    j=2
    while(j<=(i/j)):
        if not(i%j): break
        j=j+1
    if(j>i/j):
        print (i, "is prime")
        i=i+1
print ("goodbye")

#number pada python
#tipe number pada python = int, float, complex
u=20.0
print(int(u))
print(float(20.0))



