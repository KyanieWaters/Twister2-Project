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

SIZE = 25


def maximum_pos(a, n):
    maxpos = a.index(max(a))
    print("The max number is at position ", maxpos + 1)


def largest(arr, n):
    return max(arr)


# if rank == 0:
#     print(rank + " qqqq")

for i in range(0, size):
    start = i * 25
    end = start + 25
    a = np.arange(start=start, stop=end, dtype='i')
    Id_list.append(a)
    # maximum_pos(a, 33)
    # create a random sequence for random integers
    sequence = [i for i in range(100)]
    # store 25 random numbers into an array
    b = np.array(sample(sequence, 25), dtype='i')
    c = np.array(sample(sequence, 25), dtype='i')
    d = np.array(sample(sequence, 25), dtype='i')
    # append each array
    sub_1.append(b)
    sub_2.append(c)
    sub_3.append(d)

    # np.arange()

# The top of the class
y = np.add(b, c, d)
print(y.shape)
# print("The Total score of subjects combined for each student: " + str(y))
Total_score_max_values = np.zeros(25, dtype='i')
comm.Reduce(sendbuf=y, recvbuf=Total_score_max_values, op=MPI.MAX, root=0)
if (rank == 0):
    print("Simple: Total Score Max : " + str(Total_score_max_values) + ", from Rank " + str(rank) + "\n")
# n = len(Total_score)
# print("This is the Total Score: ", Total_score)
# print(largest(Total_score, n))
# Class_best_score = max(Total_score)

# print("The highest score in the Class: ", Class_best_score)


# Student ID's
for i in range(0, 100):
    Student_list.append("id_" + str(i))
# print(Student_list)


# Maximum scored student in Subject1
sub1_max_values = np.zeros(25, dtype='i')
comm.Reduce(sendbuf=sub_1[rank], recvbuf=sub1_max_values, op=MPI.MAX, root=0)
print(sub1_max_values)
m = max(sub1_max_values)
# # max_pos = sub1_max_values.index(max(sub1_max_values))
# print(m)
# # print(max_pos)
# # pos = maximum_pos(sub1_max_values, len(sub1_max_values))
# # print(pos)
if (rank == 0):
    print("Simple: Subject 1 Max : " + str(m) + ", from Rank " + str(rank) + "\n")

# Average in Subject 1
# Store the Sums of Subject 1
sub_1_sum = np.zeros(25, dtype='i')
# Calculate the Sums of Subject 1
comm.Reduce(sendbuf=sub_1[rank], recvbuf=sub_1_sum, op=MPI.SUM, root=0)
# Print the Sums of Subject 1
if (rank == 0):
    # print("Simple: Subject 1 Sum : " + str(sub_1_sum) + ", from Rank " + str(rank) + "\n")
    # Calculate the average of Subject 1
    sub1_Total = np.sum(sub_1_sum)
    sub1_Avg = sub1_Total / 100
    # print("Subject 1 Average: " + str(sub1_Avg) + "\n")

# Average in Subject 2
# Store the Sums of Subject 2
sub_2_sum = np.zeros(25, dtype='i')
# Calculate the Sums of Subject 2
comm.Reduce(sendbuf=sub_2[rank], recvbuf=sub_2_sum, op=MPI.SUM, root=0)
# Print the Sums of Subject 2
if (rank == 0):
    # print("Simple: Subject 2 Sum : " + str(sub_2_sum) + ", from Rank " + str(rank) + "\n")
    # Calculate the average of Subject 2
    sub2_Total = np.sum(sub_2_sum)
    sub2_Avg = sub2_Total / 100
    # print("Subject 2 Average: " + str(sub2_Avg) + "\n")

# Average in Subject 3
# Store the Sums of Subject 3
sub_3_sum = np.zeros(25, dtype='i')
# Calculate the Sums of Subject 3
comm.Reduce(sendbuf=sub_3[rank], recvbuf=sub_3_sum, op=MPI.SUM, root=0)
# Print the Sums of Subject 3
if (rank == 0):
    # print("Simple: Subject 3 Sum : " + str(sub_3_sum) + ", from Rank " + str(rank) + "\n")
    # Calculate the average of Subject 3
    sub3_Total = np.sum(sub_3_sum)
    sub3_Avg = sub3_Total / 100
    # print("Subject 3 Average: " + str(sub3_Avg) + "\n")
