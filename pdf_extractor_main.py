import PyPDF2
import pandas as pd

def extract_pdf_fields_to_excel(pdf_path, output_excel_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        fields = reader.get_fields()

        data = []
        if fields:
            for field_key, field_data in fields.items():
                data.append({
                    "Field Key": field_key,  # Appian needs this
                    "Field Type (/FT)": str(field_data.get('/FT')),  # Text, Button, Choice
                    "Export Value (/V)": field_data.get('/V'),  # Current/default value
                    "Options (/Opt)": field_data.get('/Opt'),  # Dropdown/radio options
                    "Field Flags (/Ff)": field_data.get('/Ff'),  # Bitmask: readonly, required
                    "Max Length (/MaxLen)": field_data.get('/MaxLen')  # Limit for text input
                })

        df = pd.DataFrame(data)
        df.to_excel(output_excel_path, index=False)
        print(f"✅ Excel file created: {output_excel_path}")

# 🔧 Example usage — replace with your PDF path
# Place this at the bottom of your script
extract_pdf_fields_to_excel(
    "/Users/matthewpoepoe/Documents/complex_sample_form.pdf",
    "/Users/matthewpoepoe/Documents/pdf_field_properties.xlsx"
)
