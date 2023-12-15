import tabula
import pandas as pd

def convert_pdf_to_excel(pdf_path, excel_output):
    # Read PDF and extract tables
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Combine tables into a single DataFrame
    combined_df = pd.concat(tables, ignore_index=True)

    # Save the combined DataFrame to an Excel file
    combined_df.to_excel(excel_output, index=False)

if __name__ == "__main__":
    pdf_file_path = "input.pdf"  # Replace with your PDF file path
    excel_output_path = "output.xlsx"  # Replace with your desired Excel output path

    convert_pdf_to_excel(pdf_file_path, excel_output_path)

