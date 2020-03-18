import os
import argparse
from collections import Counter
import random

words = ""
words_dict = dict()
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--task', type=int, metavar='', required=True, help='number of task')
parser.add_argument('-d', '--directory', type=str, help='directory of file')
args = parser.parse_args()


def get_words():
    with open(args.directory, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


def counting():
    print("amount of words: %d" % len(get_words()))
    print("unique words: %d" % len(words_dict))
    print("all used words:")
    for word in words_dict:
        print(word.ljust(20), words_dict[word])


def sentence():
    cnt = Counter(get_words())
    print(cnt.most_common(10))


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


def quicktask():
    str = input("input ur string:\n")
    nums = str.split()
    print(quicksort(nums))


def slicing():
    str = input("input ur string:\n")
    nums = str.split()
    print(merge_sort(nums))


def fibonaccigen(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


def fibonacci():
    print(list(fibonaccigen(int(input("how many fibonacci numbers wanna see?\n")))))


def main():
    if args.task == 1:
        counting()
    elif args.task == 2:
        sentence()
    elif args.task == 3:
        quicktask()
    elif args.task == 4:
        fibonacci()
    elif args.task == 5:
        slicing()
    else:
        print('wrong input')


if __name__ == "__main__":
    main()
