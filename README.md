Project URL: https://github.com/gyllianerae/rsh-task-cli

# 📝 Task Tracker CLI

A simple **command-line Task Tracker** built with Python.
This application helps you **add, update, delete, and manage tasks** using a JSON file for storage.

The project is built using **only Python’s standard library** and runs entirely from the terminal.

---

## 📌 Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as:

  * `todo`
  * `in-progress`
  * `done`
* List:

  * All tasks
  * Tasks by status
* Persistent storage using a JSON file
* Graceful error handling

---

## 🛠️ Technologies Used

* Python 3
* Standard Python modules only:

  * `sys`
  * `json`
  * `os`
  * `datetime`

❌ No external libraries or frameworks used

---

## 📂 Project Structure

```
task-tracker/
│
├── task_cli.py     # Main CLI application
├── tasks.json      # Task storage file (auto-created)
└── README.md       # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

* Python 3 installed on your system
  Check by running:

```bash
python --version
```

or

```bash
python3 --version
```

---

### 2️⃣ Clone or Download the Project

Place `task_cli.py` in a folder of your choice.

---

### 3️⃣ Navigate to Project Folder

```bash
cd path/to/task-tracker
```

---

### 4️⃣ Run the Program

```bash
python task_cli.py
```

You should see:

```
Usage: task-cli <command> [arguments]
```

---

## 📖 Usage Guide

### ➕ Add a Task

```bash
python task_cli.py add "Buy groceries"
```

---

### 📋 List All Tasks

```bash
python task_cli.py list
```

---

### ✏️ Update a Task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

---

### 🔄 Mark Task as In Progress

```bash
python task_cli.py mark-in-progress 1
```

---

### ✅ Mark Task as Done

```bash
python task_cli.py mark-done 1
```

---

### 📂 List Tasks by Status

```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

---

### 🗑️ Delete a Task

```bash
python task_cli.py delete 1
```

---

## 📄 Task Format (tasks.json)

Each task is stored with the following properties:

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2026-01-05T10:30:00",
  "updatedAt": "2026-01-05T10:30:00"
}
```

---

## ⚠️ Error Handling

* Missing arguments
* Invalid task ID
* Unknown commands
* Empty task list

The program will show helpful messages instead of crashing.

---

## 🎯 Learning Objectives

This project helps practice:

* Command-line arguments (`sys.argv`)
* File handling in Python
* JSON data storage
* Error handling with `try/except`
* Writing clean, modular code

---

## 📌 Future Improvements (Optional)

* Add task priorities
* Add due dates
* Search tasks
* Convert to class-based (OOP) design
* Add unit tests

---

## 👨‍💻 Author

Created as a learning project to understand **CLI applications and file handling in Python**.
