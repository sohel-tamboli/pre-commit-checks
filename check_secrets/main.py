# print_arguments/main.py
import argparse
import os
import subprocess

def print_arguments(arguments: list[str]):
    # print(os.system("pwd"))
    pwd = os.getcwd()
    # print(os.system("ls")
    subprocess.run("brew tap trufflesecurity/trufflehog", stdout= subprocess.DEVNULL)
    subprocess.run("brew install trufflehog", stdout= subprocess.DEVNULL)
    
    os.system(f"trufflehog filesystem --directory=.")
    # for argument in arguments:
    #     print(os.system(f"trufflehog filesystem ."))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    print_arguments(args.filenames)


if __name__ == "__main__":
    main()