# Minimal Terminal Guide

This is the absolute minimum you need to navigate a terminal and work with tools like Claude Code.

---

## 1. Create a Directory

```bash
mkdir myproject
```

---

## 2. Change Directory

```bash
cd myproject     # go into a folder
cd ..            # go up one level
cd ~             # go to your home directory
cd ./someDirectory   # folder inside the current directory
cd ~/Documents   # absolute path from home
```

Special paths:
- `.`  = current directory
- `..` = parent directory
- `~`  = home directory

---

## 3. List Files

```bash
ls        # list contents
ls -la    # detailed listing (optional)
```

---

## 4. Open Current Folder (macOS)

```bash
open .    # opens current directory in Finder
open file.txt
```

---

## Optional but Handy

```bash
pwd       # show where you are
./somefile.sh  # run a script in the current folder
```

---

## TL;DR

```bash
mkdir someDirectory
cd someDirectory
cd ..
cd ~
ls
open .
```
