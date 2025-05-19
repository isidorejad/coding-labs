def instruc():
    print("Welcome!\nYou will be tested on 4 questions about World History. 3 marks are alloted\nfor each question you answer correctly.\nAll the best!")
    name = input("Please enter your name to begin: ")
    print("\nHello", name+ "🙂 Good Luck!\n")

fun_fact1 = "World War I, also known as the Great War, began in 1914 after\nthe assassination of Archduke Franz Ferdinand of Austria. His murder\ncatapulted into a war across Europe that lasted until 1918.During the\nconflict, Germany, Austria-Hungary, Bulgaria and the Ottoman Empire (the-\nCentral Powers) fought against Great Britain, France, Russia, Italy, Romania,\nCanada, Japan and the United States(the Allied Powers).\n(A&E Television Networks 2009)"
fun_fact2 = "Adolf Hitler was born in Braunau am Inn in Austria on April\n20th, 1889.(Biography.com Editors 2014)"
fun_fact3 = "By 1215, thanks to years of unsuccessful foreign policies and\nheavy taxation demands, England’s King John was facing down a possib-\nle rebellion by the country’s powerful barons. Under duress, he agreed\nto a charter of liberties known as the Magna Carta (or Great Charter) that\nwould place him and all of England’s future sovereigns within a rule of law.\n(History.com Editors 2009)"
fun_fact4 = "A printing press is a device for applying pressure to an inked\nsurface resting upon a print medium (such as paper or cloth), thereby\ntransferring the ink. It marked a dramatic improvement on earlier printing\nmethods in which the cloth, paper or other medium was brushed or rubbed\nrepeatedly to achieve the transfer of ink, and accelerated the process.\nTypically used for texts, the invention and global spread of the printing\npress was one of the most influential events in the second millennium.\nJohannes Gutenberg, a goldsmith by trade, developed, circa 1439, a printing\nsystem by adapting existing technologies to printing purposes, as well as\nmaking inventions of his own.\n(H. Callum, Content Writer 2019)"
score = 0
# Instruction displayed for user
instruc()

# Storing questions into a function
# QUESTION 1
answer_1= input("1. World War 1 began in which year?\n (a) 1923 \n (b) 1938 \n (c) 1917 \n (d) 1914 \n Answer is: ")
if answer_1 == "d" or answer_1 == "1914":
    print(" Correct!")
    print("Fun fact: ",fun_fact1)
    print("\n")
    score += 3
else:
    print("Incorrect answer! Please try again.")
    print("\n")

# QUESTION 2
answer_2= input("2. Adolf Hitler was born in which country?\n (a) France \n (b) Germany \n (c) Austria \n (d) Hungary \n Answer is: ")
if answer_2 == "c" or answer_2 == "Austria":
    print(" Correct!")
    print("Fun fact: ",fun_fact2)
    print("\n")
    score += 3
else:
    print("Incorrect answer! Please try again.")
    print("\n")

# QUESTION 3
answer_3= input("3. The Magna Carta was published by the King of which country?\n (a) France \n (b) Austria \n (c) Italy \n (d) England \n Answer is: ")
if answer_3 == "d" or answer_3 == "England":
    print(" Correct!")
    print("Fun fact: ",fun_fact3)
    print("\n")
    score += 3
else:
    print("Incorrect answer! Please try again.")
    print("\n")

# QUESTION 4
answer_4= input("4. The first successful printing press was developed by this man.\n (a) Johannes Gutenberg \n (b) Benjamin Franklin \n (c) Sir Isaac Newton \n (d) Martin Luther \n Answer is: ")
if answer_4 == "a" or answer_4 == "Johannes Gutenberg":
    print(" Correct!")
    print("Fun fact: ",fun_fact4)
    print("\n")
    score += 3
else:
    print("Incorrect answer! Please try again.")
    print("\n")
    
# Feedback for player
def player_feedback():
    if score == 12:
        print("Excellent.")
    elif score >= 6:
        print("Very good.")
    else:
        print("Time to brush up on your knowledge of World History.")
player_feedback()
print('You scored:',score,'in this quiz')
        
