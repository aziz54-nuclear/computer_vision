# Computer Vision Projects

A collection of Python computer vision scripts using OpenCV and MediaPipe.

## Requirements

- Python 3.11
- pip
- Webcam
- OpenCV
- MediaPipe

## Setup and Installation

### 1. Clone the repository

### 2. Create the virtual environment

```bash
py -3.11 -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
venv\Scripts\activate.bat
```

### 4. Install dependencies

Make sure the virtual environment is activated before installing packages.

```bash
python -m pip install --upgrade pip
pip install opencv-python mediapipe
```

## Running the Scripts

Activate the virtual environment first:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run any script using Python:

### Body Tracking

```bash
python bodyTracking.py
```

### Face Detection

```bash
python faceDetection.py
```

### Hand Tracking

```bash
python handtrackingmin.py
```

Press `q` to quit the webcam window (if supported by the script).

## Project Structure

```text
computer_vision/
│
├── venv/
├── bodyTracking.py
├── faceDetection.py
├── handtrackingmin.py
├── .gitignore
└── README.md
```

## Notes

- The project uses Python 3.11.
- All dependencies must be installed inside the `venv` virtual environment.
- The virtual environment is excluded from Git version control.
- A working webcam is required for real-time detection.
- Always activate `venv` before running the scripts.

## License

This project is available for educational and personal use.
