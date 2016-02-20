AD=int(input("What is the adult dose?" ))
CW=int(input("What is the child weight in lbs?" ))
CD= (AD*(CW/150))
print ("The child dose is" , round (CD, 0 ), "mg")