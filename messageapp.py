import tkinter as tk
from tkinter import Scrollbar, Text

# Function to send a message
def send_message():
    message = input_text.get("1.0", "end-1c")
    if message:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert("end", "You: " + message + "\n")
        chat_box.config(state=tk.DISABLED)
        input_text.delete("1.0", "end")

# Create the main window
app = tk.Tk()
app.title("Simple Message App")

# Create a text widget for displaying the chat
chat_box = Text(app, state=tk.DISABLED, wrap=tk.WORD)
chat_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Add a scrollbar to the chat box
scrollbar = Scrollbar(app, command=chat_box.yview)
scrollbar.grid(row=0, column=2, sticky="nsew")
chat_box['yscrollcommand'] = scrollbar.set

# Create an entry widget for typing messages
input_text = Text(app, height=2, wrap=tk.WORD)
input_text.grid(row=1, column=0, padx=10, pady=10)

# Create a button to send messages
send_button = tk.Button(app, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter main loop
app.mainloop()
