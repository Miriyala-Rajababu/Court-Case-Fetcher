Here is the complete `README.md` content in **one plain text block** — ready to copy and paste directly into your project:

---

```
# eCourts Case Scraper 🏛️

This project is a simple Python script that scrapes court case information from the eCourts Services website (https://districts.ecourts.gov.in/). It allows you to input a case type, number, and year, then fetches and stores the raw HTML response into a local SQLite database.

## 📁 Project Structure

.
├── main.py           # Script to run the scraper  
├── database.py       # Database setup and logging functions  
├── requirements.txt  # List of Python dependencies  
├── .env.example      # Sample environment variables  
├── README.md         # This file  
├── LICENSE           # MIT or Apache-2.0 license  

## ⚙️ Setup Instructions

1. **Clone the Repository**
```

git clone [https://github.com/Miriyala-Rajababu/Court-Case-Fetcher.git]
cd ecourts-case-scraper

```

2. **Create Virtual Environment (optional but recommended)**
```

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

```

3. **Install Dependencies**
```

pip install -r requirements.txt

```

4. **Set Up Environment Variables**

Create a `.env` file (or use the provided `.env.example`) and add:
```

COURT\_URL=[https://districts.ecourts.gov.in/faridabad](https://districts.ecourts.gov.in/faridabad)
CASE\_TYPE=Civil
CASE\_NUMBER=123
YEAR=2022

```

## ▶️ Running the Script

```

python main.py

```

This will fetch court case data and store it in `queries.db`.

## 🧠 CAPTCHA Strategy

The eCourts site uses a dynamic CAPTCHA. In this proof-of-concept:
- CAPTCHA is **skipped**
- Or you can implement manual input / automation (e.g., using OCR like `pytesseract`)

## 🏛️ Court Selected

Faridabad District Court  
URL: https://districts.ecourts.gov.in/faridabad  
Reason: Public access and predictable HTML structure for testing

## 🧪 Sample Inputs

- Case Type: Civil  
- Case Number: 123  
- Year: 2022  
- Court URL: https://districts.ecourts.gov.in/faridabad

## 🧾 Output Format

The fetched HTML is stored in the SQLite database:

- Database: `queries.db`  
- Table: `logs`  
- Columns: case_type, case_number, year, html, timestamp  

## 📦 Sample Output

```

{
"id": 1,
"case\_type": "Civil",
"case\_number": 123,
"year": 2022,
"html": "<!DOCTYPE html> ...",
"timestamp": "2025-08-01 10:15:00"
}

```

## 🪪 License

This project is licensed under the MIT or Apache-2.0 License. See the LICENSE file for details.

## ✅ Optional Features

- Dockerfile for containerization  
- Logging with timestamps  
- Pagination handling  
- GitHub Actions workflow  
- Basic unit tests  

## 🙌 Contributions

Pull requests are welcome! Open an issue first to discuss what you want to change.
```

---

Let me know if you want this saved to a `.md` file or need it customized for deployment or GitHub Pages.
