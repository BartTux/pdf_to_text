import unittest
from unittest.mock import mock_open, patch

from core.pdf_processor import PDF_Processor


class TestPDF_Processor(unittest.TestCase):

    def test_load_content(self):
        file_path = 'file_path'
        mock = mock_open(read_data='This is an example pdf..')

        with patch('builtins.open', mock) as mocked_open:
            processor = PDF_Processor()
            result = processor.load_content(file_path)

            self.assertEqual(result, 'This is an example pdf..')
            mock.assert_called_with(file_path, 'r')


if __name__ == '__main__':
    unittest.main()