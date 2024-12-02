# Face Lock System for Laptop

A Python-based face recognition system designed to enhance laptop security by integrating with the Linux boot process. This system provides secure, seamless authentication using face recognition during startup.

---

## Features

- **Secure Authentication**: Implements face recognition to authenticate users at startup.
- **Linux Integration**: Works within the Linux boot process for a smooth login experience.
- **Customizable**: Built with OpenCV and Python, allowing easy customization.

---

## Requirements

### Software
- **Operating System**: Linux (Tested on Ubuntu 20.04 and later)
- **Python Version**: Python 3.8 or higher
- **Libraries**:
  - `opencv-python`
  - `numpy`
  - `dlib`
  - `face-recognition`
- **Linux Packages**:
  - `lightdm` (or another Display Manager)
  - `libopencv-dev`

Install Python libraries with:
```bash
pip install opencv-python numpy dlib face-recognition

```
## BIOS and Laptop Configuration
- 1. Enable Integrated Camera in BIOS
- 2.Restart your laptop and enter the BIOS/UEFI settings (press F2, DEL, or ESC during boot).
- 3.Navigate to Integrated Peripherals or Advanced.
- 4.Ensure the Integrated Camera option is Enabled.
- 5.Save changes and exit.
