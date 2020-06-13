# trygit-4-8-plus
A simple mock up of a modular, nested python package for group collaboration without merge conflicts on day 1

## How to Use trygit-4-8-plus 
* `solarsys` is meant to represent a standalone ***repo***sitory
* it is incomplete and imperfect by design
* use `trygit-4-8-plus` as a template to create your custom repo to customize the experience
  
## Instructions for Custom Repo
*See the bottom of this document to find some common **Reference Materials**.* 
### Requirements
- Each particpate has a github account
- Each particpate has git installed on your computer or laptop
- Each particpate has python on your computer or laptop
- Team messaging platform if working remotely
- Link from organizer to your team's custom repo
### Abbreviations
- Group Git webpage (**GG**)
- Your Git webpage (**YG**)
- Your Computer (**YC**)
### Step by step
***Getting a local copy for future contributions via git***
1. ***GG***: Click ***Fork*** (top left) and select your github username
2. ***YG***: Click ***Clone or Download*** and copy the the URL in the pop-up window
3. ***YC***: Open terminal window and navigate to where you want to save this repo
4. ***YC***: Type `git clone <pasted_url>`. `<pasted_url>` is the entireity of your previous copy on ***YG***.  It will be something like `https://github.com/<your_git_uid>/<repo_name>.git`
4. ***YC***: Type `cd <repo_name>`. 
4. ***YC***: Type `git remote add <repo_name> git://github.com/<repo_name>/<repo_name>.git`. Now your computer is setup to track your remote fork (default name `origin`) and the remote central repo (`<repo_name>`). You can locally change the names if more convenient for you. 
6. ***YC***:  Test the library by starting a python session and importing the library. You can begin developing your contributions to the local repo you just cloned.
*Before telling git of your changes...*
- Do not locally *commit* and *push* changes to the central repo. Use your fork for this purpose.
- It is best to never *commit* work on the master branch. The central repo and its forks can have different copies called braches with unique names. In this way, you can work on serveral changes with serveral branches for your fork of a central repo.
- Git commands to check things before committing: `git status`, `git remote -v`, `git branch`
- Use `git commit` regulary to track incremental changes. 
- If you get stuck or confused,then use [scikit-beam's citee resource for common git problems](http://sethrobertson.github.io/GitFixUm/fixup.html)

***Starting local contributions via get***
1. ***GG***: Use ***Issues*** link to identify potential problems to help solve or start an *issue* on something you would like to solve/enhance. Sometimes individuals will assign themselves to work on a problem.  Once they have a solution they want to *merge* into the central repo, the *issue* should reference the associated *pull request*. Use ***Pull Requests*** to see changes to code that are under review. 
2. ***YC***: Type `git branch <descriptive_name-of-your-change>` to create a new branch. Use `git branch` to see the active branch.
3. ***YC***: Type `git checkout <branch-descriptive-name-of-your-change>` to switch to the new branch. Use `git branch` again.
4. ***YC***: Type `git add <filename.py>` to organize the files you have changed/created and would like to *commit*.
5. ***YC***: Type `git commit -m "<quick statement descring incremental change>"`. Repeat `git add` and `git commit` as necessary until you are finished with your changes/additions

***Submitting your changes***
*Some central repos have requirements like tests and codestyle (PEP8).  These can be automated.*
1. ***YC***: After all tests and check, type `git push <your_fork_remote_name> <branch-descriptive-name-of-your-change>`. If using the default remote name in this workflow, <your_fork_remote_name> = `origin`
2. ***GG***: Click ***Pull requests*** and select ***New pull requests***. You will see a GUI to decribe what which repo/branch that you want to move your specific repo/branch into:   *BASE-Remote(Fork), Branch <<-- HEAD-Remote(Fork), Branch*.  For most cases you only need to change the branch on each side to match `<branch-descriptive-name-of-your-change>`.
3. ***GG***: Click ***Submit*** and select 1 to 3 reviewers depending on central repo rules and complexity of your submitted *pull request* (PR). In ***Issues*** add a comment referencing your new *PR*.
4. ***GG***: You can recieve email updates to your *PRs*. Interact with reviewers and other interested parties on github as much as possible.
5. ***YC***: If you have new changes in response to the *PR* review before it is *merged*, then you can continue to *add* and *commit* changes to the submitted branch on your fork. To update the *PR*, you will just simply perform the same *push* in step 1.
6. ***GG***: Sometimes *merging* permission is granted to everyone, but check with others before *merging* your *PR* to avoid confusion. Once the *PR* is *merged*, update and potentially close the associated *issue(s)*. 











### Reference Materials: 
*For your implmentation of this template or in your future projects.*
- [solar system](https://solarsystem.nasa.gov/planets/in-depth/#the_new_definition_of_planet_otp)
- [markdown](https://www.markdownguide.org/cheat-sheet/)
- [See ***Contributing*** and ***Developer Materials*** for detailed practices used by a community repo](https://scikit-beam.github.io/scikit-beam/ )
- [more git](http://try.github.io/)
