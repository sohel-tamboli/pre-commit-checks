# print_arguments/main.py
import argparse
import os

def print_arguments(arguments: list[str]):
    # print(os.system("pwd"))
    pwd = os.getcwd()
    # print(os.system("ls")
    os.system("brew tap trufflesecurity/trufflehog")
    os.system("brew install trufflehog")
    
    print(os.system(f"trufflehog filesystem ."))
    # for argument in arguments:
    #     print(os.system(f"trufflehog filesystem ."))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    print_arguments(args.filenames)


if __name__ == "__main__":
    main()