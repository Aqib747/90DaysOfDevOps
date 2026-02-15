<h2>What is the difference between git add and git commit?</h2>
Ans -   git add - bascially select what goes into next commit, it takes content from the working directory and write into stagging area (index).
        git commit -bascially take whats in the staging area and file content is saved blobs and tree structure (object)  

<h2>What does the staging area do? Why doesn't Git just commit directly?</h2>
Ans - staging area, it give us the control what goes in the next commit ,it gives us flexibity to correct mistake before commit.

<h2>What information does git log show you?</h2>
<img width="1916" height="148" alt="Screenshot from 2026-02-15 09-54-02" src="https://github.com/user-attachments/assets/f885a61e-39e4-41cb-a420-ab49f230ed15" />

<h2>What is the .git/ folder and what happens if you delete it?</h2>
Ans - its is entire git database, No .git then no git and git will forget every thing about commit branches and history.

<h2>What is the difference between a working directory, staging area, and repository</h2>
Ans - working directory :- it will consist the real file which your editor modifies, Non trackable until added.
      Staging area - what will goes into your next commit, basically blue print of your next commit, we use git add
      repository - where data is stored in blobs and tree structure, we use git commit
