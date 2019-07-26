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


for i in range(0, size):
    start = i * 25
    end = start + 25
    a = np.arange(start=start, stop=end, dtype='i')
    Id_list.append(a)
    # print(a)
    # create a random sequence for random integers
    sequence = [i for i in range(100)]
    # store 25 random numbers into an array
    b = np.array(sample(sequence, 25), dtype='i')
    c = np.array(sample(sequence, 25), dtype='i')
    d = np.array(sample(sequence, 25), dtype='i')
    # print(b)
    # print("This is array b: ", b)
    # append each array
    sub_1.append(b)
    sub_2.append(c)
    sub_3.append(d)
    y = np.add(b, c, d)
    # print(y)
    # maxElement = np.max(y)
    # # Total_score.append(maxElement)
    # print("The max element from the array: ", maxElement)
    # # print("These are the max numbers from each array: ", Total_score)
    # # highest_value = np.max(Total_score)
    # # print("The highest Score is: ", highest_value)
    # index_result = np.where(y == np.max(y))
    # print("The list of indices of max elements: ", index_result[0])


for i in range(0, 100):
    Student_list.append("id_" + str(i))

# print(Student_list)


# Maximum scored student in Subject1
print(sub_1)

max_score_Sub1 = np.max(sub_1)
print("The max score in Subject 1 is: ", max_score_Sub1)
sub1_max_index = np.where(sub_1 == np.max(sub_1))
print("The list of indices of max elements: ", sub1_max_index[0])
