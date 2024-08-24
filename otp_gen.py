import random
otp=random.randrange(100000,1000000)
print("your otp is ",otp)
print(" OTP valid for 10 min only ")
user=int(input("enter otp "))
if(otp==user):
     print("permission acces ! ")
else:
    print(" permission deny !!!")