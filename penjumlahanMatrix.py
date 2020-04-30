#KELOMPOK SANTUY IF 41 10
# SIMD (penjumlahan matrix)
#menggunakan 4 pool data dan 1 pool intruksi

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.rank

data_stream1 = numpy.array([[1, 1, 2, 2], [1, 1, 2, 2]]) #POOL DATA 1
data_stream2 = numpy.array([[3, 3, 4, 4], [3, 3, 2, 1]]) #POOL DATA 2

if rank == 0:
    hasil_1 = numpy.add(data_stream1[rank], data_stream2[rank])
    print(hasil_1)


if rank == 1:
    hasil_2 = numpy.add(data_stream1[rank], data_stream2[rank])
    print(hasil_2)