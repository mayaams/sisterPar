#KELOMPOK SANTUY IF 41 10

# SIMD (penjumlahan matrix)
#menggunakan 4 pool data dan 1 pool intruksi

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

data_stream1 = [[1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2]] #POOL DATA 1
data_stream2 = [[3, 3, 4, 4], [3, 3, 4, 4], [3, 3, 4, 4]] #POOL DATA 2
data_stream3 = [[2, 2, 3, 3], [2, 2, 3, 3], [2, 2, 3, 3]] #POOL DATA 3
data_stream4 = [[1, 1, 7, 7], [1, 1, 7, 7], [1, 1, 7, 7]] #POOL DATA 4

def cetak_matriks(matriks):
    for row in matriks:
        print (row)

#POOL INTRUKSI
def intruksiJumMatriks(matriks_a, matriks_b):
    temp_row = []
    matriks_ab= []

    for i in range(0,len(matriks_a)):
        for j in range(0,len(matriks_a[0])):
            temp_row.append(matriks_a[i][j] + matriks_b[i][j])
        matriks_ab.append(temp_row)
        temp_row = []
    return matriks_ab


if rank == 0:
    print("A+B=")
    hasil_1 = intruksiJumMatriks(data_stream1, data_stream2)
    cetak_matriks(hasil_1)

if rank == 1:
    print("C+D=")
    hasil_2 = intruksiJumMatriks(data_stream3, data_stream4)
    cetak_matriks(hasil_2)
