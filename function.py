def contoh_function(no1,no2):
	answer = no1 + no2
	print(answer)
contoh_function(5,5)

# defaul parameter di python
def nomor(n1,n2=2):
	print(n1,n2)
nomor(2) #jika parameter 2 dan sudah ada nilai di salahsatunya
#maka jika di argumen hanya diisi 1, defaultnya akan mengisi ke parameter yang belum ada nilainya

def jendela(width, height, font='NTR',
			bgc='white', scroolbar=True):
	print(width,height,font,scroolbar)
jendela(500,300,bgc='red')
# jika sudah di definisikan nilai parameter, dan ingin mengubahnya maka ubah di argumen dengan menginisialisasi
# ulang saat pemanggilan fungsi, contoh pada parameter bgc diatas


# GLOBAL DAN LOCAL VARIABLE
x = 5 #global variable
def contoh():
	print("ini nilai dari var global :",x)
	print(x+5)
contoh()

y=2
def contoh2():
	globx = x
	print(globx)
	globx +=5
	print(globx)
	return globx
# untuk mengatasi masalah ketika tidak boleh menggunakan "global y"
y = contoh2()
print(y)