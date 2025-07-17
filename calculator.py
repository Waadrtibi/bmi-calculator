import streamlit as st

st.title('Welcome to BMI Calculator')

weight = st.number_input("Entrez votre poids (en kg)", min_value=0.0, format="%.2f")

status = st.radio("📏 Sélectionnez le format de votre taille :", ('cm', 'mètres', 'pieds'))

height = 0.0

if status == 'cm':
    height = st.number_input("Taille en centimètres", min_value=0.0, format="%.2f")
elif status == 'mètres':
    height = st.number_input("Taille en mètres", min_value=0.0, format="%.2f")
elif status == 'pieds':
    height = st.number_input("Taille en pieds", min_value=0.0, format="%.2f")

if st.button('🧮 Calculer votre IMC'):
    if weight <= 0:
        st.error("Veuillez entrer un poids valide supérieur à zéro.")
    elif height <= 0:
        st.error("Veuillez entrer une taille valide supérieure à zéro.")
    else:
        # Conversion en mètres
        if status == 'cm':
            height_m = height / 100
        elif status == 'mètres':
            height_m = height
        else:  # pieds
            height_m = height * 0.3048  # conversion correcte

        bmi = weight / (height_m ** 2)
        st.success(f"Votre IMC est : {bmi:.2f}")

        if bmi < 16:
            st.error("Vous êtes extrêmement maigre")
        elif bmi < 18.5:
            st.warning("Vous êtes en sous-poids")
        elif bmi < 25:
            st.success("Vous êtes en bonne santé")
        elif bmi < 30:
            st.warning("Vous êtes en surpoids")
        else:
            st.error("🚨 Obésité")
