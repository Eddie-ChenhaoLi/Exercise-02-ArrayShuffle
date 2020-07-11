import random


def generate_array(a, b):
    arr = []
    for i in range(a, b):
        arr.append(i)
    return arr


def shuffle_array(arr):
    return random.shuffle(arr)
