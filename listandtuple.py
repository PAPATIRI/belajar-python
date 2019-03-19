#kita tidak bisa mengubah, edit, delet dll untuk tuple, berlawanan dengan list
#tuple sebagai berikut
x = 2,3,4,5,6
y = (2,3,4,5,6)

#list sebagai berikut
z = [2,3,4,5,6]
#memanggil salah satu elemen pada tuple dan list
print(x[1])
print(y[3])
print(z[2])

#manipulasi pada list

q = [4,3,2,6,8]
#menambahkan elemen pada index terakhir
q.append(3)
print(q)
#menyisipkan elemen pada list
q.insert(2,9) #(no index yang ingin di sisipi, nilai index nya)
print(q)
#menghapaus elemen pada list
q.remove(2)
print(q)
#menghapus akhir index pada list
q.pop()
print(q)
#
q.remove(q[2])
print(q)

