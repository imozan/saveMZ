# 💾 SaveMZ

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Version](https://img.shields.io/badge/Version-2.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight and easy-to-use JSON database library for Python.

SaveMZ makes working with JSON files simple by providing an intuitive API for reading, writing, updating, and deleting data using dot-separated paths. It also includes a built-in cache system, events, and custom exceptions.

---

# ✨ Features

- 📦 Lightweight and easy to use
- ⚡ Built-in cache system
- 📁 Dot-separated path support
- ✏️ Read, write, update and delete values
- 🔄 Reload data from disk
- 🎯 Event system
- 🚨 Custom exceptions
- 🐍 Python 3.10+

---

# 📦 Installation

```bash
pip install savemz
```

---

# 🚀 Quick Start

```python
from savemz import SaveMZ

db = SaveMZ("database.json")

db.set("user.name", "Julius")
db.set("user.age", 18)

print(db.get("user.name"))

db.delete("user.age")
```

---

# 📖 Methods

## Read

```python
db.read()
```

Returns the entire JSON object.

---

## Write

```python
db.write(data)
```

Writes a Python object to the JSON file.

You can also specify the indentation:

```python
db.write(data, indent=4)
```

---

## Get

```python
db.get("user.name")
```

Returns the value stored at the given path.

---

## Set

```python
db.set("user.name", "John")
```

Creates or updates a value.

---

## Delete

```python
db.delete("user.name")
```

Deletes the specified key.

---

## Reload

```python
db.reload()
```

Reloads the file and clears the cache.

---

# ⚡ Events

Register an event:

```python
from savemz import SaveMZ

db = SaveMZ("database.json")

def after_set(path, value):
    print(f"{path} -> {value}")

db.onEvent("after_set", after_set)

db.set("user.name", "Alex")
```

Available events:

- before_read
- after_read
- before_write
- after_write
- before_set
- after_set
- before_delete
- after_delete
- before_reload
- after_reload

Remove an event:

```python
db.offEvent("after_set", after_set)
```

---

# 🚨 Exceptions

SaveMZ provides custom exceptions for cleaner error handling.

Example:

```python
from savemz import PathNotFoundError

try:
    db.get("user.age")
except PathNotFoundError:
    print("Path not found.")
```

---

# 📄 Example JSON

```json
{
  "user": {
    "name": "John",
    "age": 20
  }
}
```

Access values using:

```python
db.get("user.name")
```

Output:

```python
John
```

---

# 📌 Why SaveMZ?

- Simple API
- Lightweight
- No external dependencies
- Fast cache system
- Event support
- Easy nested JSON access
- Beginner-friendly
- Clean and readable code

---

# 📄 Changelog

See the full changelog in:

```
CHANGELOG.md
```

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Julius**

GitHub:

https://github.com/imozan/saveMZ

If you like this project, consider giving it a ⭐ on GitHub.
