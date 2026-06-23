**Git Basics Tutorial Plan**

**1. Introduction to Git**

- Explain what Git is and why it's useful for version control.
- Show examples of how teams and developers use Git for collaborative coding.
- Discuss repositories and commits as fundamental concepts.

**2. Setting Up a Repository**

- Navigate to a project folder and initialize a Git repository:

  ```
  git init
  ```

- Explain how Git starts tracking changes in the directory.

**3. Adding Changes to Staging**

- Modify or create a file, e.g., `README.md`.

- Add the file to the staging area:

  ```
  git add README.md
  ```

- Show the status of the repository:

  ```
  git status
  ```

- Explain the difference between the working directory, staging area, and commit history.

**4. Committing Changes**

- Create a commit with a meaningful message:

  ```
  git commit -m "Initial commit: Added README file"
  ```

- Explain that commits save snapshots of code changes.

**5. Pushing to a Remote Repository**

- Set up a remote repository (GitHub, GitLab, etc.).

- Link the local repository to the remote one:

  ```
  git remote add origin <remote_repo_URL>
  ```

- Push changes to the remote repository:

  ```
  git push -u origin main
  ```

- Explain how pushing allows others to access the latest version.

**6. Navigating Commit History**

- Show a list of previous commits:

  ```
  git log --oneline
  ```

- Move to an earlier commit using:

  ```
  git checkout <commit_hash>
  ```

- Explain how this is useful for debugging and tracking changes.

**7. Returning to Latest Version**

- If students checked out a previous commit, return to the latest version:

  ```
  git checkout main
  ```

- Reinforce why tracking commit history is crucial for code development.

**8. Reset your branch to that commit**

- Find the hash of your commit

  ```
  git reset --hard <commit_hash>
  ```

- This command **moves the HEAD back** to the specified commit and **deletes all newer commits**.

**9. Push the changes (if needed)**

- If this branch is already pushed to a remote repository and you want to **force** the reset on the remote as well:

  ```
  git push --force origin main
  ```

- Be careful with `--force`, as it rewrites history and removes commits for everyone working on the repository.
- Instead of deleting commits, you can **revert** the changes, while preserving the commit history:

    ```
    git revert HEAD
    ```

- This creates a **new commit** that reverses the changes made in the latest commit (HEAD), rather than deleting it.

    ```
    git revert HEAD~3
    ```

- This undoes the last 3 commits **without deleting history**, and creates three new commits, each reversing one of the last three commits.