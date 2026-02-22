<h1>Challenge Tasks</h1>

<h1>Task 1: Git Merge — Hands-On</h1>

<h2>Create a new branch feature-login from main, add a couple of commits to it</h2>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/62e6760d-a766-41e0-816c-79372e2c440b" />

<h2>Switch back to main and merge feature-login into main
Observe the merge — did Git do a fast-forward merge or a merge commit?</h2>

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c6e09021-5cec-4c69-8d47-18be963f5fc9" />
. Git explicitly says  "Merge made by 'ort' startergy"<br>
. it did not say fast forward<br>
. The ort strategy (new default since Git 2.34) handled the merge automatically<br>
. This was a true merge commit (three-way merge), not a fast-forward, because both master and feature-login had independent commits when merged.<br>


<h2>Now create another branch feature-signup, add commits to it — but also add a commit to main before merging
Merge feature-signup into main — what happens this time?</h2>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/53115a60-3fa8-4dfa-9d4c-736813d0b821" />
. Fast forward merge - git realised master has no new commit since feature-signup branch created, this means it just can master pointer forward to the same commit feature-signup <br>



<h1>Answer in your notes:</h1>
<h2>What is a fast-forward merge?</h2>
 Answer - A fast-forward merge happens when the branch you are merging has all the new commits ahead of the current branch, and the current branch has no new commits since the branch diverged.<br>

In this case, Git does not create a merge commit. It simply moves the branch pointer forward to the latest commit of the feature branch.


<h2>When does Git create a merge commit instead?</h2>
 Answer -Git creates a merge commit (true three-way merge) when: <br><br>

Both branches have independent commits since they diverged.<br>
Git cannot just slide the pointer forward, because the histories need to be combined.<br>
The merge commit has two parent commits — one from each branch.<br>
This preserves the history of both branches.<br>

<h2>What is a merge conflict? (try creating one intentionally by editing the same line in both branches)</h2>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/31483a53-507a-4209-9ad7-38c9932a29b8" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ef656ac2-7b2d-40fa-b133-9d4c4ebade4c" />


<h1> Task 2: Git Rebase — Hands-On</h1>

Create a branch feature-dashboard from main, add 2-3 commits
While on main, add a new commit (so main moves ahead)
Switch to feature-dashboard and rebase it onto main
Observe your git log --oneline --graph --all — how does the history look compared to a merge?
Answer in your notes:
What does rebase actually do to your commits?
How is the history different from a merge?
Why should you never rebase commits that have been pushed and shared with others?
When would you use rebase vs merge?
Task 3: Squash Commit vs Merge Commit
Create a branch feature-profile, add 4-5 small commits (typo fix, formatting, etc.)
Merge it into main using --squash — what happens?
Check git log — how many commits were added to main?
Now create another branch feature-settings, add a few commits
Merge it into main without --squash (regular merge) — compare the history
Answer in your notes:
What does squash merging do?
When would you use squash merge vs regular merge?
What is the trade-off of squashing?
Task 4: Git Stash — Hands-On
Start making changes to a file but do not commit
Now imagine you need to urgently switch to another branch — try switching. What happens?
Use git stash to save your work-in-progress
Switch to another branch, do some work, switch back
Apply your stashed changes using git stash pop
Try stashing multiple times and list all stashes
Try applying a specific stash from the list
Answer in your notes:
What is the difference between git stash pop and git stash apply?
When would you use stash in a real-world workflow?
Task 5: Cherry Picking
Create a branch feature-hotfix, make 3 commits with different changes
Switch to main
Cherry-pick only the second commit from feature-hotfix onto main
Verify with git log that only that one commit was applied
Answer in your notes:
What does cherry-pick do?
When would you use cherry-pick in a real project?
What can go wrong with cherry-picking?
