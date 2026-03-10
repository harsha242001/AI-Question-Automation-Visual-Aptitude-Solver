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
        if r.get("tpl"):
            for k, v in r["tpl"].items():
                if isinstance(v, str):
                    r["tpl"][k] = process_text(v)
        
        if not r.get("is_invalid", False):
            r["answer_str"] = process_text("rs " + str(r.get("answer", "")))
        else:
            r["answer_str"] = "Invalid Answer"

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
            text-align: right;
            border-bottom: 2px dotted #777;
            padding: 5px 0;
            white-space: nowrap;
        }
        .leg-row > * {
            vertical-align: middle;
            display: inline-block;
        }
        .leg-row:last-child {
            border-bottom: none;
            text-align: center;
        }
        .pl-wrapper {
            display: inline-block;
            vertical-align: middle;
            margin: 0 5px;
        }
        .formula-box {
            border: 4px solid #000;
            border-radius: 4px;
            padding: 15px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #000;
            white-space: nowrap;
        }
        .formula-box > * {
            display: inline-block;
            vertical-align: middle;
            margin: 0 3px;
        }
        .f-frac {
            display: inline-block;
            vertical-align: middle;
            text-align: center;
        }
        .f-top { padding-bottom: 5px; display: block; }
        .f-bot { border-top: 2px solid #000; padding-top: 3px; width: 100%; text-align: center; display: block; }
        .tag {
            display: inline-block;
            vertical-align: middle;
            text-align: center;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 800;
            margin: 0 4px;
        }
        .tag.mp { background: #FFF; color: #333; border: 1px solid #999; }
        .tag.cp { background: #f7ced3; color: #444; }
        .tag.sp { background: #abdef6; color: #444; }
        .tag.d { background: #e9e0cb; color: #444; }
        .tag.p { background: -webkit-linear-gradient(top, #ff5e95, #ffb88e); background: linear-gradient(to bottom, #ff5e95, #ffb88e); color: #4a1525; }
        .tag.l { background: -webkit-linear-gradient(-45deg, #fcce9b, #eed397); background: linear-gradient(135deg, #fcce9b, #eed397); color: #b96937; }
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
            <div class="left-col" style="font-family: Calibri, Arial, sans-serif;">
                <div style="margin-bottom: 25px; font-size: 22px; font-weight: bold; position: relative;">
                    <span style="color: #D64654; font-size: 30px; margin-right: 10px; line-height: 1; margin-left: 20px; vertical-align: middle;">•</span> 
                    <span style="vertical-align: middle;">{{ r.tpl.top_line }}</span>
                </div>
                
                <div style="margin-bottom: 20px; font-size: 22px; font-weight: bold; position: relative;">
                    <span style="color: #D64654; font-size: 30px; margin-right: 10px; line-height: 1; margin-left: 20px; vertical-align: middle;">•</span> 
                    <span style="vertical-align: middle;">Given/New :</span>
                </div>

                <div style="position: relative; margin-left: -5px; font-size: 19px; margin-top: -10px;">
                    <!-- The Main 4-column Box -->
                    <div style="border: 2px solid #ccc; border-radius: 8px; display: table; width: 100%; text-align: center; background: #fff; z-index: 2; position: relative; padding: 0; box-sizing: border-box; table-layout: fixed;">
                        <!-- Col 1 -->
                        <div style="display: table-cell; vertical-align: middle; border-right: 2px dashed #999; padding: 10px 5px; width: 23%;">
                            <div style="margin-bottom: 8px; font-weight: bold; font-size: 18px;">{{ r.tpl.b1_top }}</div>
                            <div style="font-weight: bold; font-size: 18px;">{{ r.tpl.b1_bot }}</div>
                        </div>
                        <!-- Col 2 -->
                        <div style="display: table-cell; vertical-align: middle; border-right: 2px dashed #999; padding: 10px 5px; width: 23%;">
                            <div style="margin-bottom: 8px; font-weight: bold;">{{ r.tpl.b2_top }}</div>
                            <div style="font-weight: bold; font-size: 18px;">{{ r.tpl.b2_bot }}</div>
                        </div>
                        <!-- Col 3 -->
                        <div style="display: table-cell; vertical-align: middle; border-right: 2px dashed #999; padding: 10px 5px; width: 27%;">
                            <div style="margin-bottom: 8px; font-weight: bold;">{{ r.tpl.b3_top }}</div>
                            <div style="font-weight: bold; font-size: 18px;">{{ r.tpl.b3_bot }}</div>
                        </div>
                        <!-- Col 4 -->
                        <div style="display: table-cell; vertical-align: middle; padding: 8px 5px; width: 27%;">
                            <div style="display: inline-block; vertical-align: middle; margin-right: 5px;">
                                <div style="margin-bottom: 8px; font-weight: bold;">{{ r.tpl.b4_top }}</div>
                                <div style="font-weight: bold; font-size: 17px;">{{ r.tpl.b4_bot }}</div>
                            </div>
                            {% if r.tpl.b4_frac_num %}
                            <div style="display: inline-block; vertical-align: bottom; font-weight: bold; font-size: 20px; line-height: 1.1; margin-bottom: -5px;">
                                <div style="border-bottom: 2px solid #000; padding: 0 4px; text-align: center;">{{ r.tpl.b4_frac_num }}</div>
                                <div style="padding: 0 4px;">{{ r.tpl.b4_frac_den }}</div>
                            </div>
                            {% endif %}
                        </div>
                    </div>
                    
                    <!-- Arrow connection for equation -->
                    {% if r.tpl.form_top %}
                    <div style="position: relative; margin-top: 50px; margin-bottom: 25px; width: 100%; text-align: center;">

                        <!-- L-shaped dashed line using webkit-safe CSS (no calc) -->
                        <div style="position: absolute; right: 13.5%; bottom: 50%; height: 75px; border-right: 2px dashed #888; z-index: 1;"></div>
                        <div style="position: absolute; left: 50%; right: 13.5%; top: 50%; border-top: 2px dashed #888; z-index: 1;"></div>

                        <!-- Formula Box -->
                        <div style="display: inline-block; background:#f0f3f6; border:1px solid #ccc; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.15); padding:10px 20px; font-size:20px; position: relative; z-index: 2; white-space:nowrap; text-align: center;">

                            <div style="padding-bottom:5px; font-weight:bold; width:100%; {% if r.tpl.form_bot %}border-bottom:2px solid #000;{% endif %}">
                                <span>{{ r.tpl.form_top }}</span>
                            </div>

                            {% if r.tpl.form_bot %}
                            <div style="padding-top:5px; font-weight:bold; width: 100%;">
                                <span>{{ r.tpl.form_bot }}</span>
                            </div>
                            {% endif %}
                            
                            <!-- Arrowhead pointing left, attached to the exact right edge of the formula box -->
                            <div style="position: absolute; right: -8px; top: 50%; margin-top: -6px; width: 0; height: 0; border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-right: 8px solid #888;"></div>
                        </div>

                    </div>
                    {% endif %}
                </div>
                
                <div class="cross-multiply">
                    <div class="cross-label">Cross-multiply:</div>
                    
                    <div style="margin-bottom: 20px; font-size: 20px; margin-left: 20px;">
                        <span class="ans-arrow" style="vertical-align: middle; display: inline-block; width: 35px;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="12" viewBox="0 0 30 12" style="vertical-align: middle;">
                                <path d="M0,6 L28,6 M22,2 L28,6 L22,10" fill="none" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </span>
                        <span style="font-weight: normal; color: #444; vertical-align: middle; display: inline-block;">{{ r.tpl.cross }}</span>
                    </div>
                    
                    <div style="font-size: 20px; margin-left: 20px; margin-bottom: 20px;">
                        <span class="ans-arrow" style="vertical-align: middle; display: inline-block; width: 35px;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="12" viewBox="0 0 30 12" style="vertical-align: middle;">
                                <path d="M0,6 L28,6 M22,2 L28,6 L22,10" fill="none" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </span>
                        <span class="ans-x" style="font-size: 20px; border-radius: 4px; padding: 2px 7px; vertical-align: middle; display: inline-block;">x</span> 
                        <span style="font-weight: bold; font-size: 22px; vertical-align: middle; display: inline-block;">=</span>
                        
                        {% if r.tpl.x_den %}
                        <div style="display: inline-block; text-align: center; font-weight: normal; font-size: 22px; line-height: 1.1; margin: 0 5px; color: #444; vertical-align: middle;">
                            <div style="border-bottom: 2px solid #000; padding: 0 4px;">{{ r.tpl.x_num }}</div>
                            <div style="padding: 0 4px;">{{ r.tpl.x_den }}</div>
                        </div>
                        <span style="font-weight: bold; font-size: 22px; vertical-align: middle; display: inline-block;">=</span>
                        {% else %}
                        <div style="margin: 0 5px; font-weight: bold; font-size: 22px; vertical-align: middle; display: inline-block;">{{ r.tpl.x_num }}</div>
                        <span style="font-weight: bold; font-size: 22px; vertical-align: middle; display: inline-block;">=</span>
                        {% endif %}
                        
                        <span class="ans-box" style="margin-left: 5px; border-radius: 6px; padding: 8px 16px; vertical-align: middle; display: inline-block; {% if r.is_invalid %}background: #e74c3c;{% endif %}">
                            {% if r.is_invalid %}
                            Invalid Answer
                            {% else %}
                            {{ r.tpl.x_ans }}
                            {% endif %}
                        </span>
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

                <div class="formula-box" style="padding: 15px 5px;">
                    <table style="margin: 0 auto; border-spacing: 0; padding: 0;">
                        <tr>
                            <td style="vertical-align: middle; padding: 0 5px; font-weight: bold; font-size: 22px;">
                                <span class="tag p">P</span> =
                            </td>
                            <td style="vertical-align: middle; padding: 0 5px; text-align: center;">
                                <div style="padding-bottom: 5px;"><span class="tag sp">SP</span> - <span class="tag cp">CP</span></div>
                                <div style="border-top: 2px solid #000; padding-top: 5px;"><span class="tag cp">CP</span></div>
                            </td>
                            <td style="vertical-align: middle; padding: 0 5px; font-weight: bold; font-size: 22px;">
                                &times; 100
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </div>
    {% endfor %}

</body>
</html>
    """

    return Template(template).render(results=results, image_b64=image_b64)