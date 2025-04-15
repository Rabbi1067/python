#Extracting tables from docx files


def extract_tables_from_docx(docx_path):
#Defines a function that extracts all tables from a .docx file.
doc = Document(docx_path)
#Loads the Word file into a Document object.
tables = []   #EMPTY tables
for table in doc.tables:  #Starts looping through each table in the document.
        table_data = []
        for row in table.rows:  #For each row in the current table, prepare a list to store the cell data.
            row_data = []
            for cell in row.cells:    #Extracts text from each cell and adds it to the row list.
                row_data.append(cell.text)
            table_data.append(row_data)   #Adds the complete row to the current table
        tables.append(table_data) #Adds the full table (now a list of rows) to the tables list.
    return tables   #Returns the final list of all tables
# 📄 Input path to your .docx file 
docx_path = "C:\\Users\\Local User\\Pictures\\assignment seu\\DBL final update 2021100000002-sheikh md. salman farsi.docx"

# 🔄 Extract all tables
tables = extract_tables_from_docx(docx_path)

# 🖨️ Print each table with row data
for i, table in enumerate(tables):
    print(f"\n🔸 Table {i + 1}:\n")
    for row in table:
        print(row)
