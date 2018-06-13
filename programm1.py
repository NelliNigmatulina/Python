var = "i", "SOC", "Elbas", "FCRN"
a = 25; b = 85; c = 35; d = 70; f = 35; g = 80          #a,b - SOC; c,d - Elspot market, f,g - FCR-N
i = 90; e = 16; h = 16                                 #i = present SOC, e = Elbas

SOC_i=list(range(a,b))
Elbas_e=list(range(c,d))
FCRN_h = list(range(f,g))
if i in SOC_i or i>b:                       #Check SOC  LOOP
    print("Battery SOC =", i)
else:
    i < a                                 # If SOC is low => check the power output from the panels
    print("Battery SOC =", i)                  # or prices on the Elspot
                                                    # or prices on the FCR-N     LOOP
if e in Elbas_e:
    print("Elbas price =", e)
elif e<c and h in FCRN_h:                               #If the price on the Elspot is LOW and on the FCR-N is in a range => FCR-N
    print("FCR-N price =", h)
elif e>c and h in FCRN_h:                                   #If the price on the ELspot is HIGH, but on the FCR-N is in a range => FCR-N
    print("FCR-N price =", h)








