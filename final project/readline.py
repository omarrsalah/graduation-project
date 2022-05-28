with open('Man_city.docx') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)