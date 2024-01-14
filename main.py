from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        pdf_text = []

        for index in range(0, 4):
            content = reader.pages[index].extract_text()
            pdf_text.append(content)

        return pdf_text


if __name__ == '__main__':
    try:
        extracted_text = extract_text_from_pdf('E:\PyCharm\Projects\\test2.pdf')

        for text in extracted_text:
            print(text)
    except FileNotFoundError as ex:
        print('Nie znaleziono pliku')
