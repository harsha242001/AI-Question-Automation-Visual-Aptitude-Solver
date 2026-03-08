# 🧠 AI Question Automation – Visual Aptitude Solver

AI Question Automation is a **Python-based automation pipeline** that converts aptitude questions into **step-by-step visual explanations**.

The system reads questions from an Excel dataset, extracts mathematical entities from the text, solves the problem using rule-based logic, and generates:

• **PNG explanation cards**
• **HTML solution reports**
• **PDF printable worksheets**

This project demonstrates how automation can convert **unstructured text → structured reasoning → visual educational content**.

---

# 🚀 Example Output

For the question:

```
A trader marks an article 40% above its cost price. 
He allows a 10% discount and still earns ₹36 profit.
```

The system automatically generates:

```
Cost Price = ₹138.46
```

With full visual step-by-step explanation cards.

Outputs generated:

```
output/q_1.png
output/report.html
output/report.pdf
```

---

# 🏗 System Architecture

The project follows a **modular processing pipeline**.

```
          Excel Dataset
               │
               ▼
        Text Parsing Engine
               │
               ▼
        Variable Extraction
               │
               ▼
        Mathematical Solver
               │
               ▼
         HTML Template Engine
               │
        ┌──────┴────────┐
        ▼               ▼
   PNG Image Cards   HTML Report
                           │
                           ▼
                        PDF Export
```

Each module performs a **single responsibility**, making the system easy to extend.

---

# 🔄 Processing Pipeline

## 1️⃣ Dataset Input

Questions are stored in an Excel dataset.

```
data/questions.xlsx
```

Example question:

```
A trader marks an article 40% above its cost price and allows a 10% discount.
```

Dataset is loaded using **Pandas**.

---

## 2️⃣ Parsing (Text → Variables)

The parser extracts numerical and logical entities from the question.

Example extraction:

```
Input Question:
A trader marks an article 40% above its cost price and earns ₹36 profit.

Extracted Variables:
{
  markup_percent: 40,
  discount_percent: 10,
  profit_amount: 36
}
```

Extraction is implemented using **regular expressions**.

Module:

```
parser/extractor.py
```

---

## 3️⃣ Mathematical Solver

The solver identifies the question pattern and applies the correct formula.

Example formula:

```
MP = (1 + markup/100) × CP
SP = MP × (1 − discount/100)

Profit = SP − CP
```

Example computed result:

```
CP = 138.46
```

Module:

```
solver/math_solver.py
```

---

## 4️⃣ Step Explanation Generator

The solver also produces explanation steps.

Example:

```
Let CP = x
MP = (1 + 40/100)x
SP = MP × (1 − 10/100)
1.26x − x = 36
x = 138.46
```

These steps are inserted into the visual template.

---

## 5️⃣ HTML Rendering

Solutions are rendered using **Jinja2 templates**.

Template file:

```
templates/visual_template.html
```

This controls:

• page layout
• styling
• legend
• formula display
• answer formatting

Module:

```
renderer/html_renderer.py
```

---

## 6️⃣ Image Generation

Each rendered HTML solution is captured as a PNG image using a headless browser.

Process:

```
HTML → Playwright → Screenshot → PNG
```

Output example:

```
output/q_1.png
output/q_2.png
```

Module:

```
renderer/image_exporter.py
```

---

## 7️⃣ HTML Report Generation

All solved questions are combined into a single webpage.

```
output/report.html
```

Module:

```
renderer/report_renderer.py
```

---

## 8️⃣ PDF Generation

The HTML report is converted into a printable PDF worksheet.

```
output/report.pdf
```

Module:

```
exporter/pdf_exporter.py
```

---

# 📂 Project File Structure

```
C:\ai-question-automation - chatgpt\
│   main.py                      # Core execution loop bridging the modules
│   README.md                    # Project documentation
│   requirements.txt             # Python dependencies
│
├── assets/
│       books.png                # Asset image used in visual templates
│
├── data/
│       questions.xlsx           # Input dataset
│       sample.json              # Sample exported dataset
│
├── exporter/
│       pdf_exporter.py          # HTML → PDF conversion
│
├── output/                      # Generated files
│       q_1.png...q_6.png        # Individual solution cards
│       report.html              # Full HTML report
│       report.pdf               # Printable PDF worksheet
│
├── parser/
│       extractor.py             # Regex-based entity extraction
│
├── renderer/
│       html_renderer.py         # Template rendering
│       image_exporter.py        # PNG screenshot generation
│       report_renderer.py       # HTML report generation
│
├── solver/
│       math_solver.py           # Mathematical solving engine
│
└── templates/
        visual_template.html     # Main HTML layout template
```

---

# ▶️ Running the Project

### Install dependencies

```
pip install -r requirements.txt
```

### Run the automation

```
python main.py
```

Generated outputs will appear in:

```
output/
```

---

# 📊 Generated Outputs

| Output        | Description                          |
| ------------- | ------------------------------------ |
| PNG Cards     | Visual explanation for each question |
| HTML Report   | All questions with solutions         |
| PDF Worksheet | Printable formatted document         |

---

# 🧩 Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core programming language |
| Pandas     | Dataset processing        |
| Regex      | Text extraction           |
| Jinja2     | HTML templating           |
| Playwright | PNG generation            |
| pdfkit     | PDF export                |

---

# 🔮 Future Improvements

Possible extensions:

• Support additional aptitude topics
• NLP-based question understanding
• Web interface for question input
• Automatic worksheet generation
• Batch dataset processing

---

# 🎯 Key Takeaway

This project shows how an automation system can transform:

```
Raw Question Text
        ↓
Mathematical Reasoning
        ↓
Visual Educational Content
```

Such systems are used in **AI tutoring platforms, educational content generators, and automated exam preparation tools**.

---

# 👨‍💻 Author

Harsha Vardhan
Senior Software Engineer
