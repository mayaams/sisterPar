# SIMD (penjumlahan matrix)
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

data_stream1 = [[1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2]]
data_stream2 = [[3, 3, 4, 4], [3, 3, 4, 4], [3, 3, 4, 4]]
data_stream3 = [[2, 2, 3, 3], [2, 2, 3, 3], [2, 2, 3, 3]]
data_stream4 = [[1, 1, 7, 7], [1, 1, 7, 7], [1, 1, 7, 7]]

def cetak_matriks(matriks):
    for row in matriks:
        print (row)

def intruksiJumMatriks(matriks_a, matriks_b):
    temp_row = []
    matriks_ab= []

    for i in range(0,len(matriks_a)):
        for j in range(0,len(matriks_a[0])):
            temp_row.append(matriks_a[i][j] + matriks_b[i][j])
        matriks_ab.append(temp_row)
        temp_row = []
    return matriks_ab

#print ("Matriks A = ")
#cetak_matriks(data_stream1)

#print ("Matriks B = ")
#cetak_matriks(data_stream2)

#print ("Matriks C = ")
#cetak_matriks(data_stream3)

#print ("Matriks D = ")
#cetak_matriks(data_stream4)


if rank == 0:
    print("A+B=")
    hasil_1 = intruksiJumMatriks(data_stream1, data_stream2)
    cetak_matriks(hasil_1)

if rank == 1:
    print("C+D=")
    hasil_2 = intruksiJumMatriks(data_stream3, data_stream4)
    cetak_matriks(hasil_2)
