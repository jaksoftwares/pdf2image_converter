import os
import fitz  # PyMuPDF

def convert_pdfs_to_images(input_folder, output_folder):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            
            # Get PDF name without extension
            pdf_name = os.path.splitext(filename)[0]

            print(f"Processing: {filename}...")

            # Open the PDF using PyMuPDF
            pdf_document = fitz.open(pdf_path)
            page_count = len(pdf_document)
            
            for page_num in range(page_count):
                page = pdf_document[page_num]
                
                # Render the page as an image (300 DPI for high quality)
                zoom = 300 / 72  # 72 is the default DPI in PyMuPDF
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat)
                
                # Save directly to output folder with PDF name and page number
                image_name = f"{pdf_name}_page_{page_num + 1}.png"
                image_path = os.path.join(output_folder, image_name)
                pix.save(image_path)
            
            pdf_document.close()
            print(f"Done! Saved {page_count} image(s) from {filename}")

if __name__ == "__main__":
    # PDFs are in the current directory
    source_directory = "."
    destination_directory = "./converted_images"

    convert_pdfs_to_images(source_directory, destination_directory)
