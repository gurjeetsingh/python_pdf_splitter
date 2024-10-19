import PyPDF2

# List of names for the output PDF files
names = [
    "John Smith", "Michael Johnson", "Emily Brown", "Sarah Wilson", 
    "Olivia Taylor", "Emma Davis", "David Miller", "Sophia Thompson", 
    "Patricia Anderson", "Rachel Roberts", "James Harris", "Isabella Clark", 
    "Mia Lewis", "Daniel White", "Joseph King", "Ethan Scott", 
    "Lisa Lee", "Alexander Young", "Lily Adams", 
    "Joshua Martinez", "Gabriel Hall", "Rebecca Allen", "Brittany Turner"
]

# Input PDF file
input_pdf = "input.pdf"

# Open the PDF file
with open(input_pdf, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    # Ensure the number of names matches the number of pages
    if len(names) != num_pages:
        print(f"Error: Number of names ({len(names)}) does not match the number of pages ({num_pages}).")
    else:
        # Loop through each page and save it as a separate PDF file
        for i in range(num_pages):
            output_pdf_name = f"{names[i]}.pdf"
            pdf_writer = PyPDF2.PdfWriter()

            # Extract the page and add it to the writer
            pdf_writer.add_page(pdf_reader.pages[i])

            # Write the page to a new file
            with open(output_pdf_name, "wb") as output_pdf_file:
                pdf_writer.write(output_pdf_file)

            print(f"Page {i+1} saved as {output_pdf_name}")
