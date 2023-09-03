import tkinter as tk
from tkinter import ttk
import requests
import tkinter as tk
from tkinter import ttk
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Function to currency
def convert_currency():
    from_currency = from_currency_combobox.get().strip().upper()
    to_currency = to_currency_combobox.get().strip().upper()
    amount = float(entry_amount.get().strip())

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {
        "to_currency": to_currency,
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency
    }

    headers = {
        "X-RapidAPI-Key": "API_KEY",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    converted_amount = amount * exchange_rate
    result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


def show_exchange_rate_graph():
    from_currency = from_currency_combobox.get().strip().upper()
    to_currency = to_currency_combobox.get().strip().upper()

    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {
        "from_symbol": from_currency,
        "function": "FX_MONTHLY",
        "to_symbol": to_currency,
        "outputsize": "full",
        "datatype": "json"
    }

    headers = {
        "X-RapidAPI-Key": "API_KEY",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Extracting data
    time_series = data['Time Series FX (Monthly)']
    months = list(time_series.keys())
    months = sorted(months, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))
    exchange_rates = [float(time_series[month]['4. close']) for month in months]

    # Date formatting
    formatted_dates = [datetime.strptime(month, "%Y-%m-%d").strftime("%b %Y") for month in months]

    # Display dates
    step = max(1, len(formatted_dates) // 10)  
    x_ticks = formatted_dates[::step]

    # Create a line chart for monthly data
    plt.figure(figsize=(10, 6))
    plt.plot(formatted_dates, exchange_rates, marker='o', linestyle='-')
    plt.ylabel(f'Exchange Rate ({from_currency}/{to_currency})')
    plt.title(f'Monthly Exchange Rates ({from_currency}/{to_currency})')
    plt.xticks(x_ticks, rotation=45)
    plt.tight_layout()
    #Display char
    plt.show()

#GUI 
window = tk.Tk()
window.title("Currency Converter")

# Labels
label_from_currency = ttk.Label(window, text="From currency:")
label_to_currency = ttk.Label(window, text="To currency:")
label_amount = ttk.Label(window, text="Amount:")

# Different currencies.
currencies = [
    "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD",
    "NOK", "SGD", "HKD", "KRW", "TRY", "MXN", "INR", "RUB", "BRL", "ZAR",
    "AED", "SAR", "THB", "DKK", "MYR", "IDR", "PHP", "HUF", "PLN", "CZK",
    "ILS", "CLP", "ARS", "EGP", "KWD", "QAR", "OMR", "VND", "UAH", "NGN",
    "KES", "COP", "PEN", "TWD", "BDT", "PKR", "LKR", "RON", "HRK", "BGN",
    "AED", "SAR", "THB", "DKK", "MYR", "IDR", "PHP", "HUF", "PLN", "CZK",
    "ILS", "CLP", "ARS", "EGP", "KWD", "QAR", "OMR", "VND", "UAH", "NGN",
    "KES", "COP", "PEN", "TWD", "BDT", "PKR", "LKR", "RON", "HRK", "BGN",
    "ISK", "RSD", "RON", "HRK", "BGN", "ISK", "RSD", "TND", "DZD", "KZT",
    "AED", "SAR", "THB", "DKK", "MYR", "IDR", "PHP", "HUF", "PLN", "CZK",
    "ILS", "CLP", "ARS", "EGP", "KWD", "QAR", "OMR", "VND", "UAH", "NGN",
    "KES", "COP", "PEN", "TWD", "BDT", "PKR", "LKR", "RON", "HRK", "BGN",
    "ISK", "RSD", "TND", "DZD", "KZT", "TRY", "MXN", "INR", "RUB", "BRL",
    "ZAR", "CNY", "JPY", "KRW", "CAD", "AUD", "NZD", "SEK", "NOK", "SGD",
    "HKD", "ILS", "CLP", "ARS", "EGP", "QAR", "OMR", "VND", "NGN", "COP",
    "MYR", "IDR", "THB", "HUF", "PLN", "CZK", "UAH", "TWD", "PKR", "LKR"
]
#Currencies Input
from_currency_combobox = ttk.Combobox(window, values=currencies)
to_currency_combobox = ttk.Combobox(window, values=currencies)

#widgets
entry_amount = ttk.Entry(window)
convert_button = ttk.Button(window, text="Convert", command=convert_currency)
result_label = ttk.Label(window, text="Result will be shown here")
label_from_currency.grid(row=0, column=0, padx=10, pady=10)
from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)
label_to_currency.grid(row=1, column=0, padx=10, pady=10)
to_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
label_amount.grid(row=2, column=0, padx=10, pady=10)
entry_amount.grid(row=2, column=1, padx=10, pady=10)
convert_button.grid(row=3, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, columnspan=2, padx=10, pady=10)
show_graph_button = ttk.Button(window, text="Show Exchange Rate Graph", command=show_exchange_rate_graph)
show_graph_button.grid(row=5, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()