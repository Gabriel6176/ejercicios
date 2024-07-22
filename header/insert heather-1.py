
name = input ("Name: ")
age = input("Age: ")
BirthYear = input("Birth Year: ")
filename = "info.txt"
header = "Name Age Grade\n"

def WriteHeader(filename, header):
    """
    ;param filename: a file path
    ;param header: a string representing the file's "header" row

    This function will check if the header exists in the first line
    and inserts the header if it doesn't exist
    """
    file = open(filename, 'r')
    lines = [line for line in file]
    file.close()
    if lines and lines[0] == header:
        # There are some lines in the file, and first line is the header
        return True
    else:
        # The first line is NOT the header
        file = open(filename, w)
        # Rewrite the file: append header if needed, and all lines which previously were there
        # excluding any misplaced header lines which were not at row 1
        file.write(header + ''.join([line for line in lines if not line == header]))
        file.close()
        return True


if __name__ == '__main__':
    if WriteHeader(filename, header):
        file = open(filename, 'a')
        file.write("{} / {} / {}\n".format(name, age, BirthYear))
        file.close()
    else:
        print('there was some problems...')



