print "Welcome to the CSI forensic program!"
print "This is the found DNA: "

with open ("dna.txt", "r") as dna_file:
    dna = dna_file.read()
    print dna

while True:
    start = ""
    while start != "y" and start != "n":
        start = raw_input("Do you want to compare the DNA? (y/n): ").lower()

    if start == "n":
        print "Goodbye!"
        break

traits = {
    "hair_color": {
        "CCAGCAATCGC": "Black",
        "GCCAGTGCCG": "Brown",
        "TTAGCTATCGC": "Blonde"
    }

    "facial_shape": {
        "GCCACGG": "Sqaure"
        "ACCACAA": "Round"
        "AGGCCTCA": "Oval"
    }
}

for trait_name, dna_mapping in traits.iteritems():
    for dna_fragment, pheno_type in hair_color.iteritems()

        if dna_fragment in DNA_file:
            profile_dict["hair_color"] = pheno_type