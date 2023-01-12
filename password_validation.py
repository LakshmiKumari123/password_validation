# Password Validation Program.
#1K@l
# we need atleast 4 character with atleast one[special char,digit,alpha in both case]
password=input("Enter Your Password :")
a,b,c,d=0,0,0,0
p=["@","#","$","%","^","&","*"]
if len(password)>=4:
  for i in password:
    if i.isalpha():
      if i==i.upper():
        a+=1
      else:
        b+=1
    elif i.isdigit():
      c+=1
    elif i in p:
      d+=1
  if (a>=1) and (b>=1) and (c>=1) and (d>=1):
    print("Valid Password")
  if a==0:
    print("Enter atleast one capital later")
  if b==0:
    print("Enter atleast one small later")
  if c==0:
    print("Enter atleast one digit")
  if d==0:
    print("Enter atleast on special character")
else:
  print("password size should be atleast 4")