import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Create the main window.
root = tk.Tk()
root.title("Polynomial Graph Calculator")

# Create a text box for the polynomial equation.
polynomial_label = tk.Label(root, text="Polynomial Equation:")
polynomial_entry = tk.Entry(root)
polynomial_label.grid(row=0, column=0)
polynomial_entry.grid(row=0, column=1)

# Create two text boxes for the x-axis and y-axis ranges.
x_axis_label = tk.Label(root, text="X-Axis Range:")
x_axis_low_entry = tk.Entry(root)
x_axis_high_entry = tk.Entry(root)
x_axis_label.grid(row=1, column=0)
x_axis_low_entry.grid(row=1, column=1)
x_axis_high_entry.grid(row=1, column=2)

y_axis_label = tk.Label(root, text="Y-Axis Range:")
y_axis_low_entry = tk.Entry(root)
y_axis_high_entry = tk.Entry(root)
y_axis_label.grid(row=2, column=0)
y_axis_low_entry.grid(row=2, column=1)
y_axis_high_entry.grid(row=2, column=2)

# Create a button to graph the polynomial.
graph_button = tk.Button(root, text="Graph")
graph_button.grid(row=3, column=0)


# Bind the graph button to a function that will graph the polynomial.
def graph_polynomial():
    # Get the polynomial equation from the text box.
    polynomial = polynomial_entry.get()

    # Check if the polynomial equation is valid.
    try:
        np.poly1d(np.array(polynomial.split(), dtype=float))
    except:
        tk.messagebox.showerror("Error", "Invalid polynomial equation.")
        return

    # Get the x-axis and y-axis ranges from the text boxes.
    x_axis_low = float(x_axis_low_entry.get())
    x_axis_high = float(x_axis_high_entry.get())
    y_axis_low = float(y_axis_low_entry.get())
    y_axis_high = float(y_axis_high_entry.get())

    # Generate x-axis data and evaluate the polynomial.
    x_data = np.linspace(x_axis_low, x_axis_high, 1000)
    y_data = np.polyval(np.poly1d(np.array(polynomial.split(), dtype=float)), x_data)

    # Graph the polynomial.
    plt.plot(x_data, y_data)
    plt.ylim(y_axis_low, y_axis_high)
    plt.show()


# Bind the graph button to the graph_polynomial function.
graph_button.config(command=graph_polynomial)

# Run the app.
root.mainloop()
