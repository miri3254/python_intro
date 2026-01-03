# My First Game

A small Python game located in the `my_first_game` folder. This repository contains the game's source (`main.py`), a `requirements.txt` for dependencies, and a PyInstaller build output under `build/`.

## Requirements

- Python 3.8+
- See `my_first_game/requirements.txt` for Python packages used by the game.

## Quick start (Windows PowerShell)

1. Open a terminal and change to the project folder:

```powershell
cd my_first_game
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies and run the game:

```powershell
pip install -r requirements.txt
python main.py
```

## Build (optional)

This project includes a PyInstaller spec in the `my_first_game` folder. To build a standalone executable:

```powershell
cd my_first_game
pip install pyinstaller
pyinstaller --onefile main.spec
```

Built artifacts will appear under `dist/` and detailed build output under `build/`.

## Project layout

- `my_first_game/` — game source and build spec
	- `main.py` — entry point
	- `requirements.txt` — Python deps
- `build/` — PyInstaller build output (ignored by .gitignore)

## Next steps

- If you want, I can add a short description of the game controls, a screenshot, or update `requirements.txt` if any dependencies are missing.

---
Generated README by assistant.
