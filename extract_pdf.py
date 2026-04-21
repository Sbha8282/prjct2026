import PyPDF2

# Open the PDF file
with open('/workspaces/prjct2026/pravin (1).pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Extract text from all pages
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    
    # Save to a text file
    with open('/workspaces/prjct2026/sample_text.txt', 'w') as out_file:
        out_file.write(text)

print("Text extracted from PDF and saved to sample_text.txt")