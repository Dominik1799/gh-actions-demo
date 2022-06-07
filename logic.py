from datetime import date

def get_today():
    today = date.today().strftime("%d/%m/%Y")
    return today