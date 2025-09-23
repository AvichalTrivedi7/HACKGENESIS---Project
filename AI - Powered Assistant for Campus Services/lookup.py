import json
import tkinter as tk
from tkinter import scrolledtext
from llama_cpp import Llama

# === Load Dataset ===
with open("dataset.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

# === Load Mistral Model ===
llm = Llama(
    model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    max_tokens=512,
    temperature=0.3,
    top_p=0.9,
    repeat_penalty=1.1
)

def search_dataset(user_input):
    """
    Use LLM to act like a Campus Assistant with access to mock student data.
    """
    dataset_text = json.dumps(dataset, indent=2)

    prompt = f"""
You are a helpful Campus AI Assistant inside the Unified Campus Identity System.
Use the mock student dataset below to answer queries realistically.

Dataset:
{dataset_text}

User query: {user_input}

Respond in Structured format about answer, details and source.
"""
    
    response = llm(prompt, max_tokens=256, stop=["</s>"])
    return response["choices"][0]["text"].strip()

# === Tkinter GUI ===
def get_result():
    query = entry.get()
    if not query.strip():
        output_box.insert(tk.END, "\n Please enter query.\n")
        return
    output_box.insert(tk.END, f"\n🔍 Query: {query}\n")
    result = search_dataset(query)
    output_box.insert(tk.END, f"✅ Result: {result}\n")
    output_box.see(tk.END)

# Window setup
root = tk.Tk()
root.title("Unified Campus Lookup Assistant")
root.geometry("700x500")

# Label
label = tk.Label(root, text="Enter Query:", font=("Arial", 12))
label.pack(pady=5)

# Input field
entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(pady=5)

# Search button
btn = tk.Button(root, text="Search", command=get_result, font=("Arial", 12), bg="lightblue")
btn.pack(pady=5)

# Output box
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Arial", 11))
output_box.pack(pady=10)

# Run GUI
root.mainloop()
