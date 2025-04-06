# 🏆 Certificate Generator (Python)

This project automates the creation of personalized certificates for students using a template image and a list of names from a CSV file. Perfect for schools, events, workshops, or online courses.

---

## 📂 Project Structure

certificate_generator/ 
├── certificate_template.jpg
# Your certificate design
  ├── students.csv # List of student names 
  ├── generate_certificates.py # Python script for generation 
  ├── Tinos-Regular.ttf # (Optional) Font file used 
  ├── certificates/ # Output folder (auto-created)
  ├── requirements.txt # Required Python packages 
  └── run_generator.cmd # Easy one-click runner for Windows


---

## ✅ How It Works

1. Load student names from `students.csv`
2. Use `certificate_template.jpg` as the design
3. Render each name in the center of the certificate
4. Save each certificate as an image in the `certificates/` folder

---

## 🛠️ Setup Instructions

### 1. Install Dependencies

Make sure Python 3 is installed, then run:

pip install -r requirements.txt

### 2. Add Student Names

Edit `students.csv` with your student list:

names  example Alice Johnson Bob Smith Charlie Doe


> The header **must** be `names`.

### 3. Run the Script

For Windows (double-click):

run_generator.cmd


Or run manually:

python generate_certificates.py


---

## 🔤 Font Info

The script uses [Tinos](https://fonts.google.com/specimen/Tinos) – a free and open-source alternative to Times New Roman, downloaded automatically.

---

## ✨ Output

- All generated certificates will be saved inside the `certificates/` folder.
- File format: `Certificate_Student_Name.jpg`

---

## 📄 License

This project is open-source and free to use for any educational or event purpose.

---

## 🤝 Contributions

Got an idea? PRs and suggestions welcome! Let's automate the boring stuff together 😄
Once saved, just do:
