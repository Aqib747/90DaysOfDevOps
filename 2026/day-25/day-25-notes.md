
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
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7af6e290-8fc3-41b2-b972-056dc2b577cc" />
3. Check `git log` — is commit Y still in the history?

Yes


4. Answer in your notes:
   - How is `git revert` different from `git reset`?
     
## 🔄 Git Reset vs Git Revert (Core Difference)

| Command | Rewrites History | Safe After Push | Use Case |
|------|-----------------|----------------|---------|
| `git reset` | ❌ Yes | ❌ No | Local cleanup |
| `git revert` | ✅ No | ✅ Yes | Undo pushed commits |

**Golden Rule (DevOps):**
> If a commit is already pushed → **REVERT, don’t RESET**

- Why is revert considered **safer** than reset for shared branches?
   
   -
   Whhen would you use revert vs reset?
| Scenario                  | Best Choice  |
| ------------------------- | ------------ |
| Bad commit already pushed | `git revert` |
| CI/CD pipeline failure    | `git revert` |
| Production rollback       | `git revert` |
| Local unpushed mistake    | `git reset`  |

---

### Task 3: Reset vs Revert — Summary
Create a comparison in your notes:
## ⚖️ Git Revert vs Git Reset — Quick Comparison

| Feature | `git revert` | `git reset` |
|------|-------------|-------------|
| Rewrites history | ❌ No | ✅ Yes |
| Safe for pushed commits | ✅ Yes | ❌ No |
| Needs force push | ❌ No | ✅ Yes |
| Team friendly | ✅ Yes | ❌ No |
| Production safe | ✅ Yes | ❌ No |

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
# 🌿 Branching Strategies – DevOps Mastery Guide

Branching strategies define **how teams collaborate, integrate code, and release software safely and quickly**.

---

## 1️⃣ GitFlow

### 🔧 How it Works
GitFlow uses **multiple long-lived branches**, each serving a specific purpose in the release lifecycle.

### 🧱 Branches
- `main` – Production-ready code
- `develop` – Integration branch for features
- `feature/*` – New feature development
- `release/*` – Release preparation
- `hotfix/*` – Emergency production fixes


### 🏭 Where It’s Used
- Large enterprises
- Big teams
- Products with **scheduled releases**

### ✅ Pros
- Clear structure
- Controlled releases
- Stable production branch
- Easy role separation

### ❌ Cons
- Complex workflow
- Slower delivery
- Merge conflicts
- Overkill for small teams

### 🧠 DevOps Insight
GitFlow works best with **strong CI/CD automation**.  
Without automation, merge complexity increases.

---

## 2️⃣ GitHub Flow

### 🔧 How it Works
GitHub Flow is **simple and fast** with only one long-lived branch.

- `main` is always deployable
- All work happens in short-lived feature branches
- Changes are merged via Pull Requests

### 🔁 Flow Diagram

### 🏭 Where It’s Used
- Large enterprises
- Big teams
- Products with **scheduled releases**

### ✅ Pros
- Clear structure
- Controlled releases
- Stable production branch
- Easy role separation

### ❌ Cons
- Complex workflow
- Slower delivery
- Merge conflicts
- Overkill for small teams

### 🧠 DevOps Insight
GitFlow works best with **strong CI/CD automation**.  
Without automation, merge complexity increases.

---

## 2️⃣ GitHub Flow

### 🔧 How it Works
GitHub Flow is **simple and fast** with only one long-lived branch.

- `main` is always deployable
- All work happens in short-lived feature branches
- Changes are merged via Pull Requests

### 🔁 Flow Diagram
main ──●────●────●────●────▶
\ \
feature feature feature


### 🏭 Where It’s Used
- Startups
- SaaS products
- Continuous delivery teams

### ✅ Pros
- Simple and clean
- Faster development
- Easy onboarding
- CI/CD friendly

### ❌ Cons
- Requires strong testing
- Risky without discipline
- No dedicated release branch

### 🧠 DevOps Insight
GitHub Flow **assumes**:
- Automated tests
- Code reviews
- Frequent deployments

---

## 3️⃣ Trunk-Based Development

### 🔧 How it Works
All developers integrate changes **directly or near-directly** into `main`.

- No long-lived branches
- Feature branches last hours or days
- Feature flags are commonly used

### 🔁 Flow Diagram
main ──●─●─●─●─●─●─●─▶


### 🏭 Where It’s Used
- High-scale engineering teams
- Companies deploying multiple times per day
- Mature DevOps organizations

### ✅ Pros
- No merge hell
- Fastest delivery
- Continuous integration by design
- High deployment frequency

### ❌ Cons
- Requires excellent test coverage
- Needs feature flags
- High engineering discipline

### 🧠 DevOps Insight
This is the **end-game DevOps strategy**.  
If CI fails, **everyone stops and fixes it**.

---

## ⚖️ Strategy Comparison

| Strategy | Complexity | Delivery Speed | Best For |
|--------|------------|----------------|----------|
| GitFlow | High | Slow | Large enterprises |
| GitHub Flow | Medium | Fast | Startups, SaaS |
| Trunk-Based Development | Low (concept) / High (discipline) | Fastest | Mature DevOps teams |

---

## 🎯 Strategy Selection Answers

### 🚀 Startup Shipping Fast
**Recommended:** GitHub Flow  
**Reason:** Simple, fast, minimal process, easy CI/CD integration

### 🏢 Large Team with Scheduled Releases
**Recommended:** GitFlow  
**Reason:** Controlled releases, clear stabilization phase

### 🌍 Open-Source Projects
**Common Choice:** GitHub Flow (or Trunk-like)  
**Reason:** PR-based workflow, `main` always deployable

---

## 🧠 How a DevOps Engineer Chooses a Strategy

A DevOps engineer evaluates:
1. Deployment frequency
2. CI/CD maturity
3. Team size
4. Stability requirements

Then chooses the strategy accordingly.

---

## 🧠 One-Line Memory Rules

- **GitFlow** → Control & predictability  
- **GitHub Flow** → Speed & simplicity  
- **Trunk-Based Development** → Continuous delivery excellence  

---

## 💼 Interview-Ready Answer

> “For startups, I prefer GitHub Flow due to its simplicity and fast delivery.  
> For large teams with scheduled releases, GitFlow provides better structure.  
> In mature DevOps environments with strong CI/CD, Trunk-Based Development is the most efficient.”

----------------------------------------------------------------------------------------------------------

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

