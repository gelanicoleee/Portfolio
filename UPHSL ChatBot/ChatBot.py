import tkinter as tk
import tkinter.font
from tkinter import NW, scrolledtext
import xml.etree.ElementTree as ET

window = tk.Tk()
window.title("Ask Something About Perps")
window.geometry("885x630")
window.resizable(width=False, height=False)
window.iconbitmap('Logo.ico') # Replacing icon of the window

def saved_responses(filename): # Parsing XML and Finding contents of specific Tag
    responses = {}
    tree = ET.parse('information.xml')
    root = tree.getroot()
    for response in root.findall('response'):
        keywords = response.find('keywords').text # Get keywords in the XML file
        response_texts = [text.text for text in response.findall('text')] # Get response texts in the XML file
        keywords_list = keywords.split(",") # Split keywords by comma
        for keyword in keywords_list:
            responses[keyword.strip().lower()] = '\n'.join(response_texts) # Store response texts of each keyword in the dictionary
    return responses

def send_message(): # User input queries
    user_message = user_input.get()
    user_input.delete(0, tk.END) # Clear the input field
    chatbox.config(state=tk.NORMAL) # Enable chatbox for editing
    chatbox.insert(tk.END,"You: " + user_message + "\n", "user") # Display user's message in chatbox
    chatbox.config(state=tk.DISABLED) # Disable chatbox for editing
    respond(user_message)

def respond(message): # Get the corresponding respond of the keyword
    message_lower = message.lower()
    response = "Sorry. You can call 02-8779-5310 or visit UPHSL website for other inquiries."
    for keyword in responses: # Finding the keyword in the responses dictionary
        if keyword in message_lower:
            response = responses[keyword]
            break
    append_to_chatbox("ASAP:\n" + response + "\n")

def append_to_chatbox(text): # Adding text to display in the chatbox
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, text) # Append text to chatbox
    chatbox.config(state=tk.DISABLED)
    chatbox.see(tk.END) # Scroll to the end of chatbox

def clear_chat(): # Clearing the text display in the chatbox
    chatbox.config(state=tk.NORMAL)
    chatbox.delete(1.0, tk.END) # Delete all text from chatbox
    append_to_chatbox("ASAP:\n Hello! How can I assist you today?\n")
    chatbox.config(state=tk.DISABLED)

def add_to_history(): # Add history of chat in history list
    chat_history = chatbox.get(1.0, tk.END).strip()  # Get current chat history
    if chat_history:
        history_name = " UNTITLED " + str(len(history_dict) + 1)  # Create a history name
        history_dict[history_name] = chat_history  # Save chat history to dictionary
        history_names.append(history_name)  # Add history name to list
        history_listbox.delete(0, tk.END)
        for name in history_names:  # Update the listbox
            history_listbox.insert(tk.END, name)
        clear_chat()  # Clear chatbox after saving chat history
        display_history()

def display_history(event=None):  # Display selected chat history
    selected_index = history_listbox.curselection()[0]  # Get index of selected history
    selected_name = history_listbox.get(selected_index)
    selected_history = history_dict[selected_name]  # Get selected chat history
    chatbox.config(state=tk.NORMAL)
    chatbox.delete(1.0, tk.END)
    chatbox.insert(tk.END, selected_history)  # Display selected chat history
    chatbox.config(state=tk.DISABLED)

# BACKGROUND
bg_ChatBotBg = tk.PhotoImage(file="ChatBotBG.png")
frm_Background = tk.Frame(window, bg='#3B0918')
frm_Background.place(x=0, y=0, relwidth=1, relheight=1)
canvas = tk.Canvas(frm_Background, width=885, height=630)
canvas.pack()
canvas.create_image(0, 0, image=bg_ChatBotBg, anchor=NW)

# FONT
Name_font = tkinter.font.Font(family="Franklin Gothic Demi", size=24)
Chatbox_font = tkinter.font.Font(family="Franklin Gothic Medium", size=11)
Listbox_font = tkinter.font.Font(family="Franklin Gothic Demi", size=13)
user_input_font = tkinter.font.Font(size=12)

# LOGO IMAGE
logo_img = tk.PhotoImage(file="Logo.png")

# FRAMES
frm_ChatBoxName = tk.Frame(window, bg="#112A6C")
frm_chatbox = tk.Frame(window, highlightcolor="#012265", highlightbackground="#012265", highlightthickness=3, bg="#012D85")
frm_input = tk.Frame(window, highlightcolor="#012265", highlightbackground="#012265", highlightthickness=3, bg="#012D85", padx=4, pady=5)

# LABELS & CHATBOX
lbl_Logo = tk.Label(master=frm_ChatBoxName, image=logo_img, bg="#112A6C")
lbl_ChatBoxName = tk.Label(master=frm_ChatBoxName, text="ASAP", bg="#112A6C", fg='#FFDE00', font=Name_font)
# Make the chatbox scrollable to view all the contents displayed
chatbox = scrolledtext.ScrolledText(frm_chatbox, width=59, height=19, padx=10, pady=10, state=tk.DISABLED, font=Chatbox_font, wrap=tk.WORD)

# POSITIONS
lbl_Logo.grid(row=0, column=0, padx=(10,0), pady=5)
lbl_ChatBoxName.grid(row=0, column=1, sticky="ew", padx=(165, 110))
frm_ChatBoxName.grid(row=0, column=0, pady=10, sticky="w", padx=(39, 0))
frm_chatbox.grid(row=1, column=0, padx=36)
frm_input.grid(row=2, column=0, pady=20)
chatbox.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

# CONFIGURE
chatbox.tag_config("user", background="#FFDE00")

# USER INPUT
user_input = tk.Entry(frm_input, width=57, font=user_input_font)
user_input.grid(row=0, column=0, padx=(13, 6), sticky="w")
user_input.bind('<Return>', lambda event=None: send_message()) # Allows user click Enter key to send message

# SEND BUTTON
btn_send_image = tk.PhotoImage(file="Send.png")
send_button = tk.Button(frm_input, image=btn_send_image, command=send_message, bd=0, highlightthickness=0, relief=tk.FLAT)
send_button.grid(row=0, column=1, padx=(5, 10), sticky="e")

# RESET BUTTON
btn_reset = tk.PhotoImage(file="Clear.png")
reset_button = tk.Button(frm_ChatBoxName, image=btn_reset, command=clear_chat, bd=0, highlightthickness=0, relief=tk.FLAT)
reset_button.grid(row=0, column=2, padx=(20, 14), sticky="e")

# ADD BUTTON
btn_add_image = tk.PhotoImage(file="Add.png")
add_button = tk.Button(frm_ChatBoxName, image=btn_add_image, command=add_to_history, bd=0, highlightthickness=0, relief=tk.FLAT)
add_button.grid(row=0, column=7, padx=(20, 14), sticky="e")

# SAVED RESPONSES
responses = saved_responses("responses.txt")
append_to_chatbox("ASAP:\nHello! How can I assist you today?\n")

# CHAT HISTORY LIST AND DICTIONARY
history_dict = {}
history_names = []

# HISTORY LISTBOX
history_listbox = tk.Listbox(window, width=15, height=19, font=Listbox_font, fg="#FFDE00", highlightcolor="#012D85", highlightbackground="#012D85", highlightthickness=9, bg="#012D85", borderwidth=0, activestyle=tk.NONE)
history_listbox.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
history_listbox.bind('<<ListboxSelect>>', display_history)

window.mainloop()






