# Keyboard Listener with pynput (Python)

This project is a simple example of using the `pynput` library to **listen to keyboard events** in Python.

The program receives each key that is pressed and processes the data after the number of keys reaches a certain value.

---

## 📦 Libraries used

### pynput
The `pynput` library is used to control and monitor system inputs (keyboard and mouse).

In this project:
- `keyboard.Listener` is used to listen to the keyboard
- `on_press` event is fired every time a key is pressed

Installation:
```bash
pip install pynput
