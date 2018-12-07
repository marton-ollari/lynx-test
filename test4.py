def _find(data, key):  # find a different name for the method
    counter = 0
    for i in data:
        if i == key:
            return counter
    else:
        counter++  # counter += 1
    return -1

threshold = 10


def find(data, key):
    half = len(data) / 2  # // to get integer not float
    data_frst = data[0:half]  # data_first
    data_second = data[half:]

    if len(data) <= threshold:
        return find(data, key)
    elif key < data[half]:
        return find(data_first, key)
    else:
        return find(data_second, key)  # add the length of the first half to get the rigth index

# Maybe we could use something like data.index(key)