import sys
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

#print(rank, size)

list = []
for i in range(0, 4):
    start = i * 4
    end = start + 4
    a = np.arange(start=start, stop=end, dtype='i')
    list.append(a)


print("Simple: Input :", list[rank] ," From Rank : " + str(rank))


# # initialize the numpy arrays that store the results from reduce operation
output_sum = np.array([0,0,0,0], dtype='i')

# # perform reduction based on sum and maximum
comm.Reduce(sendbuf=list[rank], recvbuf=output_sum, root=1, op=MPI.MAX)
#comm.Allreduce([list[rank],'i'], [output_sum, 'i'], op=MPI.MIN)

#if (rank == 0):
#   print("Simple: Output Sum : " + str(output_sum) + ", from Rank " + str(rank) + "\n")

print("Simple: Output Sum : " + str(output_sum) + ", from Rank " + str(rank) + "\n")
