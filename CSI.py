print "Welcome to the CSI forensic program!"
print "This is the found DNA: "

with open ("dna.txt", "r") as dna_file:
    dna = dna_file.read()
    print dna

suspect_characteristics = {}

Eva = {"hair_color": "Brown", "facial_shape": "Oval", "eye_color": "Blue", "gender": "Female", "race": "White"}

Larisa = {"hair_color": "Brown", "facial_shape": "Round", "eye_color": "Green", "gender": "Female", "race": "White"}

Matej = {"hair_color": "Black", "facial_shape": "Oval", "eye_color": "Blue", "gender": "Male", "race": "White"}

Miha = {"hair_color": "Brown", "facial_shape": "Square", "eye_color": "Green", "gender": "Male", "race": "White"}

while True:
    start = ""
    while start != "y" and start != "n":
        start = raw_input("Do you want to compare the DNA? (y/n): ").lower()

    if start == "n":
        print "Goodbye!"
        break

    if "CCAGCAATCGC" in dna:
        suspect_characteristics["hair_color"] = "Black"

    elif "GCCAGTGCCG" in dna:
        suspect_characteristics["hair_color"] = "Brown"

    elif "TTAGCTATCGC" in dna:
        suspect_characteristics["hair-color"] = "Blonde"

    else:
        print "Nothing found!"

    break

while True:

    if "GCCACGG" in dna:
        suspect_characteristics["facial_shape"] = "Square"

    elif "ACCACAA" in dna:
        suspect_characteristics["facial_shape"] = "Round"

    elif "AGGCCTCA" in dna:
        suspect_characteristics["facial_shape"] = "Oval"

    else:
        print "Nothing found!"

    break

while True:

    if "TTGTGGTGGC" in dna:
        suspect_characteristics["eye_color"] = "Blue"

    elif "GGGAGGTGGC" in dna:
        suspect_characteristics["eye_color"] = "Green"

    elif "AAGTAGTGAC" in dna:
        suspect_characteristics["eye_color"] = "Brown"

    else:
        print "Nothing found!"

    break

while True:

    if "TGAAGGACCTTC" in dna:
        suspect_characteristics["gender"] = "Female"

    elif "TGCAGGAACTTC" in dna:
        suspect_characteristics["gender"] = "Male"

    else:
        print "Nothing found!"

    break

while True:

    if "AAAACCTCA" in dna:
        suspect_characteristics["race"] = "White"

    elif "CGACTACAG" in dna:
        suspect_characteristics["race"] = "Black"

    elif "CGCGGGCCG" in dna:
        suspect_characteristics["race"] = "Asian"

    else:
        print "Nothing found!"

    break

print "The characteristics of the criminal are: "
print suspect_characteristics

if suspect_characteristics == Eva:
    print "Eva is the criminal!"

elif suspect_characteristics == Larisa:
    print "Larisa is the criminal!"

elif suspect_characteristics == Matej:
    print "Matej is the criminal!"

elif suspect_characteristics == Miha:
    print "Miha is the criminal!"

