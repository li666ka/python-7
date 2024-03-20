"""
  This function prints text to the console.

  Args:
    text: The text to print.
"""


def print_to_console(text):
    print(text)


"""
  This function writes text to a file using Python built-ins.

  Args:
    filename: Path to the file.
    text: The text to write.
"""


def write_to_file_python(filename, text):
    with open(filename, "w") as f:
        f.write(text)


"""
  This function writes a DataFrame to a file using the Pandas library.

  Args:
    filename: Path to the file.
    df: The DataFrame to write.
"""


def write_to_file_pandas(filename, df):
    df.to_csv(filename)
