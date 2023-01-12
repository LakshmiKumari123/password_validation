# email Validation Program

email=input("Enter Your E-mail :")
a,b,c=0,0,0
# l@l.com / l@l.in
# length should be grether than or equals to 6
if len(email)>=6: #1 length should be atleast 6
  if email[0].isalpha(): #2 first character should be alphabet
    if "@" in email and email.count("@")==1: #3   single @ is acceptable
      if (email[-4]==".")^(email[-3]=="."): #4 two dot continousily not allowed
        for i in email:
          if i==i.isspace(): #5  Spaces are not allowed
            a=1
          elif i.isalpha():#5
            if i==i.upper():
              b=1
          elif (i =="_") or (i ==".") or (i =="@") or i.isdigit():#5 number and only these special characters are acceptable.
            continue
          else:
            c=1
        if a==1 or b==1 or c==1: #5
          print("Wrong email address #5")
        else:
          print("Verified")
      else:
        print("Wrong email address #4")
    else:
      print("Wrong email address #3")
  else:
    print("Wrong email address #2")
else:
  print("Wrong email address 1")
