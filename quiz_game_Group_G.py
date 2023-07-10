intro="Welcome to the Group G pub quiz"
print(intro.center(60,"*"))
name=input("\nInput your name here:")
print("Welcome to the PubG quiz" ,name)

ques = ("\nQ1. In which river runs through Paris? \nA.Seine/ \nB.Mersey/ \nC.Wine \nD.Delta", 
        "\nQ2. What is the Capital of INDIA? \nA. Mumbai \nB.Goa \nC.New Delhi \nD.Chennai",
        "\nQ3. What is the Mother Tongue of Maharashtra State? \nA.Marathi \nB.Telugu \nC.Gujrati \nD.Bengoli", 
        "\nQ4. Most IPL trophies Won by which team? \nA.MumbaiIndians \nB.RoyalChallengerBanglore \nC.ChennaiSuperKings \nD.KolkattaKnightRiders", 
        "\nQ5. Current Most popular programming language in the world? \nA.Java \nB.C++ \nC.JavaScript \nD.Python")

ans = (("C" or "c"), ("C" or "c"), ("A" or "a"), ("A" or"a"),("D" or "d"))
prize=(100,200,300,400,500)
startingAmount=0

for i in range(0, len(ques)):
  print(ques[i])

  Ans = input("Select your Answer OR to Quit press 'Q' : ")
  if (Ans == "Q"):
    print("Thank You for Playing!")
    break
  if Ans == ans[i]:
    print("Correct ! \nYou Won the pricepool of £.",prize[i])
    startingAmount=prize[i]
  else : 
   print("Incorrect ! \nYou lose the Game.")
   break

print("\n\nTotal Amount Won by",name,"is £",startingAmount)
# if(i==2):
#   prize=2000
# elif (i==3):
#   prize=3000
print(".....Thank You !! For Prticipating in Millionaire Game.....") 
