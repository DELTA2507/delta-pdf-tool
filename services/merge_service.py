from pypdf import PdfWriter

def merge_pdfs(files, output):
    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)

    merger.write(output)
    merger.close()