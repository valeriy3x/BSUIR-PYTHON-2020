import pytest
import os
import random
import ExternalMergeSort.external_merge_sort as external_merge
from pathlib import Path


def create_file(input_file: str, items_list):
    path = Path(__file__).parent / "../Tests/{0}".format(input_file)
    with path.open('w+') as opened:
        for x in items_list:
            opened.writelines('{}\n'.format(x))


def test_sort_file():
    input_file = "input.txt"
    output_file = "output.txt"
    numbers = [random.randint(-1000000, 1000000) for _ in range(5000)]

    create_file(input_file, numbers)

    path_1 = Path(__file__).parent / "../Tests/{0}".format(input_file)
    path_2 = Path(__file__).parent / "../Tests/{0}".format(output_file)

    external_merge.sort(path_1, path_2)

    external_sort_list = []

    with path_2.open('r') as opened:
        external_sort_list = opened.read().replace("\n", " ").strip()
        assert external_sort_list == ' '.join(map(str, sorted(numbers)))
