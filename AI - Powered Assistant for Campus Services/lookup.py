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
    Use LLM to infer the closest match from the dataset.
    """
    dataset_text = "\n".join(
        [f"- Ayurveda: {d['ayurveda']} | Biomedicine: {d['biomedicine']} | Explanation: {d['explanation']}"
         for d in dataset]
    )
    
    prompt = f"""
You are a medical assistant that maps Ayurveda terms to Allopathy/modern terms.
Dataset: {dataset_text}

User query: {user_input}

Answer in JSON format:
{{"Ayurveda": "...", "Biomedicine": "...", "Explanation": "..."}}
"""
    
    response = llm(prompt, max_tokens=256, stop=["</s>"])
    return response["choices"][0]["text"].strip()

# === Tkinter GUI ===
def get_result():
    query = entry.get()
    if not query.strip():
        output_box.insert(tk.END, "\n⚠️ Please enter a symptom/disease.\n")
        return
    output_box.insert(tk.END, f"\n🔍 Query: {query}\n")
    result = search_dataset(query)
    output_box.insert(tk.END, f"✅ Result: {result}\n")
    output_box.see(tk.END)

# Window setup
root = tk.Tk()
root.title("🩺 Ayurveda–Allopathy Lookup Assistant")
root.geometry("700x500")

# Label
label = tk.Label(root, text="Enter Symptom/Disease:", font=("Arial", 12))
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
