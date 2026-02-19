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

### Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Dziany/File_organizer.git)
2. **Navigate to directory**
   ```bash
   cd python-file-organizer
3. **Configure your path:**
   Open main.py and update the folder_to_organize variable with your target directory path:
   ```python
      folder_to_organize = pathlib.Path("C:\Users\User\Downloads")
4. **Run the script**
   ```bash
   python main.py

## ⚙️ Configuration
You can easily add or remove file types by editing config.json

Example structure:
```Json
{
    "Images": [".jpg", ".png", ".gif"],
    "Dev": [".py", ".js", ".html", ".json"]
}
```
## 📈 Roadmap (Future Improvements)
- **[] GUI Version**: Build a user-friendly interface using Tkinter or PyQt
- **[] Duplicate Handling** - Automatically rename files if a version already exists in the destination
- **[] Watching Integration** - Real-time monitoring to organize files as soon as they are downloaded

### Author: Piotr Żurawski


