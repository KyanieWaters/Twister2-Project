from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

MAX_SCORE_PER_SUB = 100
NUM_OF_STUDENTS = 100
STUDENTS_PER_RANK = NUM_OF_STUDENTS/size

sub1 = np.random.rand(25,)*100
sub2 = np.random.rand(25,)*100
sub3 = np.random.rand(25,)*100

sum_of_sub1 = np.sum(sub1)
sum_of_sub2 = np.sum(sub2)
sum_of_sub3 = np.sum(sub3)

avg_of_sub1 = sum_of_sub1/STUDENTS_PER_RANK
avg_of_sub2 = sum_of_sub2/STUDENTS_PER_RANK
avg_of_sub3 = sum_of_sub3/STUDENTS_PER_RANK

max_score_Sub1 = np.amax(sub1)

if rank == 0:
    print(sub1)
    print(sum_of_sub1)
    print(avg_of_sub1)
    print(max_score_Sub1)

for i in range(0, size):
    a = np.arange(0, STUDENTS_PER_RANK) + STUDENTS_PER_RANK*rank

# print(str(a) + str(rank))





