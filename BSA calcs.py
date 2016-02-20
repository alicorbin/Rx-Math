LBS=int(input("What is the patient's weight in lbs?" ))
ADULTDOSE=int(input("What is the adult dose in mg?" ))
KG=(LBS/2.2)
BSA=((4*KG+7)/(KG+90))
CHILDDOSE=(BSA/1.7*ADULTDOSE)
print ("The patient's weight in KG is",round (KG, 1),"kg")
print ("The body surface area of the patient is",round(BSA, 1))
print ("The child dose is",round (CHILDDOSE, 1),"mg")

