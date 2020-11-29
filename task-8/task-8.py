
from github import Github

import os

username="amfoss"

user=Github().get_user(username)

for repo in user.get_repos():
    print(repo.name)
    os.system('perceval git --json-line https://github.com/amfoss/'+repo.name+'>> task-8.json')
os.system('cat task-8.json')
