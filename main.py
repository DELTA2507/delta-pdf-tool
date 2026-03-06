import os
import webview
from services.compress_service import compress_pdf
from services.merge_service import merge_pdfs
from services.compress_folder_service import compress_folder

class Api:

    def compress(self, input_file, output_file):
        compress_pdf(input_file, output_file)
        return True

    def merge(self, files, output_file):
        merge_pdfs(files, output_file)
        return True

    def compress_folder(self, folder):
        return compress_folder(folder)


if __name__ == "__main__":
    api = Api()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_dir, "frontend", "index.html")
    webview.create_window(
        "DELTA PDF TOOL",
        html_path,
        js_api=api
    )
    webview.start()