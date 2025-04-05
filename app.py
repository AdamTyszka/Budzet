import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Budżet domowy PRO", layout="centered")
st.title("🏠 Budżet domowy – rozbudowana wersja")

# --- Funkcje pomocnicze ---
def init_state(name, default):
    if name not in st.session_state:
        st.session_state[name] = default

def add_row(key_prefix):
    st.session_state[key_prefix + "_rows"] += 1

def remove_row(key_prefix):
    if st.session_state[key_prefix + "_rows"] > 0:
        st.session_state[key_prefix + "_rows"] -= 1

# --- Inicjalizacja stanu ---
for obszar in ["stałe", "jedzenie", "rozrywka", "transport", "dzieci"]:
    init_state(obszar + "_rows", 0)

# --- Dane wejściowe ---
dochód = st.number_input("Podaj miesięczny dochód netto (zł):", min_value=0, step=100)

# --- Predefiniowane wydatki stałe ---
st.subheader("📌 Wydatki stałe")
st.caption("💬 Proponowany udział nie powinien być większy niż 40% dochodu.")

predef_stale = [
    "Kredyty/pożyczki", "Czynsz", "Prąd", "Gaz", "Woda",
    "Nieczystości", "Śmieci", "Telefon i Internet"
]
suma_stalych = 0

for item in predef_stale:
    kwota = st.number_input(f"{item} (zł)", min_value=0.0, step=10.0, key=f"stałe_{item}")
    suma_stalych += kwota

col1, col2 = st.columns([1,1])
with col1:
    st.button("➕ Dodaj koszt stały", on_click=add_row, args=("stałe",))
with col2:
    st.button("➖ Usuń koszt", on_click=remove_row, args=("stałe",))

for i in range(st.session_state["stałe_rows"]):
    nazwa = st.text_input(f"Koszt stały {i+1} – nazwa", key=f"stałe_nazwa_{i}")
    kwota = st.number_input(f"Kwota {i+1} (zł)", min_value=0.0, step=10.0, key=f"stałe_kwota_{i}")
    suma_stalych += kwota

# --- Obszar dynamiczny z opcjonalnymi predefiniowanymi wierszami ---
def obszar_budzetowy(nazwa_obszaru, sesja_key, komentarz, predefiniowane=None):
    st.subheader(f"📂 {nazwa_obszaru}")
    st.caption(komentarz)

    suma = 0

    if predefiniowane:
        for item in predefiniowane:
            kwota = st.number_input(f"{item} (zł)", min_value=0.0, step=10.0, key=f"{sesja_key}_predef_{item}")
            suma += kwota

    col1, col2 = st.columns([1,1])
    with col1:
        st.button(f"➕ Dodaj {nazwa_obszaru}", on_click=add_row, args=(sesja_key,))
    with col2:
        st.button(f"➖ Usuń {nazwa_obszaru}", on_click=remove_row, args=(sesja_key,))

    for i in range(st.session_state[sesja_key + "_rows"]):
        nazwa = st.text_input(f"{nazwa_obszaru} {i+1} – nazwa", key=f"{sesja_key}_nazwa_{i}")
        kwota = st.number_input(f"{nazwa_obszaru} {i+1} – kwota (zł)", min_value=0.0, step=10.0, key=f"{sesja_key}_kwota_{i}")
        suma += kwota

    return suma

suma_jedzenie = obszar_budzetowy("Jedzenie", "jedzenie", "💬 Proponowany udział: 10–15%")
suma_rozrywka = obszar_budzetowy("Rozrywka", "rozrywka", "💬 Proponowany udział: do 10%")
suma_transport = obszar_budzetowy(
    "Transport", "transport", "💬 Proponowany udział: do 15%",
    predefiniowane=["Paliwo", "Transport publiczny", "Eksploatacja samochodu"]
)
suma_dzieci = obszar_budzetowy(
    "Dzieci", "dzieci", "💬 Proponowany udział: zależnie od liczby dzieci i wieku",
    predefiniowane=["Zajęcia dodatkowe", "Wycieczki", "Obiady w szkole", "Kieszonkowe", "Telefon"]
)

# --- Oszczędności
st.subheader("💼 Oszczędności")
st.caption("💬 Zalecany udział: minimum 10%")
oszczednosci = st.number_input("Kwota oszczędności (zł)", min_value=0.0, step=10.0)

# --- Podsumowanie ---
suma_wszystkiego = suma_stalych + suma_jedzenie + suma_rozrywka + suma_transport + suma_dzieci + oszczednosci
zostaje = dochód - suma_wszystkiego

st.subheader("📊 Podsumowanie")
st.write(f"**Wydatki stałe:** {suma_stalych} zł")
st.write(f"**Jedzenie:** {suma_jedzenie} zł")
st.write(f"**Rozrywka:** {suma_rozrywka} zł")
st.write(f"**Transport:** {suma_transport} zł")
st.write(f"**Dzieci:** {suma_dzieci} zł")
st.write(f"**Oszczędności:** {oszczednosci} zł")
st.write(f"---\n**Suma wydatków:** {suma_wszystkiego} zł")

if zostaje > 0:
    st.success(f"✅ Zostaje Ci: {zostaje} zł – gratulacje!")
elif zostaje < 0:
    st.error(f"❌ Budżet przekroczony o {-zostaje} zł – sprawdź koszty.")
else:
    st.info("🔁 Budżet idealnie się bilansuje.")

# --- Wykres słupkowy ---
st.subheader("📈 Wykres wydatków")
df = pd.DataFrame({
    'Kategoria': ["Stałe", "Jedzenie", "Rozrywka", "Transport", "Dzieci", "Oszczędności"],
    'Kwota': [suma_stalych, suma_jedzenie, suma_rozrywka, suma_transport, suma_dzieci, oszczednosci]
})
st.bar_chart(df.set_index('Kategoria'))

# --- Dobra rada ---
st.subheader("💡 Dobra rada na dziś")
rady = [
    "Najpierw płać sobie – oszczędzaj zaraz po wypłacie.",
    "Nie zapomnij o kosztach, które występują raz na kwartał.",
    "Oszczędzanie to nawyk, nie cel sam w sobie.",
    "Twój budżet nie musi być idealny – ważne, by był Twój.",
    "Zostaw miejsce na życie – nie każdy wydatek to problem."
]
st.info(random.choice(rady))
