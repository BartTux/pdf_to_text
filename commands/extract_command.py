from core.pdf_processor import PDF_Processor


class ExtractCommand:
    def __init__(self, args):
        self.args = args
        self.processor = PDF_Processor()

    def execute(self) -> None:
        try:
            if self.processor.extract_text_from_pdf(self.args.file, self.args.output):
                print('PDF content has been extracted sucessfully!')
        except FileNotFoundError as ex:
            print(f'Cannot find the file with given path: {ex}')
        except PermissionError as ex:
            print('You have no permissions into the directory')
