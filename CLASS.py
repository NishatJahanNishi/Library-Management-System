class user:
    name=''
    email=''
    password=''
    login=False


def login(self):
       if(email==self.email and password==self.password):
           login=True
           print("Successful")
       else:
        print("failed")

def logout(self):
    login=False
    print("out")
def loggedin(self):
      if (self.login):
        return True
      else:
        return False
def profile(self):
      if loggedin():
        print(self.name, "\n", self.email)
      else:
        print("Not logged in")


a=user()
a.name="Nishi"
a.email="nishi@gmail.com"
a.password="1234"
a.login()


