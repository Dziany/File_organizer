# 📂 Smart File Organizer

A lightweight and efficient Python utility that automatically organizes cluttered folders (like "Downloads") by sorting files into categorized subdirectories based on their extensions.

## 🚀 Key Features
- **Auto-Categorization:** Pre-configured for Images, Documents, Archives, Installers, Audio, Video, and Development files.
- **JSON-Driven Configuration:** Easily customize file mappings in an external `config.json` file without modifying the core logic.
- **Robust Error Handling:** Includes `try-except` blocks to handle "Permission Denied" (files in use) and "File Already Exists" scenarios.
- **Pathlib Integration:** Built with modern Python `pathlib` for safe and cross-platform file system operations.

## 🛠️ Getting Started

### Prerequisites
- Python 3.6 or higher.
- Windows 10 or Windows 11.
- Installed libraries:
   - pathlib
   - shutil

## Instaling Libraries
To install needed libraries run:
   ```bash 
   pip install pathlib
   pip install shutil
   ```

### Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Dziany/File_organizer.git)
2. **Navigate to directory**
   ```bash
   cd python-file-organizer
3. **Configure your path:**
   Open config.json and update the source_dir variable with your target directory path:
   ```json
      "source dir": "YOUR_DIRECTORY"
   ```
4. **Run the script**
   ```bash
   python main.py
   ```

## ⚙️ Configuration
You can easily add or remove file types by editing config.json under extension_map

Example structure:
```Json
"extension_map": {
        "Image": [".jpg", ".png", ".gif", ".jpeg", ".bmp"],
        "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".rtf"],
    }

```
## 📈 Roadmap (Future Improvements)
- **[] GUI Version**: Build a user-friendly interface using Tkinter or PyQt
- **[] Duplicate Handling** - Automatically rename files if a version already exists in the destination
- **[] Watching Integration** - Real-time monitoring to organize files as soon as they are downloaded
- **[] Choices of handling files** - User will be able to chose if a file is going to be moved, copied or copied/moved and renamed
- **[] AI-assisnant** - Assistant to help with managing your files, based on your answeres it will be able to adjust config.json to your preferences

### Author: Piotr Żurawski


