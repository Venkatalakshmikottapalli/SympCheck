# Git Workflow for SympCheck Project

This README file provides the essential Git commands used in the development process of the SympCheck project.

## Branching Strategy

### 1. Check Current Branch
```bash
git branch
```
-  Lists all branches and highlights the current branch.

### 2. Switch to `master` Branch
```bash
git checkout master
```
-  Switches to the `master` branch, which holds the production-ready code.

### 3. Create a `develop` Branch
```bash
git checkout -b develop
```
-  Creates a new `develop` branch from `master` and switches to it.

### 4. Push `develop` Branch to GitHub
```bash
git push -u origin develop
```
-  Pushes the `develop` branch to the remote repository and sets it to track the remote `develop` branch.

## Development Workflow

### 5. Stage All Changes
```bash
git add .
```
-  Stages all changes in the working directory for the next commit.

### 6. Commit Changes
```bash
git commit -m "Your commit message"
```
-  Commits the staged changes with a descriptive message.

### 7. Push Changes to `develop` Branch
```bash
git push origin develop
```
-  Pushes the committed changes in the `develop` branch to the remote repository.

## Merging `develop` into `master` for Production

### 8. Switch to `master` Branch
```bash
git checkout master
```
-  Switches back to the `master` branch before merging.

### 9. Pull Latest Changes from `master`
```bash
git pull origin master
```
-  Updates the local `master` branch with the latest changes from the remote repository.

### 10. Merge `develop` into `master`
```bash
git merge develop
```
-  Merges the `develop` branch into `master`, incorporating the new features or fixes.

### 11. Push Merged `master` to GitHub
```bash
git push origin master
```
-  Pushes the updated `master` branch to the remote repository to update production code.

## Resuming Development

### 12. Switch Back to `develop` Branch
```bash
git checkout develop
```
-  Switches back to the `develop` branch to continue working on new features or fixes.



