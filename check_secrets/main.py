# print_arguments/main.py
import argparse
import os

def print_arguments(arguments: list[str]):
    print(os.system("pwd"))
    print(os.system("ls"))
    # os.system("brew tap trufflesecurity/trufflehog")
    # os.system("brew install trufflehog")
    
    for argument in arguments:
        pass
        # print(argument)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    print_arguments(args.filenames)


if __name__ == "__main__":
    main()