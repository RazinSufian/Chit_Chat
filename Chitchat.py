class Chitchat:
    def __init__  (self,string,country="Bangladesh"):
        print("Your request is being processed...")
        string=string.split(",")

        if  country=="Bangladesh":
            self.status=True
            self.name=string[0]
            self.id=string[1]
            self.age=string[2]
            self.gdender=string[3]
            self.friends_requests={}
            self.friends_relation={}
            self.friends=[]
            print("Account creation successful. But you have no friends. Add some friends and chill.")
        else:
            print("Sorry! Account creation is not allowed outside Bangladesh.")
        
    def AddFriend(self,*args):
        if len(args)==2:
            args[0].friends_requests[self]=args[1]
            return "Friend request sent. Pending for approval."
        else:
            return "Request Rejected! Relationship required."
    def approveFriendReq(self):
        for x,y in self.friends_requests.items():
            self.friends_relation[y]=f"{x.name}_{x.id}"
            self.friends.append(x)
            print(f"Congratulations! {self.name} and {x.name} can chat now.")
    def sendMessage(self,obj,masg):
        if obj.status==True:
            if self in obj.friends:
                print(f"Sent Massage:{masg}")
                print(f"Receiver Details => Name: {self.name}, ID: {self.id}, Age: {self.age}, Gender: {self.gdender}")
            else:
                print(f"Ooopps! You cannot chat with this person (id -> {obj.id}).")
        else:
            print(f"Ooopps! You cannot chat with this person (id -> {obj.id}).")
    def showNetwork(self):
        print(self.friends_relation)

    def changeStatus(self):
        if self.status==True:
            self.status=False
            print("Account activated/deactivated.")
        elif self.status==False:
            self.status=True
            print("Account deactivated/activated.")    




print("Welcome to Chitchat! Create an account, have fun!")
Wahid = Chitchat("Wahid,00123,23,Male")
print("1======================================")
Maliha = Chitchat("Maliha,00124,25,Female", "Malaysia")
print("2======================================")
Sadik = Chitchat("Sadik,00125,26,Male", "Bangladesh")
print("3======================================")
print(Wahid.AddFriend(Sadik, "Brother"))
print("4======================================")
Wahid.sendMessage(Sadik, "Hi, bro. How are you?")
print("5======================================")
Sadik.approveFriendReq()
print("6======================================")
Wahid.sendMessage(Sadik, "Hi, bro. How are you?")
print("7======================================")
Wahid.changeStatus()
print("8======================================")
Sadik.sendMessage(Wahid, "Hello, I'm fine.")
print("9======================================")
Sadik.showNetwork()
print("10=====================================")
Lamia = Chitchat("Lamia,00126,26,Female")
print("11=====================================")
print(Sadik.AddFriend(Lamia))
print("12=====================================")