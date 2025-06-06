import tkinter as tk

calc = ""


def add_to_calc(symbol):
    global calc
    calc += str(symbol)
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calc)


def evaluate_calc():
    global calc
    try:
        calc = str(eval(calc))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calc)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calc
    calc = ""
    text_result.delete(1.0, tk.END)


root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

text_result = tk.Text(root, height=2, width=24, font=("Arial", 22), bg="lightgrey")
text_result.grid(columnspan=5)

button1 = tk.Button(root, text="1", command=lambda: add_to_calc(1), width=5, height=2, font=("Arial", 18))
button1.grid(row=2, column=1)
button2 = tk.Button(root, text="2", command=lambda: add_to_calc(2), width=5, height=2, font=("Arial", 18))
button2.grid(row=2, column=2)
button3 = tk.Button(root, text="3", command=lambda: add_to_calc(3), width=5, height=2, font=("Arial", 18))
button3.grid(row=2, column=3)
button4 = tk.Button(root, text="4", command=lambda: add_to_calc(4), width=5, height=2, font=("Arial", 18))
button4.grid(row=2, column=4)
button5 = tk.Button(root, text="5", command=lambda: add_to_calc(5), width=5, height=2, font=("Arial", 18))
button5.grid(row=3, column=1)
button6 = tk.Button(root, text="6", command=lambda: add_to_calc(6), width=5, height=2, font=("Arial", 18))
button6.grid(row=3, column=2)
button7 = tk.Button(root, text="7", command=lambda: add_to_calc(7), width=5, height=2, font=("Arial", 18))
button7.grid(row=3, column=3)
button8 = tk.Button(root, text="8", command=lambda: add_to_calc(8), width=5, height=2, font=("Arial", 18))
button8.grid(row=3, column=4)
button9 = tk.Button(root, text="9", command=lambda: add_to_calc(9), width=5, height=2, font=("Arial", 18))
button9.grid(row=4, column=1)
button0 = tk.Button(root, text="0", command=lambda: add_to_calc(0), width=5, height=2, font=("Arial", 18))
button0.grid(row=4, column=2)


root.mainloop()

