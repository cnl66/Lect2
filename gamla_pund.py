"""Innan decimalreformen 1971 delades ett pund i tjugo shilling, 
som i sin tur delades i tolv pence, vilket gav totalt 240 pence på ett pund. 

Hur många pund shilling och pence blir antal inmatade pence? 
"""
# // betyder hur många hela gånger går nämnaren i täljaren
# % betyder vad blir resten vid heltalsdivisionen

total_pence = int(input("Ange antal pence: "))
pounds = total_pence // (20*12)
pence_left = total_pence % (20*12)
shilling = pence_left // 12
pence = pence_left % 12

print('"Det blir"', pounds, "pund,", shilling, "shilling och", pence, "pence")
print("\nProgrammet avslutas ... :-)")

# string = "Det blir" + str(pounds) + "pund," + str(shilling)+ "shilling och"+ str(pence) + "pence"
# print(string)
