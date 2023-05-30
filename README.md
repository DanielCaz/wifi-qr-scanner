Wi-Fi QR Code Scanner

This is a simple desktop application built in Python using Tkinter and OpenCV. The app allows users to scan QR codes containing Wi-Fi network information and copy the password to the clipboard. It utilizes the device's camera to capture the QR code and extracts the SSID and password from the decoded data. The scanned password is displayed on the main window, and the camera window automatically closes after copying the password. This app provides a convenient way to share Wi-Fi passwords using QR codes. 

Features:
- Scan QR codes containing Wi-Fi network information
- Extract SSID and password from the scanned data
- Copy the password to the clipboard
- Automatically close the camera window after copying the password

Requirements:
- Python 3.x
- Tkinter
- OpenCV
- pyzbar
- clipboard

Usage:
1. Run the script to launch the application.
2. Click on the "Scan QR Code" button to activate the camera and start scanning.
3. Position the QR code within the camera frame.
4. Once a QR code with Wi-Fi network information is detected, the password will be displayed on the main window and copied to the clipboard.
5. The camera window will automatically close after copying the password.
