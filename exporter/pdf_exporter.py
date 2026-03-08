import pdfkit

path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)


def html_to_pdf(html_path, pdf_path):
    options = {
        'enable-local-file-access': None,
        'quiet': ''
    }
    try:
        pdfkit.from_file(html_path, pdf_path, configuration=config, options=options)
    except Exception as e:
        print(f"Warning from pdfkit: {e}")