
from github import Github   #imports the pygithub module

import os   #imports os module

username="amfoss"   #sets the username variable to 'amfoss'

user=Github().get_user(username)    #gets the user details of amfoss

for repo in user.get_repos():   #get_repos() gets all the repositories from the user amfoss, stores it in a list and each element of it gets stored in repo
    print(repo.name)
    os.system('perceval git --json-line https://github.com/amfoss/'+repo.name+'>> task-8.json') #receives the commits in each repo and exports it into the json file
os.system('cat task-8.json')    #reads the json file
