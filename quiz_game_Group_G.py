intro="Welcome to the Group G pub quiz"
print(intro.center(60,"*"))
name=input("\nInput your name here:")
print("Welcome to the PubG quiz" ,name)

ques = ("\nQ1. In which river runs through Paris? \nA.Seine/ \nB.Mersey/ \nC.Wine \nD.Delta", 
        "\nQ2. What type of food is gorganzola? \nA. Fruit \nB.Herb \nC.Cheese \nD.Herb",
        "\nQ3. What did Amber Heard leave on Jonny Depps pillow? \nA.Food \nB.Faecal matter \nC.Face cream \nD.Forks", 
        "\nQ4. What is a baby kangaroo called? \nA.Fawn \nB.Joey \nC.Cria \nD.Hatchling", 
        "\nQ5. What is the fear of small spaces called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia",
        "\nQ6. Who is the tenth Doctor Who? \nA.Tennant/ \nB.Eccleston/ \nC.Whittaker \nD.Capaldi", 
        "\nQ7. What is the name of the main antagonist in the Shakespeare play Othello?? \nA. Lady McBeth \nB.Lago \nC.Cymbeline \nD.Claudius",
        "\nQ8. Which popular video game franchise has released games with the subtitles World At War and Black Ops? \nA.Call of Duty \nB.Battlefield \nC.Genshin impact \nD.Overwatch", 
        "\nQ9. What is currency of Denmark called? \nA.Euro \nB.Pound \nC.Dollar \nD.Krone", 
        "\nQ10. What is the fear of food called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia"
        "\nQ11. Who is the tenth Doctor Who? \nA.Tennant/ \nB.Eccleston/ \nC.Whittaker \nD.Capaldi", 
        "\nQ12. What is the name of the main antagonist in the Shakespeare play Othello?? \nA. Lady McBeth \nB.Lago \nC.Cymbeline \nD.Claudius",
        "\nQ13. Which popular video game franchise has released games with the subtitles World At War and Black Ops? \nA.Call of Duty \nB.Battlefield \nC.Genshin impact \nD.Overwatch", 
        "\nQ14. What is currency of Denmark called? \nA.Euro \nB.Pound \nC.Dollar \nD.Krone", 
        "\nQ15. What is the fear of food called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia" 
        "\nQ16. Who is the tenth Doctor Who? \nA.Tennant/ \nB.Eccleston/ \nC.Whittaker \nD.Capaldi", 
        "\nQ17. What is the name of the main antagonist in the Shakespeare play Othello?? \nA. Lady McBeth \nB.Lago \nC.Cymbeline \nD.Claudius",
        "\nQ18. Which popular video game franchise has released games with the subtitles World At War and Black Ops? \nA.Call of Duty \nB.Battlefield \nC.Genshin impact \nD.Overwatch", 
        "\nQ19. What is currency of Denmark called? \nA.Euro \nB.Pound \nC.Dollar \nD.Krone", 
        "\nQ20. What is the fear of food called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia"
        "\nQ21. Who is the tenth Doctor Who? \nA.Tennant/ \nB.Eccleston/ \nC.Whittaker \nD.Capaldi", 
        "\nQ22. What is the name of the main antagonist in the Shakespeare play Othello?? \nA. Lady McBeth \nB.Lago \nC.Cymbeline \nD.Claudius",
        "\nQ23. Which popular video game franchise has released games with the subtitles World At War and Black Ops? \nA.Call of Duty \nB.Battlefield \nC.Genshin impact \nD.Overwatch", 
        "\nQ24. What is currency of Denmark called? \nA.Euro \nB.Pound \nC.Dollar \nD.Krone", 
        "\nQ25. What is the fear of food called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia")

ans = (("A" or "a"), ("C" or "c"), ("B" or "b"), ("B" or"b"),("B" or "b"))
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
print(".....Thank You !! For Participating in group G pub quiz.....")

