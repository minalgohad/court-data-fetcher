import time

def fetch_case_data(case_type, case_number, year):
    # Simulated data fetch
    print("✅ Fetching case details (Mock)...")
    time.sleep(1)  # simulate delay

    return {
        'parties': f'Petitioner vs Respondent ({case_type} {case_number}/{year})',
        'filing_date': '15-Apr-2022',
        'next_hearing': '10-Aug-2025',
        'pdf_link': 'https://example.com/sample_judgement.pdf'
    }
