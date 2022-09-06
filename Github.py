import requests
import json

class Github:
    def __init__(self):
        self.api_url= "https://api.github.com"
        

    def getUser(self,usernamex):
        response=requests.get(self.api_url+"/users/"+usernamex)
        return response.json()

    def getRepositories(self,username):
        response=requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()

    def createRepository(self, Rname,token):
        payload ={
            "name": Rname,
            "description": "This is your first repository",
            "private": True,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        
        response = requests.post(self.api_url + '/user/repos', auth=('<YOUR_USERNAME>', token), data=json.dumps(payload))
        return response.json()


github=Github()
while True:
    print(" Merhaba ".center(50,"*"))
    
    
    secim=input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nSeçiminiz: ")
    if secim=="4":
        break
    else:
        if secim=="1":
            username=input("username: ")
            result=github.getUser(username)
            print(f"Name: {result['name']}\nPublic Repos: {result['public_repos']}\nFollowers: {result['followers']} ")
                
        elif secim=="2":
            username=input("username: ")
            result=github.getRepositories(username)
            i=0
            for repo in result:
                i+=1
                print(f"{i}.Repository ismi: {repo['name']}")
        elif secim=="3":
            token=input("lütfen tokeninizi giriniz: ")
            Rname=input("Repo name giriniz: ")
            result=github.createRepository(Rname,token)
            print(result)
        else:
            print("yanlış bilgi girdiniz".center(50,"!"))
