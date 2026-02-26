
## Challenge Tasks

### Task 1: Git Reset — Hands-On
1. Make 3 commits in your practice repo (commit A, B, C)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b943f1c1-1f1d-4d6d-8f67-38ebefdb152f" />

2. Use `git reset --soft` to go back one commit — what happens to the changes?
Before
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a5c6b987-2a46-41ba-a03d-dc6c6468ac0d" />
After
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7233940f-2fad-4e89-afe7-f4dab83c2215" />

What just happened? 
📌 Meaning

“Undo the commit and let me decide what to stage again.”

❌ Commit C removed from history

✅ Changes from commit C are still staged

❌ File NOT changed??????
Before reset
Commit C: line C
Commit B: line B
Commit A: line A

File content:
line A
line B
line C

After git reset --soft HEAD~1
HEAD → Commit B

Staging area: still has "line C"
Working file: still has "line C"


So when you run:

cat reset-demo.txt


👉 Git just shows the file as-is
👉 Git does NOT auto-remove file content

-------------------------------------------------------------------------------------------------------------------
3. Re-commit, then use `git reset --mixed` to go back one commit — what happens now?
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8588aff0-b1c0-4964-aef0-eb32d3dc7672" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7ab7ab4b-4bd6-473d-880c-50771b471a24" />

What happened now?

❌ Commit removed

❌ Changes unstaged

✅ File still modified

📌 Meaning

“Undo the commit and let me decide what to stage again."
---------------------------------------------------------------------------------------------------------------
4. Re-commit, then use `git reset --hard` to go back one commit — what happens this time?
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6b81bf20-2b0c-4784-8bb1-accb8100a1b8" />
What happened this time?

❌ Commit removed

❌ File changes removed

❌ Nothing staged

❌ Data gone forever

📌 Meaning

“I don’t care. Delete the commit AND the changes.”

⚠️ THIS IS DESTRUCTIVE
------------------------------------------------------------------------------------------------------------------
5. Answer in your notes:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   | Mode      | Commit      | Staging Area | Working Directory |
| --------- | ----------- | ------------ | ----------------- |
| `--soft`  | ❌ removed  | ✅ kept      | ✅ kept           |
| `--mixed` | ❌ removed  | ❌ cleared   | ✅ kept           |
| `--hard`  | ❌ removed  | ❌ cleared   | ❌ cleared        |

------------------------------------------------------------------------------------------------------------------
 
 - Which one is destructive and why?

❌ git reset --hard

Deletes commits

Deletes file changes

No recovery (unless reflog)

- When would you use each one?

🧰 When to use each?

✅ --soft

Use when:

You want to edit commit message

Combine commits (squash manually)

✅ --mixed

Use when:

You committed too much

Want to re-stage selectively

⚠️ --hard

Use when:

You want to completely discard work

Cleaning a broken local state

💼 Interview Gold Line

“git reset moves HEAD backward. --soft keeps changes staged, --mixed keeps them unstaged, and --hard deletes everything. Never use reset on pushed commits in shared branches.”
------------------------------------------------------------------------------------------------------------
- Should you ever use `git reset` on commits that are already pushed?

❌ NO (in shared branches)

Why?

Rewrites history

Breaks teammates’ repos

Causes merge chaos

✅ OK only when:

Commit is local

Branch is private

You know exactly what you’re doing
------------------------------------------------------------------------------------------------------------------- 
### Task 2: Git Revert — Hands-On
1. Make 3 commits (commit X, Y, Z)
2. Revert commit Y (the middle one) — what happens?
3. Check `git log` — is commit Y still in the history?
4. Answer in your notes:
   - How is `git revert` different from `git reset`?
   - Why is revert considered **safer** than reset for shared branches?
   - When would you use revert vs reset?

---

### Task 3: Reset vs Revert — Summary
Create a comparison in your notes:

| | `git reset` | `git revert` |
|---|---|---|
| What it does | ? | ? |
| Removes commit from history? | ? | ? |
| Safe for shared/pushed branches? | ? | ? |
| When to use | ? | ? |

---

### Task 4: Branching Strategies
Research the following branching strategies and document each in your notes with:
- How it works (short description)
- A simple diagram or flow (text-based is fine)
- When/where it's used
- Pros and cons

1. **GitFlow** — develop, feature, release, hotfix branches
2. **GitHub Flow** — simple, single main branch + feature branches
3. **Trunk-Based Development** — everyone commits to main, short-lived branches
4. Answer:
   - Which strategy would you use for a startup shipping fast?
   - Which strategy would you use for a large team with scheduled releases?
   - Which one does your favorite open-source project use? (check any repo on GitHub)

---

### Task 5: Git Commands Reference Update
Update your `git-commands.md` to cover everything from Days 22–25:
- Setup & Config
- Basic Workflow (add, commit, status, log, diff)
- Branching (branch, checkout, switch)
- Remote (push, pull, fetch, clone, fork)
- Merging & Rebasing
- Stash & Cherry Pick
- Reset & Revert

---

## Hints
- `git reflog` is your safety net — it shows everything Git has done, even after a hard reset
- For branching strategies, look at how projects like Kubernetes, React, or Linux kernel manage branches

---

## Submission
1. Add your `day-25-notes.md` to `2026/day-25/`
2. Update `git-commands.md` — commit and push
3. Push to your fork

---

## Learn in Public

Share your Reset vs Revert comparison or your branching strategy notes on LinkedIn.

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**

