Challenge Tasks
Task 1: Git Merge — Hands-On

Create a new branch feature-login from main, add a couple of commits to it


Switch back to main and merge feature-login into main
Observe the merge — did Git do a fast-forward merge or a merge commit?
Now create another branch feature-signup, add commits to it — but also add a commit to main before merging
Merge feature-signup into main — what happens this time?
Answer in your notes:
What is a fast-forward merge?
When does Git create a merge commit instead?
What is a merge conflict? (try creating one intentionally by editing the same line in both branches)
Task 2: Git Rebase — Hands-On
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
