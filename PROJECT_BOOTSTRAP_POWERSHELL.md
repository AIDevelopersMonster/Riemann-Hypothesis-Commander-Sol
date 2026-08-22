# Repository creation - Windows PowerShell

Assumes the ZIP was unpacked to:

`C:\Users\CHUWI\Documents\GitHub\Riemann-Hypothesis-Commander-Sol`

## Option A - GitHub CLI (`gh`) installed

```powershell
cd "C:\Users\CHUWI\Documents\GitHub\Riemann-Hypothesis-Commander-Sol"

git init
git add .
git commit -m "Initialize RH-SOL research programme"
git branch -M main

gh repo create AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol `
  --public `
  --source . `
  --remote origin `
  --push
```

Check:

```powershell
git status -sb
git remote -v
gh repo view --web
```

## Option B - create empty repository in GitHub web first

Create an **empty** public repository named:

`Riemann-Hypothesis-Commander-Sol`

Do not initialize it with README/LICENSE/.gitignore because they are already in this scaffold.

Then:

```powershell
cd "C:\Users\CHUWI\Documents\GitHub\Riemann-Hypothesis-Commander-Sol"

git init
git add .
git commit -m "Initialize RH-SOL research programme"
git branch -M main
git remote add origin https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol.git
git push -u origin main
```

## First research branch

```powershell
git switch -c agent/rh-sol-02-shift
```

Recommended first commit:

```powershell
git add .
git commit -m "Open RH-SOL-02 shifted-lattice spectroscopy"
git push -u origin agent/rh-sol-02-shift
```
