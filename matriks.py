def cetak_matriks(matriks):
    for row in matriks:
        print (row)
 
def jumlahkan_matriks(matriks_a, matriks_b):
    temp_row = []
    matriks_ab= []

    for i in range(0,len(matriks_a)):
        for j in range(0,len(matriks_a[0])):
            temp_row.append(matriks_a[i][j] + matriks_b[i][j])
        matriks_ab.append(temp_row)
        temp_row = []
    return matriks_ab
matriks_a = [[1, 2, 3, 5], [1, 2, 3, 5], [1, 2, 3, 5]]
matriks_b = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 
print ("matriks_a : ")
cetak_matriks(matriks_a)
 
print ("\nmatriks_b : ")
cetak_matriks(matriks_b)
 
print ("\nhasil penjumlahan :")
hasil = jumlahkan_matriks(matriks_a, matriks_b)
cetak_matriks(hasil)