def dna_to_rna(dna):
    rna = ""
    for i in dna:
        if i == "T":
            rna = dna.replace("T","U")
        elif dna.count("T") == 0:
            return dna
    return rna
# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python