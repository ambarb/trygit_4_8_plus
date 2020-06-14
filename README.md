# trygit-4-8-plus
A simple mock up of a modular, nested python package for group collaboration without 8 people editing the same file.

## How to Use trygit-4-8-plus 
* `solarsys` is meant to represent a standalone ***repo***sitory
* it is incomplete and imperfect by design but provides a "sandbox" to practice software development
* use `trygit-4-8-plus` as a template to create your custom repo for a customized team experience
* These participant instructions are designed as if you rename the repo `solarsys`
 
# solarsys
A simple mock up of a modular, nested python package for group collaboration. The project is a sandbox for gaining experience with collaborative coding projects and provides opportunites to develop and practice more advanced skills.  
 
## Instructions for using solarsys to learn more about git
*See the bottom of this document to find some common **Reference Materials**.* 
### Requirements
- Each particpate has a github account
- Each particpate has git installed on their computer
- Each particpate has python on their computer 
- Team messaging platform if working remotely
- Link from organizer to team's custom repo with additional instructions
### Abbreviations
- Group Git webpage of repo (**GG**)
- Your Git webpage of forked repo (**YG**)
- Your Computer (**YC**)
### Step by step
***Getting a local copy for future contributions via git***
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***GG*** | Click ***Fork*** (top left) and select your github username |
| 2. | ***YG*** | Click ***Clone or Download*** and copy the the URL in the pop-up window |
| 3. | ***YC*** | Open terminal window and navigate to where you want to save this repo |
| 4. | ***YC*** | Type `git clone <paste_copied_url>`. `<paste_copied_url>` is something like `https://github.com/<your_git_uid>/<repo_name>.git`. |
| 5. | ***YC*** | Type `cd solarsys`.  |
| 6. | ***YC*** | Type `git remote add solarsys git://github.com/<team_name>/solarsys.git`.  You can copy the link from *GG* like in set 2. |

Now your computer is setup to track your remote fork (default name `origin`) and the remote central repo (`<repo_name>`). You can locally change the names if more convenient for you.  

***Test the library by starting a python session and importing the library.*** If using a conda env or something simliar, you can `cd <repo_name>` and `pip install xxxx -e .` If all else fails, start your python session, navigate to the repo directory and `import solarsy`.

***Things to know before you start changing files***
- Do not locally *commit* and *push* changes to the central repo. Use your fork for this purpose.
- It is best to never *commit* work on the master branch. The central repo and its forks can have different "copies" called branches. 
- Git commands to check things before committing: `git status`, `git remote -v`, `git branch`
- Use `git commit` and `git push` regulary to track incremental changes and not loose work. 
- If you get stuck or confused,then use [scikit-beam's cited resource for common git problems](http://sethrobertson.github.io/GitFixUm/fixup.html).

***Starting local contributions and submitting them***
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***GG*** | Use ***Issues*** link to identify potential problems to help solve or start an *issue* on something you would like to contribute.|
| 2. | ***GG*** | If an issue is not assigned to you, then pick/create an issue and self assign. |
| 3. | ***YC*** | Type `git pull origin master`. |
| 4. | ***YC*** | Type`git branch <descriptive_name-of-your-change>` to create a new branch. Type `git branch`. Where is `*`?|
| 5. | ***YC*** | Type `git checkout <branch-descriptive-name-of-your-change>` to switch to the new branch. Type `git branch`.|
| 6. | ***YC*** | Start making changes and testing them as you go. |
| 7. | ***YC*** | Type `git add <filename.py>` to organize the files you have changed/created and would like to *commit*. |
| 8. | ***YC*** | Type `git commit -m "<quick statement describing incremental change>"`.  |
| 9. | ***YC*** | Type `git status` to understand what is committed, not committed, and not tracked. |
| 10. | ***YC*** | Type `git push <your_fork_remote_name> <branch-descriptive-name-of-your-change>`. In this workflow `<your_fork_remote_name>` is likely `origin`. |

*If you have extensive changes, then it is a good practice to *add*, *commit*, and *push* regularly so you don't loose work.*

***Ready to merge your new code with the central repo***
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***GG*** | Click ***Pull requests*** and select ***New pull requests***. You will see a GUI to decribe what which repo/branch that you want to move your specific repo/branch into:|   
|    |          | ***BASE*** Remote(Fork), Branch <<-- ***HEAD*** Remote(Fork), Branch|
|    |*probably*| solarsys <new_branch_name> <<-- fork of solarsys <new_branch>|
| 2. | ***GG*** | Click ***Submit*** and select reviewers. You may have instructions on this already or confer with the team to decide a policy.  |
| 3. | ***GG*** | Click ***Issues***, open "your" issue and a comment referencing your new *PR*. |
| 4. | ***GG*** | Interact with reviewers and other interested parties on github as much as possible in the *PR*. |
| 5. | ***YC*** | If you have new changes in response to the *PR* review before it is *merged*, then you can continue to *add*, *commit*, and *push* on your `<branch-descriptive-name-of-your-change>`. The associated *PR* will update automatically.|
| 6. | ***GG*** | If you have *Merge* privileges, confer with team on self-merge policy. |

For most cases you only need to change the branch on each side to match `<branch-descriptive-name-of-your-change>`.

***More advanced development*** The instrucitons outlined above can serves as first time use instructions and as a reference for the future. In addition, solarsys can be developed to add more complexity to the code with a richer desciprtion of our solar system. Finally, the solarsys project has room for more advanced practice of software carpentry tools: setup.py, version tagging, unit tests, code style requirements, json templating, and more.  

### Reference Materials: 
*For your implmentation of this template or in your future projects.*
- [solar system](https://solarsystem.nasa.gov/planets/in-depth/#the_new_definition_of_planet_otp)
- [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)
- [git cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [See ***Contributing*** and ***Developer Materials*** for detailed practices used by a community repo (scikit-beam)](https://scikit-beam.github.io/scikit-beam/ )
- [more git tutorials and examples](http://try.github.io/)
- [scikit-beam's cited resource for common git problems](http://sethrobertson.github.io/GitFixUm/fixup.html)
