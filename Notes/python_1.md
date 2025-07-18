# Version Control and Git

### Version control

What is a version control system?
- Track changes to code/documentation
- Avoids manual version control - copying and renaming e.g. v1.1, v1.2, v1.3...
- Easy to view previous versions/work and rolling back changes
- You can view who/when/what was modified
- Compare changes

Early version control

- often tracked changes to individual files
- There was a base file, each version tracked using a delta (the difference) added on each time

### Centralised VCS vs Distributed VCS (Git)

Centralised VCS

- Working copy of a file on a user's computer
- Whilst you were working on a file it would lock and noone else could access it
- you could save a copy but that would be local and not update the original file
- Only one person can update the file at a time
- Repository on server

Distributed VCS (like Git)

- Everybody gets a copy
- Repository on user's computer
- Repository on server
- Do not need to be connected to the internet to work on the files but must update when internet connection is restored
- Ideal to keep your version in sync with the server version so you do not lose anything
- Multiply this for all users needing to work on the repository - very valuable
- Push changes from your remote repository to the server repository (e.g. github) and you can then pull changes from that with other people's changes

Local VCS using Git

- Different versions of sets of files
- Version 1 - commit 1
  - File A
  - File B
  - File C
- Note: Commit - save a snapshot of a set of files
- Version 2 - commit 2
  - A1
  - no change to B
  - C1
- note: If no changes have been made since the last commit, only a reference for those files will be viewable
- Version 3 - commit 3
  - No change to A
  - No change to B
  - C2
- Note: Git does not store deltas but when it comes to compressing files it can store deltas to optimise storage

### Git

States of git
- Working directory becomes a git repository when you run something in the folder at which point you can use git to track the versions within the folder
- Folder needs to be initialised with git 
- Once it becomes a git repository we can start to use the git commands
- 3 states in git
  - modified working directory
  - staging area AKA added to index
  - .git directory (repository) (commited)
- You have made changes to files (modified working directory)
- At which point you have to run a command to add the files to staging (added to the index)
- Once they have been added to the staging(index) then you can run a command to commit them

Git commands
- `git init` - initialises the folder with git (turns folder into git repo)
- `git status` - check the state of everything
- `git add` - add files to staging areas in order to commit them
- `git add .` - adds all files to staging area in order to commit them
- `git commit -m` - git commit with a message
- `git reset` - must be careful, you can lose lots of changes with this command
- `git log` - shows previous commits
- `git checkout [branch]` - gets you back to the main commit