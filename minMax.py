#MISD (min max)
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

data = []

#nilai tatul if 41 10
data_stream = [31.50, 79.00, 79.00, 76.50, 51.78, 87.71, 86.26, 81.15, 84.63, 82.33, 64.10, 83.01, 94.53, 87.71, 90.35, 79.40, 93.00, 82.33, 86.30, 89.91, 94.53]

def instruksiMax(data):
    max = data[0]
    for i in range(len(data)-1):
        if (data[i+1] > max):
            max = data[i+1]
    return max

def instruksiMin(data):
    min = data[0]
    for i in range(len(data)-1):
        if (data[i+1] < min):
            min = data[i+1]
    return min

#cek algo min max
#m = instruksiMax(data_stream)
#n = instruksiMin(data_stream)
#print(m,n)
