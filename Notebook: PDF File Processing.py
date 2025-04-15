# 1.Import Required Libraries

import PyPDF2 as pdf#Imports the PyPDF2 library using the alias pdf. It's used to read, split, merge, and manipulate PDF files.
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
"""Directly imports core classes from PyPDF2:
PdfReader: to read PDF 
PdfWriter: to create or modify PDF  
PdfMerger: to merge multiple PDFs"""
import os #This is Python’s built-in library to interact with the operating system. You can work with file paths, check if files/folders exist, create folders, etc.
from PIL import Image  ##Imports the Image class from the PIL (Pillow) library. It helps in opening, editing, saving images.
import tabula as tab  #tabula is a library used to extract tables from PDF files (mostly works best with Java installed).


#2. Basic PDF Operations
# Open and read PDF
file = open("path/to/file.pdf", "rb")  # Open the PDF file in 'read binary' mode
reader = PdfReader(file)  # Create a PdfReader object to read the PDF

# Get metadata
info = reader.metadata  # Extract the metadata of the PDF (e.g., author, title, etc.)
print(info.author)  # Print the author of the PDF
print(len(reader.pages))  # Print the number of pages in the PDF

# Extract text from a specific page (index 3, which is the 4th page)
print(reader.pages[3].extract_text())  # Extract and print text from page 4

#output: Shows the PDF's metadata and text on a specific page.


#3. Extract Text from PDF

from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    # Open the PDF file in binary read mode
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)  # Create PdfReader object to read the PDF
        
        # Extract text from each page and join them with a newline separator
        return '\n'.join([page.extract_text() for page in reader.pages])  # Returning the text

# Path to your PDF file
text = extract_text_from_pdf("path/to/file.pdf")  # Replace with actual PDF file path
print(text)  # Print the extracted text

"""output: 
Page 1 content...
Page 2 content...
Page 3 content...
_ _ _"""

# 4. Split PDF into Single Pages

from PyPDF2 import PdfReader, PdfWriter

def split_pdf(pdf_path):
    # Read the PDF file using PdfReader
    reader = PdfReader(pdf_path)
    
    # Iterate over all the pages in the PDF
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()  # Create a PdfWriter object to write pages to a new file
        
        # Add the current page to the writer
        writer.add_page(page)
        
        # Define the output filename for each page
        output = f"page_{i+1}.pdf"  # This creates files like page_1.pdf, page_2.pdf, etc.
        
        # Write the page to a new PDF file
        with open(output, "wb") as out:
            writer.write(out)
        
        # Print confirmation message
        print(f"Created: {output}")  # Notify that the page has been split and saved

# Call the function with the path to your PDF file
split_pdf("path/to/file.pdf")  # Replace with actual PDF file path

"""output:
Created: page_1.pdf
Created: page_2.pdf
Created: page_3.pdf"""


# 5. Merge Multiple PDFs

from PyPDF2 import PdfMerger  # Import PdfMerger class from PyPDF2

def merge_pdfs(pdf_list, output="merged.pdf"):
    merger = PdfMerger()  # Create merger object | PdfMerger অবজেক্ট তৈরি করো
    
    for pdf_file in pdf_list:
        merger.append(pdf_file)  # Add each PDF file to merger | প্রতিটি পিডিএফ মের্জ করো

    merger.write(output)  # Save the merged file | একত্রিত ফাইল সংরক্ষণ করো

    print(f"Merged file saved as: {output}")  # ✅ Success message

# Call the function with a list of PDF files
merge_pdfs(["file1.pdf", "file2.pdf"])  # Example input

#output: Merged file saved as: merged.pdf


# 6. Rotate PDF Pages

from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(pdf_path, page_num, rotation=90):
    reader = PdfReader(pdf_path)        # 📖 Load the PDF file | পিডিএফ ফাইল লোড করো
    writer = PdfWriter()                # 🖊️ Create a writer object | লেখার অবজেক্ট তৈরি করো
    page = reader.pages[page_num]       # 📄 Pick the specific page | নির্দিষ্ট পৃষ্ঠা বেছে নাও
    page.rotate(rotation)               # 🔄 Rotate the page | পৃষ্ঠাটি ঘোরাও
    writer.add_page(page)               # ➕ Add the rotated page to writer | ঘোরানো পৃষ্ঠা যোগ করো

    # 💾 Save the result
    with open("rotated.pdf", "wb") as out:
        writer.write(out)
        print("✅ Saved rotated PDF as: rotated.pdf")

# 🔧 Usage Example | উদাহরণ
rotate_pdf("path/to/file.pdf", 0, 180)  # প্রথম পৃষ্ঠাকে ১৮০ ডিগ্রি ঘোরাও
#output: rotate_pdf("example.pdf", 0, 180)


#7. Extract Images from PDF

import fitz  # pip install pymupdf
import os

def extract_images(pdf_path, output_dir="images"):
    # 📄 Open the PDF | PDF ফাইল খুলো
    doc = fitz.open(pdf_path)

    # 📁 Make directory if it doesn’t exist | ফোল্ডার না থাকলে তৈরি করো
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img_count = 0

    # 🔁 Go through each page | প্রতিটি পৃষ্ঠা ঘুরে দেখো
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]  # ইমেজের রেফারেন্স আইডি
            base_image = doc.extract_image(xref)

            image_data = base_image["image"]  # বাইনারি ডেটা
            image_ext = base_image["ext"]     # ফাইল এক্সটেনশন (jpg, png, etc.)

            image_name = f"page{page_num+1}_img{img_index+1}.{image_ext}"
            image_path = os.path.join(output_dir, image_name)

            with open(image_path, "wb") as f:
                f.write(image_data)

            print(f"✅ Saved: {image_path}")
            img_count += 1

    print(f"🎉 Total {img_count} images extracted.")

# 🚀 Call the function | ফাংশন চালাও
extract_images("path/to/your/file.pdf")


# 8. Convert Image to PDF

from PIL import Image
import os

def img_to_pdf(image_path):
    # 📷 Open the image | ছবি ওপেন করো
    img = Image.open(image_path)
    
    # 🧾 Create PDF filename | PDF ফাইলের নাম তৈরি করো
    pdf_path = os.path.splitext(image_path)[0] + ".pdf"

    # 💾 Save image as PDF | ছবিকে PDF হিসেবে সংরক্ষণ করো
    img.save(pdf_path)

    # ✅ Show success message | সফল মেসেজ দেখাও
    print(f"Converted: {pdf_path}")

# 🚀 Example call | উদাহরণ
img_to_pdf("image.png")

#Converted: image.pdf


# 9. Extract Tables from PDF (using tabula)

import tabula

# 🔍 Extract all tables from the PDF | পিডিএফ-এর সব টেবিল বের করো
tables = tabula.read_pdf("path/to/file.pdf", pages="all")

# 💾 Save the first table as a CSV file | প্রথম টেবিলটি CSV হিসেবে সংরক্ষণ করো
tables[0].to_csv("table_1.csv")

# 📄 Extract tables from a specific page | নির্দিষ্ট পেজ (৭) থেকে টেবিল বের করো
page_tables = tabula.read_pdf("path/to/file.pdf", pages="7")

# 💾 Save each extracted table from page 7 | পেজ ৭ থেকে পাওয়া প্রতিটি টেবিল CSV ফাইলে সংরক্ষণ করো
for i, table in enumerate(page_tables):
    table.to_csv(f"page7_table{i}.csv")

"""
output:If the PDF has 3 tables on page 7, the following files will be saved:

page7_table0.csv

page7_table1.csv

page7_table2.csv"""

