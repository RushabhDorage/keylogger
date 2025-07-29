keylogger

KeyLogger Lite A minimal and cross-platform Python keylogger that logs all keyboard activity to a timestamped file. It includes built-in log rotation, ESC-based termination, and a simple console UI. Designed for educational, debugging, and personal productivity purposes — use responsibly.



 🖥️ KeyLogger Lite – A Minimal Python Keystroke Logger

KeyLogger Lite* is a simple Python script that captures keyboard activity and logs keystrokes to a timestamped file. Built with the `keyboard` module, it is useful for productivity monitoring, debugging, and educational purposes — with log rotation and safe exit via ESC key.



 ⚠️ Legal Disclaimer

> This tool is intended strictly for educational or authorized debugging use. Unauthorized usage to record keystrokes without consent may violate local privacy or cybersecurity laws. You are fully responsible for how you use this software.

 🚀 Features

- ⌨️ Logs all keypresses with timestamps
- 📁 Outputs to `keystrokes.log` in the working directory
- 🔁 Automatic log file rotation at 1MB size
- 🧘 Press `ESC` to stop the logger gracefully
- 🪶 Lightweight and no GUI — runs in terminal



 🛠️ Setup

 📦 Requirements

- Python 3.x
- `keyboard` module

 🔧 Install Dependencies


pip install keyboard

 ▶️ Run the Logger


python keylogger.py


The logger will begin capturing keypresses. You can stop it at any time by pressing `ESC`.

 📄 Example Output (`keystrokes.log`)

[2025-07-29 20:13:44] h
[2025-07-29 20:13:44] e
[2025-07-29 20:13:44] l
[2025-07-29 20:13:45] l
[2025-07-29 20:13:45] o
[2025-07-29 20:13:46] space
[2025-07-29 20:13:47] w
[2025-07-29 20:13:47] o
[2025-07-29 20:13:47] r
[2025-07-29 20:13:47] l
[2025-07-29 20:13:47] d

 🔁 Log Rotation

* The file size is checked after each keypress.
* Once the log exceeds **1MB**, the oldest half of the file is discarded automatically.



💡 Potential Uses

* Monitor custom keybindings or UI events
* Debug unexpected keystroke behavior
* Teach security and privacy awareness
* Personal typing practice (with consent)

 📜 License

This project is licensed under the MIT License. See (./LICENSE) for more details.

 👨‍💻 Author

Made with 🧠 and ⌨️ by [Rushabh Dorage](https://github.com/RushabhDorage)

 ⭐ Like It?

Give the repo a ⭐ and use responsibly.


MIT License

Copyright (c) 2025 [Rushabh Dorage]

