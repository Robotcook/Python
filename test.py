DNA_file = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

profile_dict = {}

Eva = {
    "hair_color": "Brown",
    "facial_shape": "Oval",
    "eye_color": "Blue",
    "gender": "Female",
    "race": "White",
}

Larisa = {
    "hair_color": "Brown",
    "facial_shape": "Oval",
    "eye_color": "Brown",
    "gender": "Female",
    "race": "White",
}

Matej = {
    "hair_color": "Black",
    "facial_shape": "Oval",
    "eye_color": "Blue",
    "gender": "Male",
    "race": "White",
}

Miha = {
    "hair_color": "Brown",
    "facial_shape": "Square",
    "eye_color": "Green",
    "gender": "Male",
    "race": "White",
}

while True:
    indicator1 = "hair_color"

    if "CCAGCAATCGC" in DNA_file:
        profile_dict[indicator1] = "Black"

    elif "GCCAGTGCCG" in DNA_file:
        profile_dict[indicator1] = "Brown"

    elif "TTAGCTATCGC" in DNA_file:
        profile_dict[indicator1] = "Blonde"

    else:
        print "No match found"

    break

while True:
    indicator2 = "facial_shape"

    if "GCCACGG" in DNA_file:
        profile_dict[indicator2] = "Square"

    elif "ACCACAA" in DNA_file:
        profile_dict[indicator2] = "Round"

    elif "AGGCCTCA" in DNA_file:
        profile_dict[indicator2] = "Oval"

    else:
        print "No match found"

    break

while True:
    indicator3 = "eye_color"

    if "TTGTGGTGGC" in DNA_file:
        profile_dict[indicator3] = "Blue"

    elif "GGGAGGTGGC" in DNA_file:
        profile_dict[indicator3] = "Green"

    elif "AAGTAGTGAC" in DNA_file:
        profile_dict[indicator3] = "Brown"

    else:
        print "No match found"

    break

while True:
    indicator4 = "gender"

    if "TGAAGGACCTTC" in DNA_file:
        profile_dict[indicator4] = "Female"

    elif "TGCAGGAACTTC" in DNA_file:
        profile_dict[indicator4] = "Male"

    else:
        print "No match found"

    break

while True:
    indicator5 = "race"

    if "AAAACCTCA" in DNA_file:
        profile_dict[indicator5] = "White"

    elif "CGACTACAG" in DNA_file:
        profile_dict[indicator5] = "Black"

    elif "CGCGGGCCG" in DNA_file:
        profile_dict[indicator5] = "Asian"

    else:
        print "No match found"

    break

if profile_dict == Eva:
    print "Eva is the criminal"

elif profile_dict == Larisa:
    print "Tim is the criminal"

elif profile_dict == Matej:
    print "Matej is the criminal"

elif profile_dict == Miha:
    print "troll is the criminal"