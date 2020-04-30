#KELOMPOK SANTUY IF 41 10

#MISD (min max)
#menggunakan 1 pool data dan 2 pool intruksi

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

data = []

#POOL DATA
data_stream = [31.50, 79.00, 79.00, 76.50, 51.78, 87.71, 86.26, 81.15, 84.63, 82.33, 64.10, 83.01, 94.53, 87.71, 90.35, 79.40, 93.00, 82.33, 86.30, 89.91, 94.53]

#POOL INTRUKSI 1
def instruksiMax(data):
    max = data[0]
    for i in range(len(data)-1):
        if (data[i+1] > max):
            max = data[i+1]
    return max

#POOL INTRUKSI 2
def instruksiMin(data):
    min = data[0]
    for i in range(len(data)-1):
        if (data[i+1] < min):
            min = data[i+1]
    return min

#cek algo min=31.5 max=94.53
#m = instruksiMax(data_stream)
#n = instruksiMin(data_stream)
#print(m,n)

if rank == 0: #mengirim data min max
    dmax = instruksiMax(data_stream)
    dmin = instruksiMin(data_stream)
    comm.send(dmax, dest=1, tag=1)
    comm.send(dmin, dest=1, tag=2)
if rank == 1: #menerima data min max
    datax = comm.recv(source=0, tag=1)
    datan = comm.recv(source=0, tag=2)
    print('Rank',rank,',','nilai maks = ',datax)
    print('Rank',rank,',','nilai min = ',datan)
