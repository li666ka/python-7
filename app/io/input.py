"""
  This function reads text from the console and returns it as a string.
"""


def read_from_console():
    text = input()
    return text


"""
  This function reads text from a file using Python built-ins and returns it as a string.

  Args:
    filename: Path to the file.

  Returns:
    String containing the text from the file.
"""


def read_from_file_python(filename):
    with open(filename, "r") as f:
        text = f.read()
    return text


"""
  This function reads text from a file using the Pandas library and returns it as a DataFrame.

  Args:
    filename: Path to the file.

  Returns:
    DataFrame containing the data from the file.
"""


def read_from_file_pandas(filename):
    df = pd.read_csv(filename)
    return df
