#!/usr/bin/python3
from git import Repo
import sys
#fonctionne
repo = Repo('/home/joord/Documents/dev/.git')
  # if repo is CWD just do '.'

data =  sys.argv[1]
#test




#fonctionne
repo.index.add(['*'])
repo.index.commit('my commit description')
origin = repo.remote('origin')
origin.push()
print (data)
