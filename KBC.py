h = (input("•hello👋, Mr tarang how are you👋👋 :"))
r = (input("•Mr tarang introduce yourself and where was you:"))
t = (input("•well done let`s go to talk about Kaun Banega Crorepati ??:"))
m  = (input("•fine now i give to 5 level for won 1 lakh okk: "))
p = (input("•level 1 in 20 k" \
"           •level 2 in 40 k" \
"           •level 3 in 60 k" \
"           •level 4 in 80 k" \
"           •level 5 in 1 lakh "))



g = (input("દેવ્યા કે સજ્જનો ચલે શરૂ કરતે હૈ કૌન બનેગા કરોડપતિ......."))


print("first question is now your screen")


print("•••The largest city in which country is not its capital but a port with an Arabic name that means 'abode of peace'")
print(" A = SOMALIA" , "B = OMAN" ,
       "C = TANZANIA", "D = BRUNEI")
# print(list)

name = (input("chosse the option:"))

match name :
      case"C":
         print("🥳🥳congratulations tarang you won 20 k rupess 💐 💐")
      case "A":
       print("😔😔sorry tarang you loss 20 k rupess")
      case"B":
       print("😔😔sorry tarang you loss 20 k rupess")
      case"D":
       print("😔😔sorry  tarang you loss 20 k rupess")


q = (input("now we got to level 2:"))


print("•••which Mughal emperor was known for building the Taj Mahal?")
list = [" A = SHAH JAHAN" , "B = AKBAR" ,
        "C = BABAR"      ,  " D = HUMAYU"]
print(list)

name = (input("chosse the option:"))

match name :
      case"A":
         print("🥳🥳congratulations tarang you won 40 k rupess💐 💐 ")
      case "B":
       print("😔😔sorry tarang you loss 40 k rupess")
      case"C":
       print("😔😔sorry tarang you loss 40 k rupess")
      case"D":
       print("😔😔sorry  tarang you loss 40 k rupess")

w = (input("now we got to level 3 and level 3 is hard :"))


print("•••Which of these states has had the most number of its governors become presidents of India?")
list = [" A = RAJASTHAN" , "B = BIHAR" ,
        "C = PUNJAB"      ,  " D = ANDHRA PRADESH "]
print(list)

name = (input("chosse the option:"))

match name :
      case"B":
         print("🥳🥳congratulations tarang you won 60 k rupess💐 💐 ")
      case "A":
       print("😔😔sorry tarang you loss 60 k rupess")
      case"C":
       print("😔😔sorry tarang you loss 60 k rupess")
      case"D":
       print("😔😔sorry tarang you loss 60 k rupess")
       
         
          
k = (input("now we got to level 4:"))


print("•••Who was the first recorded child born to English parents in North America in 1587")

list = [" A = VIRGINIA DARE" , "B = OLIVER SMITH" ,
        "C = ISLA MORGAN"      ,  " D = DAVIES MORRIS "]
print(list)

name = (input("chosse the option:"))

match name :
      case "A":
         print("🥳🥳congratulations tarang you won 80 k rupess 💐 💐 ")
      case "B":
       print("😔😔sorry tarang you loss 80 k rupess")
      case"C":
       print("😔😔sorry tarang you loss 80 k rupess")
      case"D":
       print("😔😔sorry  tarang you loss 80 k rupess")


f = (input("now we got to last level and last level is so hardest got it:"))

print("•••Which of the following is NOT a primary objective of the Indian government's monetary policy?")

list = [" A = CONTROLING INFLATION " , "B = PROMTING ECONOMICS GROWTH" ,
        "C = MAINTAINING EXCHANGE RATE STABILITY "      ,  " D = REDUCING INCOME INEQULITY"]
print(list)

name = (input("chosse the option:"))

match name :
      case " D":
         print("🥳🥳congratulations tarang you won 1 lakh rupees rupess💐 💐 ")
      case "C":
       print("😔😔sorry tarang you loss 1 lakh rupess")
      case"B":
       print("😔😔sorry tarang you loss 1 lakh rupess")
      case"A":
       print("😔😔sorry  tarang you loss 1 lakh rupess")
  

  
print("🙏thank you,for playing quiz with me🙏 ")



import random

print("🐍🌊🔫Welcome to snake water and gun game!")
print("choice : s for snake ,g for gun, w for water")

choice = ['s','w','g']
round = (input("How many round play wann:"))
name = (input("Enter your choice(s/w/g):"))

com = random.choice(choice)

    
print(f"your choice:{name}")
print(f"com choice:{com}")


for i in range(round):
   name = (input("Enter your choice(s/w/g):")).lower()
   if (name  == com):
      print("It`s a tie🤝") 
   elif (name =='s' and com == 'w') or (name == 'g' and com =='s') or (name == 'w' or com == 'g'):
    print("you win 🥳")
   else :
    print("you loos ")    



