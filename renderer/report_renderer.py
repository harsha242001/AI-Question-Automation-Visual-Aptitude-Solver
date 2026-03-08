import re
from jinja2 import Template

def process_text(text):
    text = re.sub(r'\bCP\b', '<span class="tag cp">CP</span>', text)
    text = re.sub(r'\bSP\b', '<span class="tag sp">SP</span>', text)
    text = re.sub(r'\bMP\b', '<span class="tag mp">MP</span>', text)
    text = re.sub(r'\bP\b', '<span class="tag p">P</span>', text)
    text = re.sub(r'\bL\b', '<span class="tag l">L</span>', text)
    text = re.sub(r'\bSP1\b', '<span class="tag sp">SP1</span>', text)
    text = re.sub(r'\bSP2\b', '<span class="tag sp">SP2</span>', text)
    text = re.sub(r'\b[x]\b', '<span class="tag x">x</span>', text)
    text = re.sub(r'(\d+(?:\.\d+)?)x', r"\1<span class='tag x'>x</span>", text, flags=re.IGNORECASE)
    text = re.sub(r'\brs\b', '₹', text)
    return text

def render_html(results, image_b64):
    for r in results:
        r["steps"] = [process_text(str(s)) for s in r.get("steps", [])]
        if not r.get("is_invalid", False):
            r["answer_str"] = process_text("rs " + str(r.get("answer", "")))
        else:
            r["answer_str"] = "Invalid Problem Layout"

    template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            background: #f2f2f2;
            font-family: Calibri, Arial, sans-serif;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .main-wrapper {
            background: #FFF;
            max-width: 900px;
            margin: 20px auto 60px auto;
            border: 3px solid #000;
            padding: 10px 10px 30px 10px;
            position: relative;
            box-sizing: border-box;
            page-break-inside: avoid;
        }
        .header-title-box {
            margin: 5px auto;
            width: fit-content;
            border: 2px solid #000;
            padding: 8px 30px;
        }
        .header-title-box h1 {
            color: #4B78BA;
            font-size: 26px;
            font-weight: bold;
            margin: 0;
            text-align: center;
        }
        .divider-group {
            margin: 20px 0;
        }
        .divider-thick {
            border-top: 3px solid #000;
            margin-bottom: 5px;
        }
        .divider-thin {
            border-top: 1px solid #000;
        }
        .content-grid {
            overflow: hidden;
            padding: 0 10px;
        }
        .left-col {
            float: left;
            width: 56%;
            font-size: 20px;
            font-weight: 600;
            color: #444;
        }
        .right-col {
            float: right;
            width: 38%;
            max-width: 320px;
        }
        .right-col > * {
            margin-bottom: 12px;
        }
        .question-text {
            font-size: 19px;
            color: #000;
            margin-bottom: 25px;
            font-weight: normal;
            border-bottom: 1px dashed #ccc;
            padding-bottom: 15px;
        }
        .step-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .step-list li {
            margin-bottom: 25px;
            position: relative;
            padding-left: 20px;
        }
        .step-list li::before {
            content: "•";
            color: #D64654;
            position: absolute;
            left: 0;
            top: 0;
            font-size: 26px;
            line-height: .7;
        }
        .cross-multiply {
            margin-top: 40px;
            margin-left: -5px;
        }
        .cross-label {
            text-decoration: underline;
            font-weight: bold;
            font-size: 20px;
            color: #000;
            margin-bottom: 15px;
        }
        .answer-row {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-left: 20px;
        }
        .ans-arrow {
            color: #888;
            font-weight: normal;
            letter-spacing: -2px;
            font-size: 20px;
        }
        .ans-box {
            background: #2DAB80;
            color: #FFF;
            border-radius: 4px;
            padding: 8px 18px;
            font-size: 24px;
            font-weight: bold;
        }
        .ans-x {
            display: inline-block;
            background: #5CA1DB;
            color: #FFF;
            border-radius: 4px;
            padding: 2px 8px;
            font-weight: bold;
        }
        .books-img {
            width: 100%;
            border-radius: 6px;
            object-fit: contain;
            background: #F4D3A1;
        }
        .legend-black {
            background: #000;
            border-radius: 4px;
            padding: 8px 12px;
            color: #FFF;
            font-size: 21px;
            font-weight: bold;
            font-family: Arial, sans-serif;
            margin-bottom: 5px;
        }
        .leg-row {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            border-bottom: 2px dotted #777;
            padding: 5px 0;
            gap: 10px;
        }
        .leg-row:last-child {
            border-bottom: none;
            justify-content: center;
            gap: 15px;
        }
        .pl-wrapper {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .formula-box {
            border: 4px solid #000;
            border-radius: 4px;
            padding: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            font-size: 20px;
            font-weight: bold;
            color: #000;
        }
        .f-frac {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .f-top { padding-bottom: 5px; }
        .f-bot { border-top: 2px solid #000; padding-top: 3px; width: 100%; text-align: center; }
        .tag {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 800;
            margin: 0 4px;
        }
        .tag.mp { background: #FFF; color: #333; border: 1px solid #999; }
        .tag.cp { background: #f7ced3; color: #444; }
        .tag.sp { background: #abdef6; color: #444; }
        .tag.d { background: #e9e0cb; color: #444; }
        .tag.p { background: linear-gradient(135deg, #f09ea1, #f4b8c7); color: #c94b63; }
        .tag.l { background: linear-gradient(135deg, #fcce9b, #eed397); color: #b96937; }
        .tag.x { background: #5CA1DB; color: #FFF; }
    </style>
</head>
<body>

    {% for r in results %}
    <div class="main-wrapper">
        <div class="header-title-box">
            <h1>1.1.b - Step wise visual explanation (Desired Output)</h1>
        </div>

        <div class="divider-group">
            <div class="divider-thick"></div>
            <div class="divider-thin"></div>
        </div>

        <div class="content-grid">
            <div class="left-col">
                <div class="question-text">
                    <strong>Q{{ r.idx }}.</strong> {{ r.question }}
                </div>
                
                <ul class="step-list">
                    <li>Let the original <span class="tag cp">CP</span> be = ₹ <span class="tag x">x</span></li>
                    {% for step in r.steps %}
                    <li>{{ step }}</li>
                    {% endfor %}
                </ul>

                <div class="cross-multiply">
                    <div class="cross-label">Cross-multiply:</div>
                    <div class="answer-row">
                        <span class="ans-arrow">---&#10140;</span>
                        <span class="ans-x">x</span> =
                        {% if r.is_invalid %}
                        <span class="ans-box" style="background:#E74C3C;">Invalid Problem Layout</span>
                        {% else %}
                        <span class="ans-box">{{ r.answer_str }}</span>
                        {% endif %}
                    </div>
                </div>
            </div>

            <div class="right-col">
                <img src="data:image/png;base64,{{ image_b64 }}" class="books-img">

                <div class="legend-black">
                    <div class="leg-row">
                        <span>Marked Price =</span> <span class="tag mp">MP</span>
                    </div>
                    <div class="leg-row">
                        <span>Cost Price =</span> <span class="tag cp">CP</span>
                    </div>
                    <div class="leg-row">
                        <span>Selling Price =</span> <span class="tag sp">SP</span>
                    </div>
                    <div class="leg-row">
                        <span>Discount =</span> <span class="tag d">D</span>
                    </div>
                    <div class="leg-row" style="padding-top:10px;">
                        <div class="pl-wrapper"><span>Profit =</span><span class="tag p">P</span></div>
                        <div class="pl-wrapper"><span style="margin-left:5px;">Loss =</span><span class="tag l">L</span></div>
                    </div>
                </div>

                <div class="formula-box">
                    <span class="tag p">P</span> =
                    <div class="f-frac">
                        <div class="f-top"><span class="tag sp">SP</span> - <span class="tag cp">CP</span></div>
                        <div class="f-bot"><span class="tag cp">CP</span></div>
                    </div>
                    &times; 100
                </div>
            </div>
        </div>
    </div>
    {% endfor %}

</body>
</html>
    """

    return Template(template).render(results=results, image_b64=image_b64)