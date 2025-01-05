import sys

# from interpreter_utils.if_version.TreeParser_v1 import evalProgram
from interpreter_utils.TreeParser import evalProgram


def main():
    if len(sys.argv) != 2:
        print("Use: python script.py <nombre_archivo>")
        sys.exit(1)
    scheme_program = sys.argv[1]
    try:
        evalProgram(input_program=scheme_program, show_visit_tree=0)

    except FileNotFoundError:
        print(f"Error: The file '{scheme_program}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error was generated: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
