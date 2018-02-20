print "Welcome to the CSI forensic program!"
print "This is the found DNA: "

with open ("dna.txt", "r") as dna_file:
    dna = dna_file.read()
    print dna

suspect_characteristics = {}

Eva = {"hair_color": "Brown", "facial_shape": "Oval", "eye_color": "Blue", "gender": "Female", "race": "White"}

Larisa = {"hair_color": "Brown", "facial_shape": "Oval", "eye_color": "Brown", "gender": "Female", "race": "White"}

Matej = {"hair_color": "Black", "facial_shape": "Oval", "eye_color": "Blue", "gender": "Male", "race": "White"}

Miha = {"hair_color": "Brown", "facial_shape": "Square", "eye_color": "Green", "gender": "Male", "race": "White"}

while True:
    start = ""
    while start != "y" and start != "n":
        start = raw_input("Do you want to compare the DNA? (y/n): ")

    if start == "n":
        print "Goodbye!"
        break

while True:

    characteristic1 = "hair_color"

    if "CCAGCAATCGC" in dna:
        suspect_characteristics[characteristic1] = "Black"

    elif "GCCAGTGCCG" in dna:
        suspect_characteristics[characteristic1] = "Brown"

    elif "TTAGCTATCGC" in dna:
        suspect_characteristics[characteristic1] = "Blonde"

    else:
        print "Nothing found!"

    break

while True:

    characteristic2 = "facial_shape"

    if "GCCACGG" in dna:
        suspect_characteristics[characteristic2] = "Square"

    elif "ACCACAA" in dna:
        suspect_characteristics[characteristic2] = "Round"

    elif "AGGCCTCA" in dna:
        suspect_characteristics[characteristic2] = "Oval"

    else:
        print "Nothing found!"

    break

while True:

    characteristic3 = "eye_color"

    if "TTGTGGTGGC" in dna:
        suspect_characteristics[characteristic3] = "Blue"

    elif "GGGAGGTGGC" in dna:
        suspect_characteristics[characteristic3] = "Green"

    elif "AAGTAGTGAC" in dna:
        suspect_characteristics[characteristic3] = "Brown"

    else:
        print "Nothing found!"

    break

while True:

    characteristic4 = "gender"

    if "TGAAGGACCTTC" in dna:
        suspect_characteristics[characteristic4] = "Female"

    elif "TGCAGGAACTTC" in dna:
        suspect_characteristics[characteristic4] = "Male"

    else:
        print "Nothing found!"

    break

while True:
    characteristic5 = "race"

    if "AAAACCTCA" in dna:
        suspect_characteristics[characteristic5] = "White"

    elif "CGACTACAG" in dna:
        suspect_characteristics[characteristic5] = "Black"

    elif "CGCGGGCCG" in dna:
        suspect_characteristics[characteristic5] = "Asian"

    else:
        print "Nothing found!"

    break

if suspect_characteristics == Eva:
    print "Eva is the criminal!"

elif suspect_characteristics == Larisa:
    print "Tim is the criminal!"

elif suspect_characteristics == Matej:
    print "Matej is the criminal!"

elif suspect_characteristics == Miha:
    print "Miha is the criminal!"