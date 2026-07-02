# 🌪️ Auto-Sorter: The Python File Organizer

A lightweight, lightning-fast Python automation script that instantly transforms chaotic, messy folders into perfectly categorized directories. 

## 🚀 The Vision
Tired of a cluttered Downloads folder? **Auto-Sorter** acts as your personal digital janitor. Simply point it at a messy directory, and it will automatically detect file extensions, generate the appropriate category folders, and safely move every file into its new home. 

## ✨ Features
* **Zero-Touch Execution:** Just run the script and watch the magic happen.
* **Intelligent Routing:** Automatically maps over 20+ file extensions to their correct logical categories (Images, Documents, Code, etc.).
* **Safe & Non-Destructive:** Uses Python's `shutil` module to safely transfer files without risking data loss.
* **Smart Directory Creation:** Automatically generates missing category folders on the fly using `os.makedirs(exist_ok=True)`.

## 📂 How It Works

**Before Execution:**
```text
messy_folder/
├── budget.csv
├── vacation.jpg
├── setup.exe
├── script.py
└── presentation.pptx
```

**After Execution:**
```text
messy_folder/
├── 📁 Images/       (vacation.jpg)
├── 📁 Documents/    (budget.csv, presentation.pptx)
├── 📁 Applications/ (setup.exe)
└── 📁 Code/         (script.py)
```

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Libraries:**
  * `os`: For deep operating system interaction and path management.
  * `shutil`: For high-level file operations and safe transfers.

## 💻 Quick Start

1. **Clone** this repository to your local machine.
2. **Place** your unorganized files inside the `messy_folder` directory (or update the script to point to your own folder).
3. **Run** the script via your terminal:
   ```bash
   python organizer.py
   ```
4. **Watch** your files organize themselves instantly!

---
*Built as a core automation project to master Python OS manipulation.*
