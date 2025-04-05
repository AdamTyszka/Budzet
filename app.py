import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Budżet domowy", layout="centered")
st.title("💰 Budżet domowy – Twój osobisty kalkulator")

# Wprowadzenie miesięcznego dochodu
dochód = st.number_input("Podaj swój miesięczny dochód netto (zł):", min_value=0, step=100)

# Domyślne proporcje budżetu (procenty)
proporcje = {
    "Wydatki stałe (czynsz, rachunki, transport)": 0.4,
    "Jedzenie": 0.15,
    "Rozrywka / hobby": 0.1,
    "Edukacja / rozwój": 0.05,
    "Ubrania / inne zmienne": 0.1,
    "Niezapowiedziane wydatki": 0.05,
    "Oszczędności": 0.1
}

# Dobre rady – losowane za każdym razem
rady = [
    "Nie wydawaj więcej niż zarabiasz – nawet mała nadwyżka robi różnicę.",
    "Płać najpierw sobie – oszczędzaj na początku miesiąca, nie na końcu.",
    "Zapisuj każdy wydatek – świadomość to pierwszy krok do kontroli.",
    "Oszczędzaj minimum 10% dochodu – to zdrowy nawyk!",
    "Unikaj długów konsumpcyjnych – kredyt nie jest prezentem.",
    "Budżet to Twój sojusznik, nie wróg – on daje Ci wolność.",
    "Każdy nieplanowany wydatek to szansa na naukę – nie wyrzuty sumienia.",
    "Oszczędzaj na cele, nie z lęku – to zmienia nastawienie."
]

if dochód > 0:
    st.subheader("📊 Proponowany podział budżetu:")
    kwoty = {}
    suma_wydatków = 0

    for kategoria, procent in proporcje.items():
        kwota = round(dochód * procent, 2)
        kwoty[kategoria] = kwota
        suma_wydatków += kwota
        udzial_proc = round((kwota / dochód) * 100, 1)
        st.write(f"**{kategoria}**: {kwota} zł ({udzial_proc}%)")

    # Oblicz ile zostaje po wszystkim
    zostaje = round(dochód - suma_wydatków, 2)
    if zostaje > 0:
        st.success(f"💡 Po wszystkim zostaje Ci jeszcze: **{zostaje} zł** – możesz je dorzucić do oszczędności albo zainwestować!")
    elif zostaje < 0:
        st.error(f"⚠️ Wydajesz więcej niż zarabiasz o **{-zostaje} zł** – sprawdź proporcje!")
    else:
        st.info("📘 Budżet się bilansuje idealnie.")

    # Wykres kołowy
    st.subheader("📈 Wizualizacja budżetu:")
    fig, ax = plt.subplots()
    ax.pie(kwoty.values(), labels=kwoty.keys(), autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    # Dobra rada na dziś
    st.subheader("💡 Dobra rada na dziś:")
    st.info(random.choice(rady))

else:
    st.info("🔎 Wprowadź dochód, aby zobaczyć podział budżetu.")
