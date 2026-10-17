from flask import Flask, request
from Bio.Seq import Seq

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    length = 0
    gc = 0

    if request.method == "POST":

        dna = request.form["dna"].upper()
        dna = "".join(x for x in dna if x in "ATGC")

        if dna:
            seq = Seq(dna)
            length = len(seq)
            gc = (seq.count("G") + seq.count("C")) / length * 100

    return f"""
    <html>

    <head>
        <title>BioPython DNA Analyzer</title>

        <style>

            body {{
                margin: 0;
                font-family: Arial;
                background: linear-gradient(135deg, #0077b6, #90e0ef);
                text-align: center;
            }}

            .box {{
                width: 600px;
                margin: 50px auto;
                padding: 30px;
                background: white;
                border-radius: 20px;
                box-shadow: 0 8px 25px #555;
            }}

            h1 {{
                color: #0077b6;
                margin-bottom: 5px;
            }}

            .subtitle {{
                color: #666;
                margin-bottom: 25px;
            }}

            textarea {{
                width: 90%;
                height: 120px;
                padding: 12px;
                border: 2px solid #90e0ef;
                border-radius: 12px;
                font-size: 15px;
            }}

            button {{
                margin-top: 15px;
                padding: 12px 30px;
                background: #0077b6;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                cursor: pointer;
            }}

            button:hover {{
                background: #005f8a;
            }}

            .result {{
                margin-top: 25px;
                padding: 15px;
                background: #e8f8ff;
                border-radius: 15px;
            }}

            .result h3 {{
                margin: 10px;
                color: #005f8a;
            }}

            .footer {{
                margin-top: 20px;
                color: #777;
                font-size: 13px;
            }}

        </style>
    </head>

    <body>

        <div class="box">

            <h1>🧬 BioPython DNA Analyzer</h1>

            <div class="subtitle">
                DNA Sequence Length & GC Content Calculator
            </div>

            <form method="post">

                <textarea name="dna"
                placeholder="Paste your DNA sequence here..."></textarea>

                <br>

                <button>🔬 Analyze DNA</button>

            </form>

            <div class="result">

                <h3>📏 Sequence Length: {length} bp</h3>

                <h3>🧪 GC Content: {gc:.2f}%</h3>

            </div>

            <div class="footer">
                Powered by Python & BioPython
            </div>

        </div>

    </body>

    </html>
    """

app.run()
