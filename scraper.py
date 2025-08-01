import requests
from bs4 import BeautifulSoup

def fetch_case_data(case_type, case_number, year):
    try:
       
        payload = {
            "__VIEWSTATE": "...",
            "case_type": case_type,
            "case_number": case_number,
            "filing_year": year
        }

        response = requests.post("Your url", data=payload)
        soup = BeautifulSoup(response.text, "html.parser")

        
        parties = soup.find("span", id="parties").text.strip()
        filing_date = soup.find("span", id="filing_date").text.strip()
        next_hearing = soup.find("span", id="next_hearing").text.strip()
        pdf_link = soup.find("a", href=True)["href"]

        return {
            "parties": parties,
            "filing_date": filing_date,
            "next_hearing": next_hearing,
            "pdf_link": pdf_link
        }, response.text

    except Exception as e:
        return {"error": f"Failed to fetch case data: {str(e)}"}, ""
