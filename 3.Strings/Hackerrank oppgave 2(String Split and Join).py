def split_and_join(line):
    
    line = line.split(" ")
    liney = line
    liney = "-".join(line)
    line = liney
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)