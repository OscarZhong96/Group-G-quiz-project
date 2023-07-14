from timeit import default_timer as timer


def new_game():
  intro = "Welcome to the Group G pub quiz"
  print(intro.center(60, "*"))
  name = input("\nInput your name here:")
  print("Welcome to the Group G pub quiz", name,
        "\nYou will have 30s for each question")
  return name


def play_again():
  response = input("Would you like to play again? (Y) or (N):")
  response = response.upper()
  if response == "Y":
    return True
  else:
    return False


#========================================= questions from Oscar 1-5 =====================================================-
ques = (
  "\nQ1. In which river runs through Paris? \nA.Seine \nB.Mersey \nC.Wine \nD.Delta",
  "\nQ2. What type of food is gorganzola? \nA. Fruit \nB.Herb \nC.Cheese \nD.Herb",
  "\nQ3. What did Amber Heard leave on Jonny Depps pillow? \nA.Food \nB.Faecal matter \nC.Face cream \nD.Forks",
  "\nQ4. What is a baby kangaroo called? \nA.Fawn \nB.Joey \nC.Cria \nD.Hatchling",
  "\nQ5. What is the fear of small spaces called? \nA.Acrophobia \nB.Claustrophobia \nC.Hydrophobia \nD.Cibophobia",
  
#========================================= questions from Rosemary 6-10 =====================================================-

  "\nQ6. Who wrote Pride and Prejudice? \nA.Jane Austen \nB.Charles Dickens \nC. Stephen  King \nD.Harper Lee",
  "\nQ7. Who directed Inception?? \nA. Christopher Nolan \nB.Steven Spielberg \nC.Alfred Hitchcock \nD.Quentin Tarantino",
  "\nQ8. What is the square root of 81 \nA.8 \nB.9 \nC.10 \nD.11",
  "\nQ9. What is the largest planet in the solar system called? \nA.Earth \nB.Mars \nC.Jupiter \nD.Mercury",
  "\nQ10. What does the acronym HTML stand for? \nA.HyperText Markup Language. \nB.HydroToning Maxim Language \nC.HackerText Mouse Language \nD.HiddenTiming Meaning Language",

  #========================================= Questions from Charlie 11-15 =================================================
  "\nQ11. What is the name of the 6th harry potter book and movie? Harry potter and...? \nA.The Goblet of fire \nB.The Order of the phoenix \nC.The half blood prince \nD.Deathly hallows",
  "\nQ12. In pack to the future part 2 what year does Marty and Doc Travel to at the start of the movie? \nA. 2015 \nB.1955 \nC.1985 \nD.2000",
  "\nQ13. What is the  capital of Australia? \nA.Sydney \nB.Canberra \nC.Perf \nD.Melbourne",
  "\nQ14. In Shrek 2, what animal does king Harold get turned into? \nA.Bunny \nB.Toad \nC.Chicken \nD.Frog",
  "\nQ15. Which of these x-men is the oldest? \nA.Wolverine \nB.Professor-X \nC.Magneto \nD.Beast",

  #========================================= Questions from Ashir 16-20 =====================================================
  "\nQ16. What is the highest mountain in the world? \nA.Mount Fuji \nB.Mount Kilimanjaro \nC.Mount Everest \nD.K2",
  "\nQ17. What was the Turkish City of Istanbul called before 1930? \nA. Antalya \nB.Constantinople \nC.Bethlehem \nD.Ankara",
  "\nQ18. What is the most profitable piece of entertainment in history? \nA.Avatar\nB.Iphone \nC.Michael Jackson's thriller \nD.Grand Theft Auto 5",
  "\nQ19. Who won the first ever football World Cup? \nA.Brazil \nB.Uruguay \nC.England \nD.France",
  "\nQ20. At which venue is the F1 British Grand Prix held? \nA.Nürburgring \nB.Monaco \nC.Red Bull Ring \nD.Silverstone",

  #========================================= Questions from Abdullah 21-25 ==================================================
  "\nQ21. What is the capital of France? \nA.Paris \nB.Rome \nC.London \nD.Madrid",
  "\nQ22. Which planet is known as the Red Planet? \nA.Venus \nB.Jupiter \nC.Mars \nD.Saturn",
  "\nQ23. Which is the largest ocean in the world? \nA.Indian Ocean \nB.Pacific Ocean \nC.Artic Ocean \nD.Atlantic Ocean",
  "\nQ24. What is the chemical symbol for gold? \nA.Au \nB.Ag \nC.Fe \nD.Cu",
  "\nQ25. Which country is home to the kangaroo? \nA.Brazil \nB.Mexico \nC.Canada \nD.Australia"
)
#============================================================================================================================
ans = (
  ("A"),
  ("C"),
  ("B"),
  ("B"),
  ("B"),
  ("A"),
  ("A"),
  ("B"),
  ("C"),
  ("A"),
  ("A"),
  ("C"),
  ("B"),
  ("B"),
  ("B"),
  ("C"),
  ("B"),
  ("D"),
  ("B"),
  ("D"),
  ("A"),
  ("C"),
  ("B"),
  ("A"),
  ("D"),
)
prize = [100] * len(ques)

while True:
  total_points = 0
  points = 0
  name = new_game()

  for i in range(len(ques)):
    print(ques[i])
    start = timer()

    Ans = input("Select your Answer OR to Quit press 'Q': ")
    if Ans == "Q":
      print("Thank You for Playing!")
      break
    if Ans == ans[i]:
      end = timer()
      timedifference = end - start
      if timedifference <= 30:
        print("Correct! You have gained points of £.", prize[i], "you took:",
              round(timedifference, 2), "s")
        points += prize[i]
      else:
        print("You took", round(timedifference, 2), "s",
              "This answer shall not be counted")
    else:
      print("The answer is incorrect")

  total_points += points

  print("\n\nTotal Amount of points by", name, "is", total_points)

  Achievement = ["Youngling", "Padawan", "Jedi Knight", "Jedi Master"]
  if total_points <= 2500 and total_points >= 2001:
    print("\nCONGRATS! You have achieved the rank of ", Achievement[3])
  elif total_points <= 2000 and total_points >= 1501:
    print("\nWOW! You have achieved the rank of ", Achievement[2])
  elif total_points <= 1500 and total_points >= 1001:
    print("\nWOW! You have achieved the rank of ", Achievement[1])
  elif total_points <= 1000 and total_points >= 501:
    print("\nWELL DONE! You have achieved the rank of ", Achievement[0])
  else:
    print("\nUNLUCKY! You have unlocked being a NOOB.")

  High_score = open('high score.txt', 'a')
  High_score.write("\n"
                   "name  " + name + " "
                   "score  " + str(total_points))
  High_score.close()
  with open('high score.txt', 'r') as f:
    contents = f.read()
    print("-------------------------------"
          "\n"
          "Previous scores" + contents + "\n")

  if not play_again():
    print("Thank you for playing Group Gs Grand Quiz")
    break
