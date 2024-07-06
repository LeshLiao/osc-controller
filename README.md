## IDE: Visual Studio Code

## Version: Python 3.9.6

### Memo:

#### save changed by stash
- git stash save "new_stash" --include-untracked
- git status
- git pull
- git stash list
- git stash apply stash@{0}

#### check stage changed
- git add .
- git diff --cached

### commit and push
- git add .
- git commit -am "My message"
- git log
- git push

### check connection
- ssh -T git@github.com

### enable ssh agent
cd /python-stuff
eval $(ssh-agent -s)
ssh-add ~/.ssh/rpi-key
