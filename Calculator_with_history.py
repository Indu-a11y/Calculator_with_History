# ===================================================
# Calculator with History - GUI Application
# Author: Indra Chand
# Description: A beautiful calculator with history using Tkinter
# ===================================================

import tkinter as tk
from tkinter import messagebox

# List to store calculation history
calculation_history = []


class CalculatorApp:
    """Main Calculator Application Class"""
    
    def __init__(self, root):
        """Initialize the calculator application."""
        self.root = root
        self.root.title("Calculator with History")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")
        
        # Variable to store current expression
        self.expression = ""
        
        # Create all the widgets
        self.create_display()
        self.create_buttons()
        self.create_history_panel()
    
    def create_display(self):
        """Create the calculator display screen."""
        # Main display frame
        display_frame = tk.Frame(self.root, bg="#2C3E50")
        display_frame.pack(pady=20, padx=10, fill="x")
        
        # Display label for showing expression
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 28, "bold"),
            bg="#34495E",
            fg="white",
            justify="right",
            bd=0,
            insertbackground="white"
        )
        self.display.pack(fill="x", ipady=15, padx=5)
    
    def create_buttons(self):
        """Create all calculator buttons."""
        # Button frame
        button_frame = tk.Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=10, padx=10)
        
        # Button layout - rows of buttons
        buttons = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "H"]
        ]
        
        # Create buttons in grid
        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                # Choose button color based on type
                if button_text in ["/", "*", "-", "+", "="]:
                    bg_color = "#E74C3C"  # Red for operators
                elif button_text in ["C", "←", "%", "H"]:
                    bg_color = "#3498DB"  # Blue for special
                else:
                    bg_color = "#ECF0F1"  # Light for numbers
                
                # Text color
                if button_text in ["/", "*", "-", "+", "=", "C", "←", "%", "H"]:
                    fg_color = "white"
                else:
                    fg_color = "#2C3E50"
                
                # Create button
                btn = tk.Button(
                    button_frame,
                    text=button_text,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg=fg_color,
                    width=5,
                    height=2,
                    bd=0,
                    command=lambda x=button_text: self.on_button_click(x)
                )
                btn.grid(row=row_index, column=col_index, padx=3, pady=3)
    
    def create_history_panel(self):
        """Create the history display panel."""
        # History frame
        history_frame = tk.Frame(self.root, bg="#2C3E50")
        history_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # History label
        history_label = tk.Label(
            history_frame,
            text="📜 Calculation History",
            font=("Arial", 12, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        history_label.pack(anchor="w")
        
        # History listbox
        self.history_list = tk.Listbox(
            history_frame,
            font=("Arial", 11),
            bg="#34495E",
            fg="white",
            bd=0,
            height=6,
            selectbackground="#3498DB"
        )
        self.history_list.pack(fill="both", expand=True, pady=5)
    
    def on_button_click(self, button_text):
        """Handle button click events."""
        if button_text == "C":
            # Clear the display
            self.expression = ""
            self.display.delete(0, tk.END)
        
        elif button_text == "←":
            # Backspace - remove last character
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        
        elif button_text == "H":
            # Show history info
            if len(calculation_history) == 0:
                messagebox.showinfo("History", "No calculations yet!")
            else:
                history_text = "\n".join(calculation_history[-10:])
                messagebox.showinfo("History", history_text)
        
        elif button_text == "=":
            # Calculate the result
            self.calculate_result()
        
        else:
            # Add the button text to expression
            self.expression += button_text
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
    
    def calculate_result(self):
        """Calculate and display the result."""
        try:
            # Store original expression
            original_expression = self.expression
            
            # Handle percentage
            expression_to_eval = self.expression.replace("%", "/100")
            
            # Calculate result using eval (safe for calculator)
            result = eval(expression_to_eval)
            
            # Round result if it's a float
            if isinstance(result, float):
                result = round(result, 8)
            
            # Save to history
            history_record = f"{original_expression} = {result}"
            calculation_history.append(history_record)
            
            # Update history listbox
            self.history_list.insert(tk.END, history_record)
            self.history_list.see(tk.END)  # Scroll to latest
            
            # Display result
            self.expression = str(result)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.expression = ""
            self.display.delete(0, tk.END)
            
        except Exception as error:
            messagebox.showerror("Error", "Invalid expression!")
            self.expression = ""
            self.display.delete(0, tk.END)


def main():
    """Main function to start the calculator."""
    # Create the main window
    root = tk.Tk()
    
    # Create calculator app
    app = CalculatorApp(root)
    
    # Start the application
    root.mainloop()


# Run the calculator when this file is executed
if __name__ == "__main__":
    main()
