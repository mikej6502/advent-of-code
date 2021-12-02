def read_input(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data