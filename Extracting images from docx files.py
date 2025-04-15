from docx import Document
import os

def extract_images_from_docx(docx_path, output_dir):#output_dir = "C:\\Users\\Local User\\Desktop\\python_2308\\images"

    # 📄 Load the Word document | Word ডকুমেন্ট লোড করো
    doc = Document(docx_path)

    # 📁 Check if output folder exists, if not, create it | আউটপুট ফোল্ডার না থাকলে তৈরি করো
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_counter = 1  # ইমেজ নাম্বার গোনার জন্য কাউন্টার

    # 🔍 Loop through all relationships (including media) | সব মিডিয়া রিলেশনশিপ ঘুরে দেখো
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:  # যদি রিলেশনটি ইমেজ হয়
            image_data = rel.target_part.blob  # Actual image binary | ইমেজের বাইনারি ডেটা
            image_format = rel.target_ref.split('.')[-1]  # ফাইল এক্সটেনশন (png, jpg etc.)

            # কিছু ডকুমেন্টে ফরম্যাট নির্ভুল না থাকতে পারে, তাই নিরাপত্তা হিসেবে jpg ধরে নিচ্ছি
            if image_format not in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
                image_format = 'jpg'

            # 🖼️ Create filename like image_1.jpg | ফাইলের নাম তৈরি
            image_filename = f'image_{image_counter}.{image_format}'
            image_counter += 1

            # সম্পূর্ণ পাথ তৈরি করো
            image_path = os.path.join(output_dir, image_filename)

            # 📥 Save the image file | ইমেজ ফাইলটি সংরক্ষণ করো
            with open(image_path, 'wb') as img_file:
                img_file.write(image_data)

            print(f'Saved: {image_path}')  # ✅ Success message

# 🔧 File and output directory path
docx_path = "C:\\Users\\Local User\\Pictures\\assignment seu\\DBL final update 2021100000002-sheikh md. salman farsi.docx"
output_dir = "C:\\Users\\Local User\\Desktop\\python_2308\\images"

# 🚀 Run the function | ফাংশন চালাও
extract_images_from_docx(docx_path, output_dir)

"""
output:
Saved: C:\Users\Local User\Desktop\python_2308\images\image_1.png
Saved: C:\Users\Local User\Desktop\python_2308\images\image_2.png
...
Saved: C:\Users\Local User\Desktop\python_2308\images\image_57.png
"""
