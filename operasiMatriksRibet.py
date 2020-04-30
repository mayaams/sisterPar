from mpi4py import MPI
import random
import time

def create_matrix(n_rows, n_columns):
    matrix = []
    line = []
    element = 0

    while len(matrix) != n_rows:
        n = random.randint(1,99)
        line.append(n)
        element = element + 1


        if len(line) == n_columns:
            matrix.append(line)
            line = []

    return matrix

def create_null_matrix(n_rows, n_columns):
    matrix = []
    line = []
    element = 0

    while len(matrix) != n_rows:
        n = random.randint(1,99)
        line.append(0)
        element = element + 1


        if len(line) == n_columns:
            matrix.append(line)
            line = []

    return matrix

# M1 = matrix 1, M2 = matrix 2, MF = final matrix
# n = size of matrices, beg = beginning of iteration, end = end of iteration
def mult_matrix(m1, m2, mf, n, beg, end):

    # row
    for i in range(beg, end):
        # line
        for k in range(n):
            elem = 0
            # column
            for j in range(n):

                elem = elem + (m1[i][j] * m2[j][k])
                mf[i][k] = elem

def mult_matrix2(m1, m2, mf, n, beg, end, offset):

    # row
    for i in range(beg, end):
        # line
        for k in range(n):
            elem = 0
            # column
            for j in range(n):

                elem = elem + (m1[i][j] * m2[j][k])
                mf[i-offset][k] = elem
            # print(elem)

# getting basic info
comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()


counter = 0;
# print(rank)
if rank == 0:
    print("----START----")
    n = 256
    x = create_matrix(n,n)
    y = create_matrix(n,n)
    z1 = create_null_matrix(128,n)
    start = time.time()
    comm.send(n, dest=1, tag=7)
    comm.send(x, dest=1, tag=7)
    comm.send(y, dest=1, tag=7)
    mult_matrix(x, y, z1, n, 0, 128)
    z2 = comm.recv(source=1, tag=8)
    z = z1+z2
    end = time.time()
    print(end - start)
    print("----END----")
else:
    n = comm.recv(source=0, tag=7)
    x = comm.recv(source=0, tag=7)
    y = comm.recv(source=0, tag=7)
    z = create_null_matrix(128,n)
    mult_matrix2(x, y, z, n, 128, n, 128)
    comm.send(z, dest=0, tag=8)