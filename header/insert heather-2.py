
def WriteHeader2(filename, header):
    # Always writes the header.
    file = open(filename, 'r')
    # remove any matching 'header' from the file, in case ther are duplicate header rows in the wrong places
    lines = [line for line in file if not line == header]
    file.close()

    # rewrite the file, appending the header to row 1
    file = open(filename, 'w')
    file.write(''.join([line for line in lines].insert(0,header)))
    file.close()