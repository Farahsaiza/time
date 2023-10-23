T=float(input("taper le temps en secondes"))
J=T // 86400
J1= T%86400
H=J1 // 3600 
H1=J1%3600
M=H1 // 60
S=H1%60
print(J,"jour",H,"Heure",M,"Minute",S,"seconde")
