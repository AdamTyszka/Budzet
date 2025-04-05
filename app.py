import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Budżet domowy", layout="centered")
st.title("💰 Budżet domowy – Twój osobisty kalkulator")

# Wprowadzenie miesięcznego dochodu
dochód = st.number_input("Podaj swój miesięczny dochód netto (zł):", min_value=0, step=100)

# Domyślne proporcje budżetu
proporcje = {
    "Wydatki stałe": 0.4,
    "Jedzenie": 0.15,
    "Rozrywka / hobby": 0.1,
    "Edukacja / rozwój": 0.05,
    "Ubrania / zmienne": 0.1,
    "Niezapowiedziane wydatki": 0.05,
    "Oszczędności": 0.1
}

# Dobre rady – losowane przy każdym odświeżeniu
rady = [
    "Oszczędzaj na początku miesiąca, nie na końcu.",
    "Budżet to Twoje narzędzie wolności, nie ograniczenia.",
    "Sprawdzaj podsumowanie wydatków raz w tygodniu.",
    "10% oszczędności to minimum, 20% to cel!",
    "Unikaj zakupów pod wpływem emocji.",
    "Zapisuj wydatki — świadomość to podstawa.",
]

if dochód > 0:
    st.subheader("📊 Proponowany podział budżetu:")
    kwoty = {}
    suma_wydatków = 0

    for kategoria, procent in proporcje.items():
        kwota = round(dochód * procent, 2)
        kwoty[kategoria] = kwota
        suma_wydatków += kwota
        udzial = round(kwota / dochód * 100, 1)
        st.write(f"**{kategoria}**: {kwota} zł ({udzial}%)")

    zostaje = round(dochód - suma_wydatków, 2)
    if zostaje > 0:
        st.success(f"Zostaje Ci: {zostaje} zł – możesz je odłożyć lub zainwestować.")
    elif
