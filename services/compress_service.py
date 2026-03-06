import os
import subprocess
import glob
import shutil


def find_ghostscript():

    gs = shutil.which("gswin64c")
    if gs:
        return gs

    paths = glob.glob(r"C:\Program Files\gs\*\bin\gswin64c.exe")

    if paths:
        return paths[0]

    raise FileNotFoundError("Ghostscript not found")


def compress_pdf(input_pdf, output_pdf):

    ghostscript = find_ghostscript()

    command = [
        ghostscript,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf}",
        input_pdf
    ]

    subprocess.run(command)