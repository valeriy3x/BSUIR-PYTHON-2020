import tempfile
import linecache


def merge_sort(input_file, output):
    if length(input_file) >= 2:
        mid = length(input_file) // 2

        left = tempfile.NamedTemporaryFile('w+')
        right = tempfile.NamedTemporaryFile('w+')
        write_to_file(input_file, left, 0, mid)
        merge_sort(left, left)

        write_to_file(input_file, right, mid, length(input_file))
        merge_sort(right, right)
        i = j = 0
        output.seek(0)

        left_length = length(left)
        right_length = length(right)

        while i < left_length and j < right_length:
            left_number = get_digit_from_file(left, i)
            right_number = get_digit_from_file(right, j)
            if left_number < right_number:
                output.write(str(left_number) + '\n')
                i += 1
            else:
                output.write(str(right_number) + '\n')
                j += 1

        while i < length(left):
            output.write(str(get_digit_from_file(left, i)) + '\n')
            i += 1

        while j < length(right):
            output.write(str(get_digit_from_file(right, j)) + '\n')
            j += 1
        left.close()
        right.close()


def write_to_file(source_file, output_file, from_pos, to_pos):
    for i in range(from_pos+1, to_pos+1):
        output_file.write(linecache.getline(source_file.name, i))


def get_digit_from_file(file, index):
    file.seek(0)
    for i, line in enumerate(file):
        if i == index:
            return int(line)

    return None


def length(file):
    file.seek(0)
    return sum(1 for line in file)


def sort(input_file, output_file):
    try:
        with open(input_file, 'r+') as input_file:
            with open(output_file, 'w+') as output:
                merge_sort(input_file, output)

    except FileNotFoundError:
        print("Incorrect file path")
