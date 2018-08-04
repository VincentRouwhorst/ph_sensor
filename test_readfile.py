import cvs

with open('mycvs.cvs', 'r') as csv_file:
    cvs_reader = cvs.reader(csv_file)

    for line in cvs_reader:
        print(line)
