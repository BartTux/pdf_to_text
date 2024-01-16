from argparse import ArgumentParser, Namespace
from commands import display_command, extract_command


def main() -> None:
    parser = ArgumentParser(description='Convert PDF to the text format')

    parser.add_argument('-f', '--file', help='Path to the PDF file', type=str)
    parser.add_argument('-o', '--outputcle', help='Path to the output text file', type=str, default='p2t_datastore.txt')
    parser.add_argument('-d', '--display', help='Display extracted PDF content', action='store_true')

    args: Namespace = parser.parse_args()


    if args.file is not None:
        command = extract_command.ExtractCommand(args)
        command.execute()

    if args.display:
        command = display_command.DisplayCommand(args)
        command.execute()


if __name__ == '__main__':
    main()
