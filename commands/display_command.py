from core.pdf_processor import PDF_Processor


class DisplayCommand:
    def __init__(self, args):
        self.args = args
        self.processor = PDF_Processor()

    def execute(self) -> None:
        try:
            content = self.processor.load_content(self.args.output)
            print(content)
        except FileNotFoundError as ex:
            print('You have extracted no PDF file. You need to extract file in order to display it. ')