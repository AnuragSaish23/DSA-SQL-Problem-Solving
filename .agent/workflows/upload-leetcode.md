---
description: Upload daily LeetCode problems to GitHub from Google Sheet
---

# Daily LeetCode Upload Workflow

## Overview
Upload new LeetCode problems from Google Sheet to the DSA-SQL-Problem-Solving GitHub repository.

## Resources
- **Google Sheet**: https://docs.google.com/spreadsheets/d/1vVw7-1CbBgFVlLsDAS7xR8o5LvN9qrUtsT6bW4qIA9k/edit?usp=sharing
- **GitHub Repo**: https://github.com/AnuragSaish23/DSA-SQL-Problem-Solving
- **Local Clone**: C:\Users\druma\.gemini\antigravity\scratch\DSA-Problem-Solving

## Sheet Structure
The Google Sheet contains columns:
- Date | Problem | Link | Data Structure | Difficulty | Solution | SQL Problem | SQLLink | PDifficulty | Remarks

## Daily Problems
User solves 4 problems daily:
- 2 DSA problems (Python)
- 2 SQL problems

## Steps

// turbo
1. Read the Google Sheet CSV export:
   ```
   https://docs.google.com/spreadsheets/d/1vVw7-1CbBgFVlLsDAS7xR8o5LvN9qrUtsT6bW4qIA9k/export?format=csv
   ```

2. Identify NEW problems (check by date or compare with existing notebooks in repo)

3. For each new DSA problem:
   - Extract problem number from LeetCode URL
   - Create notebook: `{number}-{problem-name-slug}.ipynb`
   - Place in correct folder: `Arrays|Strings/{Easy|Medium|Hard}/`
   - Include: Problem description, approach, Python solution, complexity analysis

4. For each new SQL problem:
   - Extract problem number from LeetCode URL
   - Create notebook: `{number}-{problem-name-slug}.ipynb`
   - Place in: `SQL/{Easy|Medium|Hard}/`
   - Include: Problem description, approach, SQL solution

// turbo
5. Pull latest changes:
   ```powershell
   cd C:\Users\druma\.gemini\antigravity\scratch\DSA-Problem-Solving
   git pull origin main
   ```

6. Stage all new files:
   ```powershell
   git add -A
   ```

7. Commit with message like: "Add problems for YYYY-MM-DD (2 DSA + 2 SQL)"

8. Push to GitHub:
   ```powershell
   git push origin main
   ```

9. **Update README.md** with new problems:
   - Update folder problem counts in the Repository Structure section
   - Add new entries to the Problems Solved tables (Arrays-Easy, Strings-Easy, SQL-Easy, etc.)
   - Format: `| Problem Name | \`{number}-{problem-slug}.ipynb\` |`

## Notebook Template (DSA)

**IMPORTANT:** For DSA problems, include ALL applicable solution approaches:
1. **Brute Force** - The most intuitive but inefficient solution
2. **Better** - An improved approach (if applicable)
3. **Optimal** - The most efficient solution

Skip an approach only if it doesn't exist (e.g., some problems have same brute and optimal).

```json
{
  "cells": [
    {"cell_type": "markdown", "source": ["# Problem Title (LeetCode #XXX)\n\n## Problem Description\n..."]},
    
    {"cell_type": "markdown", "source": ["## Approach 1: Brute Force\n\n**Intuition:** ...\n\n**Algorithm:** ..."]},
    {"cell_type": "code", "source": ["# Brute Force Solution\nclass Solution:\n    def solve(self, ...):\n        ..."]},
    {"cell_type": "markdown", "source": ["**Complexity Analysis (Brute Force):**\n- Time: O(...)\n- Space: O(...)"]},
    
    {"cell_type": "markdown", "source": ["---\n## Approach 2: Better\n\n**Intuition:** ...\n\n**Algorithm:** ..."]},
    {"cell_type": "code", "source": ["# Better Solution\nclass Solution:\n    def solve(self, ...):\n        ..."]},
    {"cell_type": "markdown", "source": ["**Complexity Analysis (Better):**\n- Time: O(...)\n- Space: O(...)"]},
    
    {"cell_type": "markdown", "source": ["---\n## Approach 3: Optimal\n\n**Intuition:** ...\n\n**Algorithm:** ..."]},
    {"cell_type": "code", "source": ["# Optimal Solution\nclass Solution:\n    def solve(self, ...):\n        ..."]},
    {"cell_type": "markdown", "source": ["**Complexity Analysis (Optimal):**\n- Time: O(...)\n- Space: O(...)"]},
    
    {"cell_type": "markdown", "source": ["## Summary\n| Approach | Time | Space |\n|----------|------|-------|\n| Brute Force | O(...) | O(...) |\n| Better | O(...) | O(...) |\n| Optimal | O(...) | O(...) |"]}
  ]
}
```

## Notebook Template (SQL)
```json
{
  "cells": [
    {"cell_type": "markdown", "source": ["# Problem Title (LeetCode #XXX)\n\n## Problem Description\n..."]},
    {"cell_type": "markdown", "source": ["## Approach\n..."]},
    {"cell_type": "code", "source": ["# SQL Solution\nsql_query = \"\"\"\nSELECT ...\n\"\"\""]},
    {"cell_type": "markdown", "source": ["## Complexity Analysis\n..."]}
  ]
}
```
