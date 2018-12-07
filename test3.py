table = [[1, 5, 7, 10], [3, 13, 14, 15], [6, 16, 19, 25]]

# Sorry, I misread the text and minimized the sum


def min_robot(table):
    length = len(table)
    width = len(table[0])
    sum = 0
    index1 = 0
    index2 = 0
    if width > length:
        for i in range(width-length):
            sum += table[index1][index2]
            index2 += 1
    else:
        for i in range(length-width):
            sum += table[index1][index2]
            index1 += 1

    while (index1 <= length and index2 < width):
        sum += table[index1][index2]
        if index2+1 < width:
            sum += table[index1][index2+1]
        index2 += 1
        index1 += 1
    return sum


def main():
    print(min_robot(table))


if __name__ == '__main__':
    main()
