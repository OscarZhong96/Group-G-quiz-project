intro="Welcome to the Group G pub quiz"
print(intro.center(60,"*"))
name=input("\nInput your name here:")
print("Welcome to the PubG quiz" ,name)
#questions from Oscar 1-10
ques = ("\nQ1. In which river runs through Paris? \nA.Seine/ \nB.Mersey/ \nC.Wine \nD.Delta", 
        "\nQ2. What type of food is gorganzola? \nA. Fruit \nB.Herb \nC.Cheese \nD.Herb",
        "\nQ3. What did Amber Heard leave on Jonny Depps pillow? \nA.Food \nB.Faecal matter \nC.Face cream \nD.Forks", 
        "\nQ4. What is a baby kangaroo called? \nA.Fawn \nB.Joey \nC.Cria \nD.Hatchling", 
        "\nQ5. What is the fear of small spaces called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia",
        
        "\nQ6. Who is the tenth Doctor Who? \nA.Tennant/ \nB.Eccleston/ \nC.Whittaker \nD.Capaldi", 
        "\nQ7. What is the name of the main antagonist in the Shakespeare play Othello?? \nA. Lady McBeth \nB.Lago \nC.Cymbeline \nD.Claudius",
        "\nQ8. Which popular video game franchise has released games with the subtitles World At War and Black Ops? \nA.Call of Duty \nB.Battlefield \nC.Genshin impact \nD.Overwatch", 
        "\nQ9. What is currency of Denmark called? \nA.Euro \nB.Pound \nC.Dollar \nD.Krone", 
        "\nQ10. What is the fear of food called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia",
        #Questions from Charlie 11-15
        "\nQ11. What is the name of the 6th harry potter book and movie? Harry potter and...? \nA.The Goblet of fire/ \nB.The Order of the phoenix/ \nC.The half blood prince \nD.Deathly hallows", 
        "\nQ12. In pack to the future part 2 what year does Marty and Doc Travel to at the start of the movie? \nA. 2015 \nB.1955 \nC.1985 \nD.2000",
        "\nQ13. What is the  capital of Australia? \nA.Sydney \nB.Canberra \nC.Perf \nD.Melbourne", 
        "\nQ14. In Shrek 2, what animal does king Harold get turned into? \nA.Bunny \nB.Toad \nC.Chicken \nD.Frog", 
        "\nQ15. Which of these x-men is the oldest? \nA.Wolverine \nB.Professor-X \nC.Magneto \nD.Beast", 
        #Questions from Ashir 16-20
        "\nQ16. What is the highest mountain in the world? \nA.Mount Fuji/ \nB.Mount Kilimanjaro/ \nC.Mount Everest \nD.K2", 
        "\nQ17. What was the Turkish City of Istanbul called before 1930? \nA. Antalya \nB.Constantinople \nC.Bethlehem \nD.Ankara",
        "\nQ18. What is the most profitable piece of entertainment in history? \nA.Avatar\nB.Iphone \nC.Michael Jackson's thriller \nD.Grand Theft Auto 5", 
        "\nQ19. Who won the first ever football World Cup? \nA.Brazil \nB.Uruguay \nC.England \nD.France", 
        "\nQ20. At which venue is the F1 British Grand Prix held? \nA.Nürburgring \nB.Monaco \nC.Red Bull Ring \nD.Silverstone"
        #Questions from Abdullah 21-25
        "\nQ21. What is the capital of France? \nA.Paris/ \nB.Rome/ \nC.London \nD.Madrid", 
        "\nQ22. Which planet is known as the Red Planet? \nA.Venus \nB.Jupiter \nC.Mars \nD.Saturn",
        "\nQ23. Which is the largest ocean in the world? \nA.Indian Ocean \nB.Pacific Ocean \nC.Artic Ocean \nD.Atlantic Ocean", 
        "\nQ24. What is currency of Denmark called? \nA.Euro \nB.Pound \nC.Dollar \nD.Krone", 
        "\nQ25. What is the fear of food called? \nA.Acrophobia \nB.Claustrophobia \nC. \nD.Cibophobia")

ans = (("A" or "a"), ("C" or "c"), ("B" or "b"), ("B" or"b"),("B" or "b"),("A" or "a"), ("B" or "b"), ("A" or "a"), ("D" or"d"),("D" or "d"),("A" or "a"), ("C" or "c"), ("B" or "b"), ("B" or"b"),("B" or "b")("A" or "a"), ("C" or "c"), ("B" or "b"), ("B" or"b"),("B" or "b"))
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

