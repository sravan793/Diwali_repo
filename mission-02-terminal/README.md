# Mission 2 — Terminal and file management

## 1. Task / objective
Practise basic Terminal commands and safely create, display, copy and rename files inside this repository.

## 2. Work completed
Use a practice directory inside the repository only. Suggested commands:

**Important:** Run `mkdir terminal-practice` from the repository root. If the folder already exists, use `cd terminal-practice` rather than creating it again. The `>` operator replaces a file's contents; `>>` appends to the end.

### Command explanations
| Command | Meaning |
|---|---|
| `pwd` | Prints the current working directory |
| `ls` | Lists visible files and folders |
| `ls -la` | Lists entries including hidden files, with details |
| `cd ..` | Moves to the parent directory |
| `mkdir name` | Creates a directory |
| `touch file` | Creates an empty file if it does not exist |
| `cp source destination` | Copies a file |
| `mv source destination` | Moves or renames a file |
| `cat file` | Prints file contents |
| `ls -lh` | Detailed listing with human-readable sizes |
| `command1 | command2` | Sends the first command's output to the second command |

### Questions
- **Overwrite vs append:** `>` replaces existing contents; `>>` adds content at the end.
- **Copy vs move:** `cp` leaves the original in place; `mv` moves or renames it.
- **`pwd` and listing:** `pwd` tells me where I am; `ls` shows what is in the current directory.

Homebrew: `[If already installed, record `brew --version` and `brew list`. Do not install or uninstall anything just for this task.]`
