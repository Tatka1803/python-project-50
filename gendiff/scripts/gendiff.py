import argparse
from gendiff.generate_diff import generate_diff

def parsing_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('file_path_1')
    parser.add_argument('file_path_2')
    parser.add_argument(
        "-f",
        "--format",
        default='stylish',
        help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)

def main():
    args = parsing_arguments()
    diff = generate_diff(args.file_path_1, args.file_path_2, args.format)
    print(diff)


if __name__ == '__main__':
    main()