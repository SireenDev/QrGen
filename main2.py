
import customtkinter
import segno
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1200x650")
root.title("QR Code Generator")
root.resizable(False, False)

# Create the side panel frame
side_panel = customtkinter.CTkFrame(master=root, width=400)
side_panel.pack(side="left", fill="y", padx=20, pady=20)

# Add content to side panel
panel_title = customtkinter.CTkLabel(
    master=side_panel,
    text="QR Code Generator",
    font=("Roboto", 24, "bold")
)
panel_title.pack(pady=20, padx=10)

info_text = """
Welcome to QR Code Generator!

This application allows you to:
• Generate QR codes from any URL
• Save QR codes as PNG files
• Customize file names

Instructions:
1. Paste your URL in the input field
2. Enter desired filename
3. Click Generate button
4. Your QR code will be saved
"""

info_label = customtkinter.CTkLabel(
    master=side_panel,
    text=info_text,
    font=("Roboto", 14),
    justify="left",
    wraplength=250
)
info_label.pack(pady=20, padx=10)

# Create main content area
main_frame = customtkinter.CTkFrame(master=root)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Add main content
titleLab = customtkinter.CTkLabel(master=main_frame, text="Generate Your QR Code", font=("Roboto", 32))
titleLab.pack(pady=25)

linkInp = customtkinter.CTkEntry(master=main_frame, placeholder_text="Paste link here", width=300)
linkInp.pack(pady=50)

nameInp = customtkinter.CTkEntry(master=main_frame, placeholder_text="Filename Here", width=300)
nameInp.pack(pady=10)

def saveQR():
    url = linkInp.get()
    fileName = nameInp.get() + ".png"
    progress.start()
    qrCode = segno.make(url)
    qrCode.save(fileName, border=0, scale=20)
    if os.path.exists(fileName):
        statusLab.configure(text="Done!")

generateBut = customtkinter.CTkButton(master=main_frame, text="Generate QR Code", width=275, command=saveQR)
generateBut.pack(pady=50)

progress = customtkinter.CTkProgressBar(master=main_frame, orientation="horizontal", width=300, height=25, mode="indeterminate")
progress.set(0)
progress.pack(pady=20)

statusLab = customtkinter.CTkLabel(master=main_frame, text="Waiting...", font=("Roboto", 20))
statusLab.pack(pady=4)

creditsLab = customtkinter.CTkLabel(master=main_frame, text="Created by SireenDev", font=("Roboto", 15))
creditsLab.pack(pady=3)

root.mainloop()
