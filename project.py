import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
XAI_API_KEY = os.getenv('XAI_API_KEY')

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)


def get_grok_response(user_message):
    """Gets a response from the Grok API."""
    try:
        completion = client.chat.completions.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": "You are Grok, a helpful AI assistant."},
                {"role": "user", "content": user_message},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


def update_chat_history(message, tag):
    """Updates the chat history with a new message. Handles loading state and newlines."""
    chat_history.configure(state='normal')
    indices = chat_history.search(r"Grok: Loading\.\.\.", tk.END, regexp=True)
    if indices:
        chat_history.delete(indices, tk.END)
    chat_history.insert(tk.END, "\n" + message + "\n", tag) # Added newline before message
    chat_history.configure(state='disabled')
    chat_history.see(tk.END)

def send_message():
    """Sends a message to Grok and updates the UI."""
    user_input = entry_box.get()
    update_chat_history("You: " + user_input, "user")
    entry_box.delete(0, tk.END)

    update_chat_history("Grok: Loading...", "grok")
    root.update_idletasks()

    grok_response = get_grok_response(user_input)
    update_chat_history("Grok: " + grok_response, "grok")


def create_gui():
    """Creates and configures the main GUI."""
    global root, chat_history, entry_box  # Declare globals for access in other functions

    root = tk.Tk()
    root.title("Grok Chatbot")
    root.configure(bg="#ADD8E6")

    chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='disabled', bg="#F0FFFF", fg="#000080")
    chat_history.tag_configure("user", foreground="#008000")
    chat_history.tag_configure("grok", foreground="#000080")
    chat_history.pack(pady=10, padx=10)

    entry_box = tk.Entry(root, width=60, bg="#E0FFFF")
    entry_box.pack(pady=5)

    send_button = tk.Button(root, text="Send", command=send_message, bg="#90EE90")
    send_button.pack()

    root.mainloop()


def main():
    """Starts the main program."""
    create_gui()


if __name__ == "__main__":
    main()
