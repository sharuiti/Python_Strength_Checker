<div align="center">

# 🔐 PASSWORD STRENGTH CHECKER

### *A comprehensive password analysis tool that evaluates security using complexity checks, common password detection, and real-time breach database verification*

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Made with Love](https://img.shields.io/badge/made%20with-❤️-red.svg)](https://github.com/sharuiti)

</div>

---

## 📋 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

### 🔍 **Multi-Layer Password Analysis**
| Feature | Description |
|---------|-------------|
| ✅ **Complexity Check** | Evaluates length, uppercase, lowercase, numbers, and special characters |
| 📋 **Common Password Detection** | Compares against top 10,000 most used passwords |
| 🌐 **Breach Database Verification** | Real-time checking against Have I Been Pwned API |
| 🛡️ **Privacy-First Design** | Uses k-anonymity - passwords never leave your computer |
| 💡 **Smart Feedback** | Provides specific, actionable improvement suggestions |
| 🔄 **Multi-Check Support** | Check multiple passwords in one session |
| ⚠️ **Severity Warnings** | Special alerts for critically weak or breached passwords |

### 🎯 **What Makes It Special**
- **Zero password storage** - Your privacy is guaranteed
- **k-Anonymity implementation** - Industry-standard security practice
- **Comprehensive error handling** - Graceful failure for network issues
- **User-friendly output** - Clear, formatted results

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Requests** | API calls to Have I Been Pwned |
| **Hashlib** | SHA-1 hashing for k-anonymity |
| **Have I Been Pwned API** | Global breach database |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step-by-Step Installation

1. **Clone the repository**
```bash
   git clone https://github.com/sharuiti/password-strength-checker.git
   cd password-strength-checker
```

2. **Install required packages**
```bash
   pip install requests
```

3. **Download the common passwords list**
```bash
   curl -O https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt
```
   Or manually download and place `10k-most-common.txt` in the `common_list/` folder.

4. **Verify installation**
```bash
   python password_checker.py
```

---

## 🚀 Quick Start

### Basic Usage
```bash
python password_checker.py
```

### Example Session
```
Enter your password (or 'quit' to exit): MyP@ssw0rd123

 PASSWORD ANALYSIS:
 -Password Length: 13 characters
 -Types used: 4/4 character types
 -Password Strength: VERY STRONG

 Your password is excellent!

 CHECK PASSWORD IN COMMON LIST:
 -password is not in common passwords list

 CHECK PASSWORD AGAINST PWNED DATABASE:
 -Not found in any breaches!
```

---

## 📖 Usage Guide

### Interactive Mode
Run the program and follow the prompts:
```bash
python password_checker.py
```

### Commands
- Type any password to analyze it
- Type `quit`, `exit`, `q`, or `bye` to exit the program

### Understanding Results

| Rating | Meaning | Action Needed |
|--------|---------|---------------|
| 🔴 **VERY WEAK** | Easily crackable | Change immediately |
| 🟠 **WEAK** | Not secure | Use a stronger password |
| 🟡 **MEDIUM** | Acceptable but improvable | Add more complexity |
| 🟢 **STRONG** | Good password | Keep using it |
| 💪 **VERY STRONG** | Excellent password | Perfect! |

### Special Alerts
- **"TOP 10 most common passwords"** - Change this password NOW
- **"Found in X breaches"** - Never use this password anywhere
- **"API error"** - Check your internet connection

---

## 🔧 How It Works

### 1. Password Strength Analysis
Checks for:
- Length (minimum 8 characters)
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (`!@#$%^&*()_+-=` etc.)

### 2. Common Password Detection
- Compares against a database of 10,000 most common passwords
- Returns rank if found (e.g., "#3 most common password!")
- Issues a special warning for passwords in the TOP 10

### 3. Breach Database Check (k-Anonymity)
```
Step 1: Hash password with SHA-1
Step 2: Send only the first 5 characters to the API
Step 3: API returns all hashes that match the prefix
Step 4: Local comparison to check if your full hash is in the list
Step 5: Returns how many times the password was found in breaches
```

---

## 📁 Project Structure
```
password-strength-checker/
│
├── 📄 password_checker.py       # Main application file
├── 📄 README.md                 # Documentation
│
└── 📁 common_list/              # Password lists
    └── 📄 10k-most-common.txt   # Top 10k most common passwords
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `password_checker.py` | Main script — strength check, common list check, HIBP API check |
| `10k-most-common.txt` | Local database of common passwords for comparison |
| `README.md` | You're reading it! |

---

## ⚙️ Configuration

### File Paths
The common passwords file is expected at `common_list/10k-most-common.txt`. If yours is in a different location, update this line in `password_checker.py`:
```python
# Change this:
with open("common_list/10k-most-common.txt", "r") as file:

# To your custom path:
with open("your/custom/path.txt", "r") as file:
```

### API Configuration
The Have I Been Pwned API is pre-configured with no API key required. The timeout is set to 5 seconds and the User-Agent is:
```
PasswordStrengthChecker/1.0 (Python Script)
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### 🐛 Report Bugs
- Open an issue with a detailed description
- Include your Python version and OS
- Paste the error message if applicable

### 💡 Suggest Features
- Open an issue with the "enhancement" tag
- Describe the feature and why it's useful

### 🔧 Submit Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Update documentation as needed
- Test your changes thoroughly

---

## 📜 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 📞 Contact

Safae Charuiti - [LinkedIn](www.linkedin.com/in/safae-charuiti-48386627b) - safaecharuiti@email.com

Project Link: [https://github.com/sharuiti/password-strength-checker](https://github.com/sharuiti/password-strength-checker)

---

## 🙏 Acknowledgments

- [Have I Been Pwned](https://haveibeenpwned.com/) for their incredible free API
- [SecLists](https://github.com/danielmiessler/SecLists) for the common passwords list
- All contributors and users who provide feedback

---

<div align="center">

⭐ If you found this project helpful, please give it a star!

Made with ❤️ and Python

</div>
