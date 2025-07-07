import json
import tkinter as tk
from tkinter import messagebox

try:
    with open('questions.json', 'r') as file:
        questions = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    messagebox.showerror("Error", f"Failed to load questions: {e}")
    exit()

OPTIONS = [1, 2, 3, 4, 5]
FONT_QUESTION = ("Arial", 12)
FONT_OPTION = ("Arial", 10)
FONT_BUTTON = ("Arial", 12)

response_vars = []

def submit():
    answers = []
    for i, question in enumerate(questions):
        selected = response_vars[i].get()
        if selected == -1:
            tk.messagebox.showwarning("Incomplete", f"You didn't answer: '{question}'")
            return
        answers.append(OPTIONS[selected])

    score = sum(
        5 - ans if i % 2 == 1 else ans - 1
        for i, ans in enumerate(answers)
    ) * 2.5

    if score >= 85:
        evaluation = "Excellent"
    elif score >= 70:
        evaluation = "Good"
    elif score >= 50:
        evaluation = "OK / Marginal"
    else:
        evaluation = "Poor"

    summary = (
        f"Final SUS Score: {score:.1f}\n"
        f"\nEvaluation: {evaluation}"
    )

    messagebox.showinfo("SUS Score Results", summary)

root = tk.Tk()
root.geometry("1000x600")
root.title("System Usability Scale (SUS)")

for i, question in enumerate(questions):
    label = tk.Label(root, text=f"{i+1}. {question}", font=FONT_QUESTION, anchor="w", justify="left")
    label.grid(row=i, column=0, sticky="w", padx=10, pady=(10, 0))

    var = tk.IntVar(value=-1)
    response_vars.append(var)

    for j, option in enumerate(OPTIONS):
        rb = tk.Radiobutton(root, text=str(option), variable=var, value=j, font=FONT_OPTION)
        rb.grid(row=i, column=j + 1, padx=5, pady=(10, 0), sticky="w")

submit_btn = tk.Button(root, text="Submit", command=submit, font=FONT_BUTTON)
submit_btn.grid(row=len(questions), column=0, columnspan=6, pady=40)

# Run the app
root.mainloop()
