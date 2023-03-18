# Question 02
med={
    "P":"Pediatrics",
    "O":"Othopedics",
    "E": "ENT"
}
ip=input("")
ul=ip.split()
p=ul.count("P")
Pl=ul.count("O")
p2=ul.count("E")
if p>Pl and p>p2:
    print(med["P"])
elif Pl>p and Pl>p2:
    print(med["O"])
else:
    print(med["E"])