LBS=int(input("What is the patient's weight?" ))
KG=(LBS/2.2)
MG=int(input("What is the tablet strength?" ))
SIG= int(input("How many times a day is the dose?" ))
DOSE=(MG*SIG)
DAILY=(DOSE/KG)
print ( round (DAILY, 1))





