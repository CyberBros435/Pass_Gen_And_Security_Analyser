# 🔐 Pass_Gen_&_Checker

<div align="center">

```
 ______  ______  ______  ______     ______  ______  __   __     ______  ______  __  __  ______  ______  __  __ 
/\  == \/\  __ \/\  ___\/\  ___\   /\  ___\/\  ___\/\ "-.\ \   /\  ___\/\  ___\/\ \_\ \/\  ___\/\  ___\/\ \/ / 
\ \  _-/\ \  __ \ \___  \ \___  \  \ \ \__ \ \  __\\ \ \-.  \  \ \ \___\ \  __\\ \  __ \ \  __\\ \ \___\ \  _"-.
 \ \_\   \ \_\ \_\/\_____\/\_____\  \ \_____\ \_____\ \_\\"\_\  \ \_____\ \_____\ \_\ \_\ \_____\ \_____\ \_\ \_\
  \/_/    \/_/\/_/\/_____/\/_____/   \/_____/\/_____/\/_/ \/_/   \/_____/\/_____/\/_/\/_/\/_____/\/_____/\/_/\/_/
```

**Password Generator & Strength Checker**

![Python](https://img.shields.io/badge/Python-3.7%2B-cyan?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v1.0-magenta?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-CyberBros435-blue?style=for-the-badge&logo=github)

A professional CLI tool for generating cryptographically secure passwords and analyzing password strength — built for security enthusiasts, bug hunters, and developers.

[Installation](#-installation) • [Usage](#-usage) • [Features](#-features) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 🚀 Features

- **🎲 Password Generator** — Cryptographically secure passwords using Python's `secrets` module (any length from 1 to 999 characters)
- **🔐 Password Strength Checker** — Full analysis of any password with detailed scoring report
- **📊 Strength Scoring** — Smart scoring system checking length, character variety, common patterns, and known weak passwords
- **⏱️ Crack Time Estimation** — Estimates how long it would take a modern GPU to brute-force your password
- **🎨 Beautiful CLI UI** — Colored panels, tables, and banners using `rich` and `pyfiglet`
- **🖥️ Cross-Platform** — Works on Windows, Linux, and macOS

---

## 📋 Requirements

- Python **3.7 or higher**
- pip (comes with Python)

---

## 📦 Installation

### Method 1 — Clone from GitHub (Recommended)

```bash
# Step 1: Clone the repository
git clone https://github.com/CyberBros435/Pass_Gen_And_Security_Analyser.git

# Step 2: Navigate into the folder
cd Pass_Gen_And_Security_Analyser

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the tool
python pass_gen_checker.py
```

---

### Method 2 — Manual Download & Install

**Step 1** — Download the ZIP from GitHub:

```
https://github.com/CyberBros435/Pass_Gen_And_Security_Analyser/archive/refs/heads/main.zip
```

**Step 2** — Extract the ZIP and open a terminal inside the folder

**Step 3** — Install dependencies:

```bash
pip install -r requirements.txt
```

**Step 4** — Run the tool:

```bash
python pass_gen_checker.py
```

---

### ⚠️ If `pip` doesn't work — try these alternatives

| System | Command |
|--------|---------|
| Linux / macOS | `pip3 install -r requirements.txt` |
| Windows (if pip not found) | `python -m pip install -r requirements.txt` |
| Linux (permission error) | `pip install -r requirements.txt --user` |

---

## ▶️ Usage

Run the tool:

```bash
python pass_gen_checker.py
```

On Linux/macOS you can also use:

```bash
python3 pass_gen_checker.py
```

---

### 🗺️ Navigation Flow

```
Launch Tool
    │
    ▼
[BANNER] — Shows once on startup
    │
    ▼
[MAIN MENU]
    ├── [1] Generate Password
    │       └── Enter length → Get password → Generate again or go back
    │
    ├── [2] Check Password Strength
    │       └── Enter password → See full report → Check again or go back
    │
    └── [3] Exit
```

---

### 🎲 Option 1 — Generate Password

1. Choose option `1` from the main menu
2. Enter your desired password length (min: 1, max: 999)
3. Your secure password is generated instantly
4. Press `y` to generate another or `n` to return to menu

**Example:**
```
  Enter password length (min 1 - max 999): 20
  
  ╭──────────────────────────────────────╮
  │   🔑 Generated Password:             │
  │                                      │
  │      X7#mKp@9LqR!vN2wY&z            │
  │                                      │
  ╰──────────────────────────────────────╯
  
  » Generate another? [y/n]:
```

---

### 🔐 Option 2 — Check Password Strength

1. Choose option `2` from the main menu
2. Type your password and press Enter
3. Get a full detailed report instantly

**Report includes:**

| Check | What it analyzes |
|-------|-----------------|
| Length | Characters counted and scored |
| Score | Total out of 100 |
| Strength Level | VERY WEAK / WEAK / MEDIUM / STRONG / VERY STRONG |
| Crack Time | Estimated GPU brute-force time |
| Uppercase | Whether A-Z letters are present |
| Lowercase | Whether a-z letters are present |
| Numbers | Whether 0-9 digits are present |
| Special Chars | Whether symbols like `!@#$` are present |
| Common Patterns | Checks for `123`, `abc`, `qwerty`, etc. |
| Common Password | Checked against 35+ known weak passwords |
| Length Suggestion | Flags if under 12 characters |

---

## 📊 Scoring System

| Score | Strength | Color |
|-------|----------|-------|
| 0 – 25 | VERY WEAK ⚠️ | 🔴 Red |
| 26 – 45 | WEAK ⚠️ | 🔴 Red |
| 46 – 65 | MEDIUM 👍 | 🟡 Yellow |
| 66 – 85 | STRONG 💪 | 🟢 Green |
| 86 – 100 | VERY STRONG 🛡️ | 🔵 Cyan |

**How points are calculated:**

```
Length:
  1-5 chars     →  0 pts
  6-7 chars     → 10 pts
  8-11 chars    → 20 pts
  12-15 chars   → 30 pts
  16+ chars     → 40 pts

Bonuses:
  Has uppercase → +10 pts
  Has lowercase → +10 pts
  Has numbers   → +10 pts
  Has symbols   → +15 pts

Penalties:
  Common pattern found  → -10 pts
  Known weak password   → -20 pts
```

---

## 📁 Project Structure

```
Pass_Gen_And_Security_Analyser/
│
├── pass_gen_checker.py    ← Main tool (single file, fully organized)
├── requirements.txt       ← Python dependencies
└── README.md              ← This file
```

---

## 🔧 Dependencies

| Library | Purpose |
|---------|---------|
| `rich` | Beautiful CLI panels, tables, and colors |
| `pyfiglet` | ASCII art banner |
| `colorama` | Windows terminal color support |

Install all at once:

```bash
pip install rich pyfiglet colorama
```

---

## 🖥️ Platform Support

| Platform | Supported | Notes |
|----------|-----------|-------|
| Windows 10/11 | ✅ | Run in CMD or PowerShell |
| Linux (Ubuntu, Kali, Debian) | ✅ | Use `python3` |
| macOS | ✅ | Use `python3` |
| Termux (Android) | ✅ | Use `pip install` then `python` |
| Kali Linux | ✅ | Great for security workflows |

---

## 🐛 Troubleshooting

**`ModuleNotFoundError: No module named 'rich'`**
```bash
pip install rich pyfiglet colorama
```

**`python: command not found` on Linux/macOS**
```bash
python3 pass_gen_checker.py
```

**Permission error on Linux**
```bash
pip install -r requirements.txt --user
```

**Windows terminal colors not showing**
```bash
# Run this first
pip install colorama
# Then run tool in Windows Terminal (not old CMD)
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Commit: `git commit -m "Add your feature"`
5. Push: `git push origin feature/your-feature`
6. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 👤 Author

**CyberBros435**

- GitHub: [@CyberBros435](https://github.com/CyberBros435)
- Repo: [Pass_Gen_And_Security_Analyser](https://github.com/CyberBros435/Pass_Gen_And_Security_Analyser)

---

<div align="center">

Made with 🔐 by **CyberBros435**

*If this tool helped you, consider giving it a ⭐ on GitHub!*

</div>
