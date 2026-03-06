import os
from services.compress_service import compress_pdf

def compress_folder(folder):
    results = []

    for file in os.listdir(folder):
        if file.lower().endswith(".pdf"):
            input_path = os.path.join(folder, file)
            output_path = os.path.join(folder, "compressed_" + file)

            compress_pdf(input_path, output_path)

            results.append((input_path, output_path))

    return results