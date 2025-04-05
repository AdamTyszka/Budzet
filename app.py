# --- Sekcja JEDZENIE z opcją prognozowania procentem ---
def obszar_jedzenie(dochód):
    st.subheader("📂 Jedzenie")
    st.caption("💬 Proponowany udział: 10–15%")

    prognoza_proc = 0
    suma = 0

    use_percent = st.checkbox("💡 Chcę wpisać % budżetu na jedzenie zamiast kwot")

    if use_percent:
        prognoza_proc = st.slider("Prognozowany % budżetu", min_value=0, max_value=50, value=10)
        prog_kwota = round((prognoza_proc / 100) * dochód, 2)
        st.info(f"To oznacza **około {prog_kwota} zł** przy budżecie {dochód} zł.")
        return prog_kwota  # pomijamy wpisy manualne
    else:
        col1, col2 = st.columns([1,1])
        with col1:
            st.button(f"➕ Dodaj Jedzenie", on_click=add_row, args=("jedzenie",))
        with col2:
            st.button(f"➖ Usuń Jedzenie", on_click=remove_row, args=("jedzenie",))

        for i in range(st.session_state["jedzenie_rows"]):
            nazwa = st.text_input(f"Jedzenie {i+1} – nazwa", key=f"jedzenie_nazwa_{i}")
            kwota = st.number_input(f"Jedzenie {i+1} – kwota (zł)", min_value=0.0, step=10.0, key=f"jedzenie_kwota_{i}")
            suma += kwota
        return suma
