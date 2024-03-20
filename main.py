from app.io.input import read_from_console, read_from_file_python, read_from_file_pandas
from app.io.output import print_to_console


def main():
    text_from_console = read_from_console()
    text_from_file_python = read_from_file_python("input.txt")
    text_from_file_pandas = read_from_file_pandas("input.csv")

    print_to_console(text_from_console)
    print_to_console(text_from_file_python)
    print_to_console(text_from_file_pandas)

    with open("output.txt", "w") as f:
        f.write(text_from_console + "\n")
        f.write(text_from_file_python + "\n")
        f.write(text_from_file_pandas)


if __name__ == '__main__':
    main()
