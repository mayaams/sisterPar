# DOKUMENTASI IN PREPARATION DITANYAIN BUAT APA APANYA

# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random


# [4/16 4:01 PM] AJI GAUTAMA PUTRADA
#     nah tapi seni paralel kan bukan supaya pekerjaan yang sama bisa dikerjain bareng2
# ​[4/16 4:01 PM] AJI GAUTAMA PUTRADA
#     tapi pekerjaan nya beda2
# ​[4/16 4:01 PM] AJI GAUTAMA PUTRADA
#     makanya diciptakan rank
# ​[4/16 4:01 PM] AJI GAUTAMA PUTRADA
#     jadi ketika empat program serupa jalan bareng, yang membedakan itu cuman rank
# ​[4/16 4:01 PM] AJI GAUTAMA PUTRADA
#     cara manggil rank itu begini
# ​[4/16 4:02 PM] AJI GAUTAMA PUTRADA
#     comm = MPI.COMM_WORLD
# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
# rank = comm.rank
rank = comm.Get_rank()


# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
randomangka = random.randint(1,5)

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    jumlah = 0
    for i in range(1,size):
        data = comm.recv(source=i, tag=11)
        print(data)
        jumlah += data['send']
    print("Jumlah = ",jumlah)
  
 
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    data = {'rank': rank,'dest':0,'send':randomangka}
    comm.send(data, dest=0, tag=11)