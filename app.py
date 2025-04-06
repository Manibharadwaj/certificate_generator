from flask import Flask, render_template, request, redirect, send_file, session, url_for
import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import zipfile

app = Flask(__name__)
app.secret_key = "fun-cert-session"
UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/output"
TEMPLATE_PATH = "certificate_template.jpg"
FONT_PATH = "Tinos-Regular.ttf"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        csv = request.files["csv"]
        template = request.files.get("template")

        csv_path = os.path.join(UPLOAD_FOLDER, "students.csv")
        csv.save(csv_path)

        if template:
            template_path = os.path.join(UPLOAD_FOLDER, "template.jpg")
            template.save(template_path)
        else:
            template_path = TEMPLATE_PATH

        # Save paths in session
        session['csv_path'] = csv_path
        session['template_path'] = template_path

        df = pd.read_csv(csv_path)
        names = df["names"].tolist()
        template_url = '/' + template_path

        return render_template("preview.html", names=names, template_url=template_url)
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    csv_path = session.get('csv_path')
    template_path = session.get('template_path')
    generate_certificates(csv_path, template_path)
    return render_template("success.html")

def generate_certificates(csv_path, template_path):
    df = pd.read_csv(csv_path)
    font = ImageFont.truetype(FONT_PATH, 60)
    for name in df['names']:
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)
        bbox = draw.textbbox((0, 0), name, font=font)
        x = (img.width - (bbox[2] - bbox[0])) / 2
        y = 600
        draw.text((x, y), name, font=font, fill="black")
        output_path = os.path.join(OUTPUT_FOLDER, f"{name.replace(' ', '_')}.jpg")
        img.save(output_path)

@app.route("/download")
def download_page():
    zip_path = os.path.join(OUTPUT_FOLDER, "certificates.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in os.listdir(OUTPUT_FOLDER):
            if file.endswith(".jpg"):
                zipf.write(os.path.join(OUTPUT_FOLDER, file), arcname=file)
    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
