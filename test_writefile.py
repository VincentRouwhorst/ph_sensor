import cvs

with open('mycvs.cvs', 'w', newline='') as f:
    fieldnames = ['kolom1', 'kolom2', 'kolom3']
    thewriter = cvs.DictWriter(f, fieldnames=fieldnames)

    thewriter.writeheader()
    for i in range(1, 100):
        thewriter.writerow({'kolom1' : 'eerste', 'kolom2' : 'tweede', 'kolom3' : 'derde'})
