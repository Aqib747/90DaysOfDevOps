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

A merge conflict occurs when Git cannot automatically combine changes from two branches during a merge because the same part of a file was modified differently in each branch.<br><br>

Git tries to merge changes automatically most of the time.<br>

But if both branches change the same line (or overlapping lines) in a file, Git doesn’t know which change to keep.<br>

Git pauses the merge and marks the conflicting sections in the file for you to resolve manually.<br>

<<<<<<< HEAD → your branch’s version

======= → separator

 >>>>>>>> feature-login → the other branch’s version

A merge conflict occurs when Git cannot automatically merge two branches because the same part of a file was changed differently, requiring manual resolution.

<h1> Task 2: Git Rebase — Hands-On</h1>

<h2>Create a branch feature-dashboard from main, add 2-3 commits

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4b977477-226c-400f-a16b-5b6c0b1254fd" />
While on main, add a new commit (so main moves ahead)</h2>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c0804a1a-a7f8-4f87-b888-5ec474704033" />





<h2>Switch to feature-dashboard and rebase it onto main
Observe your git log --oneline --graph --all — how does the history look compared to a merge?</h2>
before rebase the commit history
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5db8664c-7f03-4ad2-bcdb-2bd47efa6aa3" />
after rebase commit history
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/90ec9bc7-c4f2-4baf-93a4-e5dce6fec8e9" />

<h1>Answer in your notes:</h1>
<h2>What does rebase actually do to your commits?</h2>
1.Takes your commits from your current branch that are not in the target branch (e.g., master).<br>
2.“Reapplies” them one by one on top of the target branch.<br>
3.Creates new commits with new hashes — they are essentially the same changes, but Git treats them as new commits.<br>
4.Linearizes history — no merge commits are needed if there are no conflicts.<br>
<h2>How is the history different from a merge?</h2>
1️⃣ Merge

Combines two branches by creating a merge commit.

Preserves the true history of both branches.

History looks like a Y-shape when branches diverge and then merge.<br>
2️⃣ Rebase

Moves your feature branch commits on top of another branch.

Rewrites history to make it linear.

No merge commit is created (unless conflicts occur). <br>
✅ One-line summary: <br>

Merge preserves branch history with a merge commit; rebase rewrites commits on top of another branch to make history linear.

<h2>Why should you never rebase commits that have been pushed and shared with others?</h2>
When would you use rebase vs merge?
Rebase rewrites history — it creates new commits with new hashes.<br>

If you’ve already pushed commits to a shared repository:<br>

Other developers may have based their work on your old commits.<br>

Rebasing changes the commit hashes, so their history no longer matches yours.<br>

This can cause confusion, conflicts, or require forced pushes, which is dangerous in team environments.<br>

✅ Rule of thumb:<br>
Only rebase local or private branches that others haven’t pulled yet.


<h1>Task 3: Squash Commit vs Merge Commit</h1>
<h2>Create a branch feature-profile, add 4-5 small commits (typo fix, formatting, etc.)
Merge it into main using --squash — what happens?</h2>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e92c15d6-100b-484c-8d57-cf56451fdf69" />


<h2>Check git log — how many commits were added to main?,</h2>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/09e9f087-60af-4380-942e-f6c5feae2ab0" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0ccbd70a-22f5-4f2b-9f2a-75311b99a869" />

<h2>Now create another branch feature-settings, add a few commits
Merge it into main without --squash (regular merge) — compare the history</h2>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e973b2a3-b467-4b75-b406-56d54c0d772a" />


<h1> Answer in your notes:</h1>

<h2>What does squash merging do?</h2>
Answer - A squash merge takes all commits from a feature branch and compresses (squashes) them into ONE single commit, then applies that commit to the target branch (usually main).<br>
👉 The individual commit history from the feature branch does not appear in main.

When would you use squash merge vs regular merge?

✅ Use squash merge when:

Feature branch has messy or WIP commits

“fix typo”

“oops”

“try again”

You want clean, readable main history

Each PR should map to one logical change

Working in large teams

Repo follows “one PR = one commit” philosophy

🧠 Common in:

GitHub PR workflows

Product teams

Fast-moving startups

✅ Use regular merge when:

Commit history itself is important

Each commit represents a meaningful step

You may need to revert or cherry-pick specific commits

Debugging or auditing is critical

🧠 Common in:

Open-source projects

Infrastructure repos

Long-running feature branches



<h2>What is the trade-off of squashing?</h2>

Trade-offs of squashing (VERY IMPORTANT)
❌ What you lose with squash merge:
1️⃣ Commit-level history

You can’t see:

.How the feature evolved

.Intermediate fixes

.Step-by-step reasoning

.Debugging “who broke what” becomes harder.

2️⃣ Granular reverts are impossible

With squashed commits:

.You can only revert the entire feature

.You can’t revert just one bad commit

3️⃣ Blame becomes less precise

git blame will show:

.One author

.One commit
.Instead of multiple contributors/changes

4️⃣ Original commit SHAs are lost

.You cannot reference old commit hashes

.Cherry-picking from the squashed history is not possible


<h1>Task 4: Git Stash — Hands-On </h1>

Start making changes to a file but do not commit
Now imagine you need to urgently switch to another branch — try switching. What happens?
Use git stash to save your work-in-progress
Switch to another branch, do some work, switch back
Apply your stashed changes using git stash pop
Try stashing multiple times and list all stashes
Try applying a specific stash from the list


<h1>Answer in your notes:</h1>
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
