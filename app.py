import streamlit as st

st.title("Budżet domowy – prosty kalkulator")

# Wprowadzenie miesięcznego dochodu
dochód = st.number_input("Podaj swój miesięczny dochód netto (zł):", min_value=0, step=100)

# Domyślne proporcje budżetu (procenty)
proporcje = {
    "Wydatki stałe (czynsz, rachunki, transport)": 0.4,
    "Oszczędności / inwestycje": 0.2,
    "Jedzenie": 0.15,
    "Rozrywka / hobby": 0.1,
    "Edukacja / rozwój": 0.05,
    "Ubrania / inne zmienne": 0.1
}

if dochód > 0:
    st.subheader("Proponowany podział budżetu:")
    for kategoria, procent in proporcje.items():
        kwota = round(dochód * procent, 2)
        st.write(f"{kategoria}: {kwota} zł")

    # Możliwość pobrania danych jako plik
    if st.button("Pobierz podsumowanie jako plik tekstowy"):
        with open("budżet.txt", "w") as f:
            f.write(f"Dochód netto: {dochód} zł\n\n")
            f.write("Podział budżetu:\n")
            for kategoria, procent in proporcje.items():
                kwota = round(dochód * procent, 2)
                f.write(f"{kategoria}: {kwota} zł\n")
        with open("budżet.txt", "rb") as f:
            st.download_button(label="Pobierz plik", data=f, file_name="budżet.txt")

else:
    st.info("Wprowadź dochód, aby zobaczyć podział budżetu.")

