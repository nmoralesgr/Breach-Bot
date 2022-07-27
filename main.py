#Breach Bot Starter Code
breachYear = 2014

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Yahoo data breach.")

#Introduces breach
print("Would you like to learn about the Yahoo data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
      
  
  if topic.lower() == "a":
    print("Half a billion user accounts under Yahoo were hacked. The unknown hackers stole emails, real names, phone numbers, dates of birth, and passwords")
  
  elif topic.lower() == "b":
    print("It took Yahoo 2 years to detect the breach and then another 3 months to reveal it to their customers. They did not inform Verizon, who was supposed to buy their company for 5 billion dollars. Yahoo told their customers to change their passwords, security questions, and any other info on other sites that was similar.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("This data breach connects to integrity because Yahoo kept the breach hidden from its users and buyers in order to protect itself.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response because I think Yahoo should’ve been open about their breach so that people could take actions accordingly and Verizon didn’t go into an unwanted deal.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by saying personal information can be used to steal valuable data that can potentially harm your real-life presence. My advice would be to have different passwords for all your accounts, and even different security questions.")

  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")