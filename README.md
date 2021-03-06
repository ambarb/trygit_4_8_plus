# trygit-4-8-plus
A simple mock up of a modular, nested python package for group collaboration without 8 people editing the same file.

## How to Use trygit-4-8-plus 
* `solarsys` is meant to represent a standalone ***repo***sitory
* it is incomplete and imperfect by design but provides a "sandbox" to practice software development
* use `trygit-4-8-plus` as a template to create your custom repo for a customized team experience
* These participant instructions are designed assuming your new repo name is `solarsys`, but `<central_repo>` has been used in the text below to provide easier editing for customization.
 
# solarsys
A simple mock up of a modular, nested python ***repo***sitiory for group collaboration. The `<repo_name>` project is a sandbox for gaining experience with collaborative coding projects and provides opportunites to develop and practice more advanced skills.  
 
## Instructions for using solarsys to learn more about git
*See the bottom of this document to find some common **Reference Materials**.* 
### Requirements
- Each participant has a github account
- Each participant has git installed on their computer
- Each participant has python on their computer 
- Team messaging platform if working remotely
- Link from organizer to the team's custom repo with additional instructions --> `<team_name>/<repo_name>`
### Abbreviations
- Group Git webpage of the central repo (**GG**)
- Your Git webpage of forked repo (**YG**)
- Your Computer (**YC**)


### Step by step
*Check ***YG***, ***GG***, and `git status` in between steps as you go to underand how git works.*

***Getting a local copy for future contributions via git***
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***GG*** | With the provided link, click ***Fork*** (top left) and select your github username. |
| 2. | ***YG*** | Click ***Clone or Download*** and copy the the URL in the pop-up window. |
| 3. | ***YC*** | Open terminal window and navigate to where you want to save this repo. |
| 4. | ***YC*** | Type `git clone <paste_copied_url>`. `<paste_copied_url>` is something like `https://github.com/<your_git_uid>/<repo_name>.git`. |
| 5. | ***YC*** | Type `cd <repo_name>`. You should find `solarsys.py` in this directory level. |
| 6. | ***YC*** | Type `git remote add <repo_name> git://github.com/<team_name>/<repo_name>.git`.  You can copy the link from *GG* like in set 2. |
| 7. | ***YC*** | Type `git remote -v`. Note the remote names represent what is on github.com. |

Now your computer is setup to track your remote fork (default `origin` or generically `<your_fork_remote_name>`) and the remote central repo (`<repo_name>`). You can change the names representing the remotes if more convenient for you.  But this tutorial assumes you have not done this.

***Test the library by starting a python session and importing the library.*** No python packaging has been performed. If you are having trouble, maybe an ***Issues*** exists on the ***GG*** that you can use.

***Things to know before you start changing files***
- Do not locally *commit* and *push* changes to the central repo. Use your fork for this purpose.
- Git commands to check things before committing: `git status`, `git remote -v`, and `git branch`.
- Use `git commit` and `git push` regulary to track incremental changes for your future self and backup your work.
- If you get stuck or confused, see the links at the bottom for more details, but `git rm` can be useful if you *commit* something by accident.

***Starting local contributions and submitting them using a feature branch*** 
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***GG*** | Use ***Issues*** link to identify potential problems to help solve or start an *issue* on something you would like to contribute.|
| 2. | ***GG*** | If an issue is not assigned to you, then pick/[create](https://help.github.com/en/github/managing-your-work-on-github/opening-an-issue-from-code) an issue and self assign using the web interface. |
| 3. | ***YC*** | Here, we skip making sure both remote master branches are up to date locally. We will practice this later. |
| 4. | ***YC*** | Type`git branch <descriptive-name-of-your-change>` to create a new branch (or editable "copy"). Type `git branch`. Where is `*`?|
| 5. | ***YC*** | Type `git checkout <descriptive-name-of-your-change>` to switch to the new feature branch. Type `git branch`. See change in `*`.|
| 6. | ***YC*** | Start making changes and testing them as you go. |
| 7. | ***YC*** | Type `git add <filename.py>` to organize the files you have changed/created and would like to *commit*. |
| 8. | ***YC*** | Type `git status` to understand what is committed, not committed, and not tracked. Note your current branch from output.|
| 9. | ***YC*** | Type `git commit -m "<quick statement describing incremental change>"` to commit to your "feature branch" |
| 10. | ***YC*** | Type `git status` to understand what is committed, not committed, and not tracked. Note your current branch from output.|
| 11. | ***YC*** | Type `git push <your_fork_remote_name> <descriptive-name-of-your-change>`. In this workflow `<your_fork_remote_name>` is likely `origin`. |

*If you have extensive changes, then it is a good practice to *add*, *commit*, and *push* regularly so you don't lose work.*

***Ready to merge your new code with the central repo on github.com***
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***YG*** | There are multiple ways.  The easiest to explain is click ***Pull requests*** and select ***New pull requests***.  You will see a GUI to decribe which repo/branch (base) that accept new changes from your forked repo/branch. With the right most dropdown, select your pushed "feature branch" instead of "master".|   
|    |          | ***BASE*** Remote(Fork), Branch  <<--  ***HEAD*** Remote(Fork), Branch|
|    |*probably*| `<repo_name> master` <<-- `<forked_solarsys> <descriptive-name-of-your-change>`|
| 2. | ***YG*** | Click ***Create pull request***. [Add](https://help.github.com/en/github/writing-on-github/autolinked-references-and-urls) more details (like referencing issue). Select ***Create pull request***. |
| 3. | ***GG*** | You will be routed to ***Pull requests*** of the central repo. Select reviewers. You may have instructions on this already or confer with the team to decide a policy.  |
| 4. | ***GG*** | Click ***Issues***, open "your" issue and [add](https://help.github.com/en/github/writing-on-github/autolinked-references-and-urls) comment referencing your new *PR*. |
| 5. | ***GG*** | Interact with reviewers and other interested parties on github as much as possible in the *PR*. |
| 6. | ***YC*** | If you have new changes in response to the *PR* review before it is *merged*, then you can continue to *add*, *commit*, and *push* on your `<branch-descriptive-name-of-your-change>`. The associated *PR* will update automatically.|
| 7. | ***GG*** | If you have ***Merge*** privileges, then confer with team on its self-merge policy. |

***Practice code reviews on central repo***
For private repos, there may be not notifciation on a request to review.  In this case, navigate to the central repo's github page (***GG***) and select ***Pull requests***.  You may see your avatar on the right.  Additionally, you can hover over each PR link to see if you have been assigned something.  Click on those links and the next steps will most likely be highlighted.

***Updating local repos to match most current version of the central repo as seen on github.com***
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***YC*** | Type `git remote -v` to remind yourself of the remote names of the central repo and your fork of it. |
| 2. | ***YC*** | Type `git fetch <remote_name_central_repo>`. |
| 3. | ***YC*** | Type `git checkout master` to switch to your fork's local master branch.|
| 4. | ***YC*** | Type `git merge <remote_name_central_repo>/master` to update your fork's local master branch. |
| 5. | ***YC*** | Type `git push <remote_name_fork_of_central> master` to update the github version with the local version of your fork's master branch.  Now the github master branches of the central repo and your fork are identical. |

From here, further development is easiest if you create new central branches instead of using older ones.  `git branch -d <feature_branch>` can be used to clean up the display of your local feature branches.  

***Updating an in progress feature branch with the central repo as seen on github.com***
*This is usually not required and the method here is probably not recommended by professionals. This task can get complicated, especially if changing the same file (and more so the same lines). If you proceed with this method, then you will lose uncomitted changes.  Professionals will `rebase` instead and this method may create unwanted issue.  The good news is that this repo is designed to make a mess and learn how git works!*
| Step No. | Where | Instruction |
| -- | ----- | ----------- |
| 1. | ***YC*** | Complete the steps above to make sure both remote master branches match (central repo and fork of central repo). |
| 2. | ***YC*** | Use `git checkout <feature_branch_name>` and make you have committed all of your changes that you want to retain. |
| 3. | ***YC*** | Type `git push <remote_name_fork_of_central> master` and edit the merge request (vi editor). Upon closing and saving of this file, the feature branch will be updated. |

***More advanced development*** The instructions outlined above can be used as a reference in the future. In addition, this project can be developed to add more complexity to the code with a richer description of our solar system or provide enhanced functionality (display pretty tables or create binder website). Finally, this project has room for more advanced practice of software carpentry skills: python packaging, version tagging, unit tests, code style requirements, json templating, and more.  

## Take home 
1. Typically there is never a need to pull from your fork's remote master.
2. Never push to the central repo's remote master. Use ***Pull requests*** after pushing your fork's feature branch to its remote.
3. If you are instructed by git to `rebase`, decline if possible and research futher.  See `scikit-beam`s recommendations as a starting point for its discussion.  Use `rebase` instead of pulling from the central repo's master branch to your fork's feature branch.

### Reference Materials: 
*For your implementation of this template or in your future projects.*
- [solar system](https://solarsystem.nasa.gov/planets/in-depth/#the_new_definition_of_planet_otp)
- [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)
- [git cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [See ***Contributing*** and ***Developer Materials*** for detailed practices used by a community repo (scikit-beam)](https://scikit-beam.github.io/scikit-beam/ )
- [scikit-beam's cited resource for common git problems](http://sethrobertson.github.io/GitFixUm/fixup.html)
- [more git tutorials and examples](http://try.github.io/)
- [configure upstream repo remote (central branch master)](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)
- [update (sync) your local fork master from remote central branch master](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
- [update (sync) your remote fork to your synced local fork](https://help.github.com/en/github/using-git/pushing-commits-to-a-remote-repository)
