from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

data_stream1 = [[1, 1, 2, 2],
                [1, 1, 2, 2], 
                [1, 1, 2, 2]] #POOL DATA 1
                
data_stream2 = [[3, 3, 4, 4], 
                [3, 3, 4, 4], 
                [3, 3, 4, 4]] #POOL DATA 2


temp = [[0, 0, 0, 0]]

for i in range (0,4):
    temp[0][i] = data_stream1[rank][i] + data_stream2[rank][i]

hasil = comm.reduce(temp, op=MPI.SUM, root=0)

if rank==0:
    print("Hasil Transpose",hasil)

