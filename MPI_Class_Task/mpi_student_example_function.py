import sys
from random import seed
from random import sample
from mpi4py import MPI
import pandas as pd
import numpy as np
import operator as op

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Declare 5 arrays
Id_list = []
Student_list = []
sub_1 = []
sub_2 = []
sub_3 = []
Total_score = []


def main():
    print("hello world!")
    # for i in range(0, size):
    #     start = i * 25
    #     end = start + 25
    #     a = np.arange(start=start, stop=end, dtype='i')
    #     Id_list.append(a)
    #     # create a random sequence for random integers
    #     sequence = [i for i in range(100)]
    #     # store 25 random numbers into an array
    #     b = np.array(sample(sequence, 25), dtype='i')
    #     c = np.array(sample(sequence, 25), dtype='i')
    #     d = np.array(sample(sequence, 25), dtype='i')
    #     # append each array
    #     sub_1.append(b)
    #     sub_2.append(c)
    #     sub_3.append(d)
    #
    #     subject1 = avg_sub1()
    #     print("The average for Subject 1: ", subject1)


def avg_sub1(sub_1):
    # Average in Subject 1
    # Store the Sums of Subject 1
    sub_1_sum = np.zeros(25, dtype='i')
    # Calculate the Sums of Subject 1
    comm.Reduce(sendbuf=sub_1[rank], recvbuf=sub_1_sum, op=MPI.SUM, root=0)
    # Print the Sums of Subject 1
    if (rank == 0):
        # print("Simple: Subject 1 Sum : " + str(sub_1_sum) + ", from Rank " + str(rank) + "\n")
        # Calculate the average of Subject 1
        sub1_total = np.sum(sub_1_sum)
        sub1_avg = sub1_total / 100
        # print("Subject 1 Average: " + str(sub1_avg) + "\n")
        return sub1_avg


def avg_sub2():
    # Average in Subject 2
    # Store the Sums of Subject 2
    sub_2_sum = np.zeros(25, dtype='i')
    # Calculate the Sums of Subject 2
    comm.Reduce(sendbuf=sub_2[rank], recvbuf=sub_2_sum, op=MPI.SUM, root=0)
    # Print the Sums of Subject 2
    if (rank == 0):
        print("Simple: Subject 2 Sum : " + str(sub_2_sum) + ", from Rank " + str(rank) + "\n")
        # Calculate the average of Subject 2
        sub2_total = np.sum(sub_2_sum)
        sub2_avg = sub2_total / 100
        print("Subject 2 Average: " + str(sub2_avg) + "\n")


def avg_sub3():
    # Average in Subject 3
    # Store the Sums of Subject 3
    sub_3_sum = np.zeros(25, dtype='i')
    # Calculate the Sums of Subject 3
    comm.Reduce(sendbuf=sub_3[rank], recvbuf=sub_3_sum, op=MPI.SUM, root=0)
    # Print the Sums of Subject 3
    if (rank == 0):
        print("Simple: Subject 3 Sum : " + str(sub_3_sum) + ", from Rank " + str(rank) + "\n")
        # Calculate the average of Subject 3
        sub3_total = np.sum(sub_3_sum)
        sub3_avg = sub3_total / 100
        print("Subject 3 Average: " + str(sub3_avg) + "\n")
