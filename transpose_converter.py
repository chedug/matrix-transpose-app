from tkinter import Tk, Label, Entry, Button, messagebox


class MatrixTransposeApp:
    def __init__(self, master):
        self.master = master
        master.title('Matrix Transpose App')

        # Initial instructions
        self.label = Label(master, text="Enter matrix size and press 'Generate'")
        self.label.grid(row=0, columnspan=4)

        # Matrix size entries
        self.rows_label = Label(master, text="Rows:")
        self.rows_label.grid(row=1, column=0)
        self.rows_entry = Entry(master)
        self.rows_entry.grid(row=1, column=1)

        self.cols_label = Label(master, text="Cols:")
        self.cols_label.grid(row=1, column=2)
        self.cols_entry = Entry(master)
        self.cols_entry.grid(row=1, column=3)

        # Generate matrix input grid button
        self.generate_button = Button(master, text="Generate", command=self.generate_input_grid)
        self.generate_button.grid(row=2, columnspan=4)

        # Dynamic attributes
        self.matrix_entries = []
        self.transpose_button = None

    def generate_input_grid(self):
        # Get matrix dimensions
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for rows and columns.")
            return

        self._clear_entries()

        self._generate_matrix_input_fields(rows, cols)

        # Button to calculate and display transpose
        self.transpose_button = Button(self.master, text="Transpose", command=self.display_transpose)
        self.transpose_button.grid(row=rows+3, columnspan=cols)

    def display_transpose(self):
        try:
            matrix = [[MatrixTransposeApp._get_entry(entry) for entry in row] for row in self.matrix_entries]
        except ValueError:
            messagebox.showerror("Invalid Input", "Please ensure all matrix entries are numbers.")
            return

        transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        # Format the result for display
        result = '\n'.join([
            '\t'.join([
                f"{cell: >7}" if isinstance(cell, int) else f"{cell: >7.2f}" for cell in row
            ]) for row in transpose
        ])
        messagebox.showinfo("Transposed Matrix", result)

    def _clear_entries(self):
        # Clear previous entries if any
        for entry_row in self.matrix_entries:
            for entry in entry_row:
                entry.destroy()
        if self.transpose_button:
            self.transpose_button.destroy()

    def _generate_matrix_input_fields(self, rows, cols):
        self.matrix_entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = Entry(self.master, width=5)
                entry.grid(row=i+3, column=j)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)


    @staticmethod
    def _get_entry(entry):
        val = float(entry.get())
        if val.is_integer():
            val = int(val)
        return val


root = Tk()
my_gui = MatrixTransposeApp(root)
root.mainloop()

