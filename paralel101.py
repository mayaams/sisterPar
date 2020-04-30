# DOKUMENTASI IN PREPARATION DITANYAIN BUAT APA APANYA
# ini kommunikasi reduction

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


# [4/16 4:06 PM] AJI GAUTAMA PUTRADA
#     kira2 size arti nya apa?
# ​[4/16 4:06 PM] IVAN
#     iya pak munculnya 4 setiap rank
# ​[4/16 4:06 PM] YAZID
#     size itu maksudnya berapa yang sedang jalanin itu juga?
# ​[4/16 4:06 PM] MUCHAMAD
#     jumlah proses paralelnya(?)
# ​[4/16 4:07 PM] AJI GAUTAMA PUTRADA
#     ya...
# ​[4/16 4:07 PM] AJI GAUTAMA PUTRADA
#     jumlah program paralel nya
# ​[4/16 4:07 PM] AJI GAUTAMA PUTRADA
#     sesuai -n yang kita masukin ya


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




///////////////////////////////////////
# KODINGAN PAK AJI
# comment dulu yang atas kalo mau run
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

# for i in range(0,8,2):
# batesnya 8 , stepnya 2
for i in range(rank,8,size):
    print i