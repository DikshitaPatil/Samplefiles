fid="neha"
fpass="1234"
fid1="pooja"
fpass1="5678"
userid=input("enter your id:")
pasw=int(input("enter your password"))
if(userid==fid and pasw==fpass):
    print("welcome neha")
elif(userid==fid1 and pasw==fpass1):
    print("welcome pooja")
else:
    print("wrong id and password")
