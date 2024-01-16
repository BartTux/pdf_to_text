from PyPDF2 import PdfReader


class PDF_Processor:
    def extract_text_from_pdf(self, pdf_file: str, output_file: str) -> bool:
        with open(pdf_file, 'rb') as pdf:
            reader = PdfReader(pdf, strict=False)
            extracted_content = ''

            for page in reader.pages:
                extracted_content += page.extract_text()

            self.save_content(extracted_content, output_file)
            return True

    def save_content(self, content: str, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(content)

    def load_content(self, filename: str) -> str:
        with open(filename, 'r') as f:
            content = f.read()

        return content