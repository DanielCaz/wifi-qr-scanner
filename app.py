import tkinter as tk
import cv2
from pyzbar.pyzbar import decode
import clipboard
from tkinter import messagebox


def scan_qr_code():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Create a flag to track if the window is closed
    window_closed = False

    # Create the OpenCV window
    cv2.namedWindow("QR Code Scanner")

    # Read frames from the webcam
    while not window_closed:
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow("QR Code Scanner", frame)

        # Check for the 'q' key press to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Convert the frame to grayscale for QR code decoding
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode QR codes from the grayscale frame
        qr_codes = decode(gray)

        # Process the detected QR codes
        for qr_code in qr_codes:
            # Extract the data and type from the QR code
            data = qr_code.data.decode("utf-8")
            qr_type = qr_code.type

            # Check if the QR code contains Wi-Fi network information
            if qr_type == 'QRCODE' and data.startswith("WIFI:"):
                wifi_info = data[5:]  # Remove the 'WIFI:' prefix

                # Split the Wi-Fi network information into components
                components = wifi_info.split(';')

                ssid = ''
                password = ''

                # Extract SSID and password from the components
                for component in components:
                    if component.startswith("S:"):
                        ssid = component[2:]
                    elif component.startswith("P:"):
                        password = component[2:]

                # Handle the Wi-Fi link
                clipboard.copy(password)
                messagebox.showinfo("Wi-Fi QR Code Scanner",
                                    "Password copied to clipboard")

                # Update the label text
                ssid_label.config(text=f"SSID: {ssid}")
                password_label.config(text=f"Password: {password}")
                window_closed = True  # Set the flag to close the window

    # Release the webcam and destroy the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


# Create the main application window
app = tk.Tk()
app.title("Wi-Fi QR Code Scanner")
app.geometry("300x200")


# Create a button to trigger QR code scanning
scan_button = tk.Button(app, text="Scan QR Code", command=scan_qr_code)
scan_button.pack(pady=10)

# Create a label to display the SSID
ssid_label = tk.Label(app, text="SSID: ")
ssid_label.pack(pady=10)

# Create a label to display the password
password_label = tk.Label(app, text="Password: ")
password_label.pack(pady=10)

# Start the application's event loop
app.mainloop()
