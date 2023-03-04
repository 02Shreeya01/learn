# declare two variables and add them or sub them or mult them or div them
# work - 1
a=45
b=56
c=a+b
print(c)

x=99
y=34
z=x-y
print(z)

g=89
h=55
i=g*h
print(i)

s=67
t=77
r=s/t
print(r)


#work - 2 
#if condition

cake = "redvelvet"

if cake == "Black Forest Cake":
    print("the rate of this is 500")
elif cake == "Butterscotch":
    print("the rate of this is 550")  
elif cake == "pineapple":
    print("the rate of this is 500")
elif cake == "chocalate caramel":
    print("the rate of this is 650") 
elif cake == "fudge Brownie":
    print("the rate of this is 800")
elif cake == "fruit overload cake":
    print("the rate of this is 850")    
elif cake == "cream drop chocalate":
    print("the rate of this is 650")    
else:
    print("the quality is good in this backery") 
    
    
# work - 3 

colors = ["Butterscotch","pineapple","Black Forest Cake","chocalate caramel","fudge Brownie","fruit overload cake","cream drop chocalate"]
for i in colors:        
    print(i)
cake = "redvelvet"

if cake == "Black Forest Cake":
    print("the rate of this is 500")
elif cake == "Butterscotch":
    print("the rate of this is 550")  
elif cake == "pineapple":
    print("the rate of this is 500")
elif cake == "chocalate caramel":
    print("the rate of this is 650") 
elif cake == "fudge Brownie":
    print("the rate of this is 800")
elif cake == "fruit overload cake":
    print("the rate of this is 850")    
elif cake == "cream drop chocalate":
    print("the rate of this is 650")    
else:
    print("the quality is good in this backery") 
    print(i)
   
#work - 4
#marks

dictt = {"sub1" : 70, "sub2" : 60, "sub3" : 75 }
max_marks = 75

dictt. values()

dictt. keys()   

for i, j in zip (dictt.keys(), dictt.values()):
    print(i, round((j/max_marks)*100))
    
    
dictt = {"sub1" : 70, "sub2" : 60, "sub3" : 75 }
max_marks = 75
dict1 = {}
for i, j in zip (dictt.keys(), dictt.values()):
    c = round((j/max_marks)*100,2)
    dict1 = [i]
    print(i, c) 
    
#work - 5
#marks
max_marks = [100,75,100,35,50]
marks = {"stu1" :[55,35,65,20,33],
"stu2" :[95,35,70,25,36],
"stu3" :[50,60,65,22,45],
"stu4" :[58,65,87,16,54],
"stu5" :[35,44,76,24,49],
"stu6" :[22,54,54,10,35],
"stu7" :[56,56,86,6,45],
"stu8" :[75,74,88,5,5],
"stu9" :[99,32,24,4,24],
"stu10" :[13,45,86,33,34], 
"stu11" :[56,54,65,23,43], 
"stu12" :[35,67,56,32,40], 
"stu13" :[45,13,36,30,44],
"stu14" :[29,45,22,23,33],  
"stu15" :[59,24,65,34,23]}



marks = [55,95,50,58,35,22,56,75,99,13,56,35,45,29,59]

for i in marks:
   per = round((i/100)*100,2) 
   if per < 100 and per > 80:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : A")
   elif per <= 80  and per >60:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : B")
   elif per <= 60  and per >50:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : C")
   elif per <= 50:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : D")
   else:
       print("Marks : " + str(i))
       print("Error")

marks = [35,35,60,65,44,54,5674,32,45,65,67,13,45,24]

for i in marks:
   per = round((i/75)*100,2) 
   if per < 100 and per > 80:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : A")
   elif per <= 80  and per >60:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : B")
   elif per <= 60  and per >50:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : C")
   elif per <= 50:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : D")
   else:
       print("Marks : " + str(i))
       print("Error")
       
mark [65,70,65,87,76,54,86,88,24,86,65,56,36,22,65]       
       
       for i in marks:
          per = round((i/100)*100,2) 
          if per < 100 and per > 80:
              print("Marks : "+ str(i) +" ,Percentage : " + str(per))
              print("Grade : A")
          elif per <= 80  and per >60:
              print("Marks : "+ str(i) +" ,Percentage : " + str(per))
              print("Grade : B")
          elif per <= 60  and per >50:
              print("Marks : "+ str(i) +" ,Percentage : " + str(per))
              print("Grade : C")
          elif per <= 50:
              print("Marks : "+ str(i) +" ,Percentage : " + str(per))
              print("Grade : D")
          else:
              print("Marks : " + str(i))
              print("Error")
              
marks = [20,25,22,16,24,10,6,5,4,33,23,32,30,23,34]              
              
   for i in marks:
   per = round((i/35)*100,2) 
   if per < 100 and per > 80:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : A")
   elif per <= 80  and per >60:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : B")
   elif per <= 60  and per >50:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : C")
   elif per <= 50:
       print("Marks : "+ str(i) +" ,Percentage : " + str(per))
       print("Grade : D")
   else:
       print("Marks : " + str(i))
       print("Error")
       
marks = [33,36,45,45,49,35,45,5,24,34,43,40,44,33,23]       
       
for i in marks:
per = round((i/50)*100,2) 
if per < 100 and per > 80:
    print("Marks : "+ str(i) +" ,Percentage : " + str(per))
    print("Grade : A")
elif per <= 80  and per >60:
    print("Marks : "+ str(i) +" ,Percentage : " + str(per))
    print("Grade : B")
elif per <= 60  and per >50:
    print("Marks : "+ str(i) +" ,Percentage : " + str(per))
    print("Grade : C")
elif per <= 50:
    print("Marks : "+ str(i) +" ,Percentage : " + str(per))
    print("Grade : D")
else:
    print("Marks : " + str(i))
    print("Error")
 
 
 #work -6 
#web scrapping 
 
import requests

response = requests.get("https://en.wikipedia.org/wiki/Volleyball")

result = {
    'status_code' : response.status_code,
    'headers' : dict(response.headers),
    'content' : response.text
    }

print(result) 
 
 
#work - 7 
#  Using Dictionary and list with for loop and If loop:

cricket = [
    {'name' : 'SR Tendulkar (IND)','runs' : 15921 }, 
    {'name' : 'RT Ponting(AUS)','runs' : 13378 },
    {'name' : 'JH Kalis(ICC/SA)','runs' : 13289 },
    {'name' : 'R Dravid(ICC/IND)','runs' : 13288 },
    {'name' : 'AN Cook (ENG)','runs' : 12472 },
    {'name' : 'KC Sangakkara (SL)','runs' : 12400 },
    {'name' : 'BC Lara (ICC/WI)','runs' : 11953 },
    {'name' : 'S Chanderpaul (WI)','runs' : 11867 },
    {'name' : 'DPMDJayawardene (SL)','runs' : 11814 }, 
    {'name' : 'AR Border (AUS)','runs' : 11174 },
    {'name' : 'SR Waugh (AUS)','runs' : 10927 },
    {'name' : 'JE Root (ENG)','runs' : 10853 },
    {'name' : 'SM Gavaskar (IND)','runs' : 10122 },
    {'name' : 'Younis khan (Pak)','runs' : 10099 },
    {'name' : 'HM Amla (SA)','runs' : 9282 },
    {'name' : 'GC Smith (ICC/SA)','runs' : 9265 },
    {'name' : 'GA Gooch (ENG)','runs' : 8900 },
    {'name' : 'Javed Miandad (PAK)','runs' : 8832 },
    {'name' : 'Inzamam-ul-Haq (ICC/PAK)','runs' : 8830 }, 
    {'name' : 'VVS Laxman (IND)','runs' : 8781 },
    {'name' : 'AB de Villiers (SA)','runs' : 8765 },
    {'name' : 'SPD Smith (AUS)','runs' : 8718 },
    {'name' : 'MJ Clarke (AUS)','runs' : 8643 },
    {'name' : 'ML Hayden (AUS)','runs' : 8625 },
    {'name' : 'V Sehwag (ICC/IND)','runs' : 8586 }
    ]  

names_over_11100 = [] 

for person in cricket:
    if person['runs'] > 11100:
        names_over_11100.append(person['name']) 
        
print(names_over_11100)

    