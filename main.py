from argparse import ArgumentParser, Namespace
from PyPDF2 import PdfReader
from PyPDF2.generic import ContentStream


parser = ArgumentParser(description='Convert PDF to the text format')

parser.add_argument('-f', '--file', help='Path to the PDF file', type=str)
parser.add_argument('-d', '--display', help='Display extracted PDF content', action='store_true')

args: Namespace = parser.parse_args()

filename: str = 'p2t_datastore.txt'

def save_content(content: str, filename: str) -> None:
    with open(filename, 'w') as f:
        f.write(content)


def load_content(filename: str) -> str:
    with open(filename, 'r') as f:
        content = f.read()

    return content


def extract_text_from_pdf(pdf_file: str) -> bool:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)

        for page in reader.pages:
            content = page.extract_text()

        save_content(content, filename)
        return True


if __name__ == '__main__':
    if args.file is not None:
        try:
            if extract_text_from_pdf(args.file):
                print('PDF content has been extracted sucessfully!')

        except FileNotFoundError as ex:
            print(f'Cannot find the file with given path: {ex}')
        except PermissionError as ex:
            print('You have no permissions into the directory')

    if args.display:
        try:
            print(load_content(filename))
        except FileNotFoundError as ex:
            print('You have extracted no PDF file. You need to extract file in order to display it. ')
