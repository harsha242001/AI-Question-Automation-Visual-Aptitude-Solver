import pandas as pd
import os

from parser.extractor import extract_variables
from solver.math_solver import solve
from renderer.report_renderer import render_html as render_report_html
from renderer.html_renderer import render_html as render_single_html
from renderer.image_exporter import export_image
from exporter.pdf_exporter import html_to_pdf


def main():

    print("Loading questions dataset...")

    df = pd.read_excel("data/questions.xlsx")

    print("Total Questions Found:", len(df))

    results = []
    
    os.makedirs("output", exist_ok=True)
    
    import base64
    with open("assets/books.png", "rb") as bf:
        b64_img = base64.b64encode(bf.read()).decode('utf-8')

    for i, row in df.iterrows():

        question = row["question"]

        print("\n--------------------------------")
        print(f"Processing Question {i+1}")
        print(question)

        variables = extract_variables(question)

        print("Extracted variables:", variables)

        result = solve(variables)

        if result is None:
            print("Unsupported question type")
            continue

        answer, steps = result

        is_invalid = False
        if isinstance(answer, (int, float)) and answer < 0:
            is_invalid = True

        question_str = str(question).replace("\r", " ").replace("\n", " ").replace("₹", "rs")

        results.append({
            "idx": i + 1,
            "question": question_str,
            "steps": steps,
            "answer": answer,
            "is_invalid": is_invalid
        })

        # Render single HTML template for the image
        single_html_content = render_single_html(
            "templates/visual_template.html",
            {
                "question": question_str,
                "steps": steps,
                "answer": answer,
                "is_invalid": is_invalid,
                "image_b64": b64_img
            }
        )

        output_file = f"output/q_{i+1}.png"
        export_image(single_html_content, output_file)
        print(f"Generated image: {output_file}")


    html_content = render_report_html(results, b64_img)

    html_path = "output/report.html"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("\nHTML report generated:", html_path)

    pdf_path = "output/report.pdf"

    html_to_pdf(html_path, pdf_path)

    print("PDF report generated:", pdf_path)

    print("\nAutomation completed successfully!")


if __name__ == "__main__":
    main()