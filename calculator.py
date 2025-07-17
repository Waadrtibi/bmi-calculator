import streamlit as st
st.title('💪 Welcome to BMI Calculator')
weight = st.number_input("Entrez votre poids (en kg)", min_value=0.0, format="%.2f")

status = st.radio("📏 Sélectionnez le format de votre taille :", ('cm', 'mètres', 'pieds'))

bmi = None

if status == 'cm':
    height = st.number_input("Taille en centimètres", min_value=0.0, format="%.2f")
    try:
        bmi = weight / ((height / 100) ** 2)
    except ZeroDivisionError:
        st.error("⚠️ Veuillez entrer une taille supérieure à zéro.")

elif status == 'mètres':
    height = st.number_input("Taille en mètres", min_value=0.0, format="%.2f")
    try:
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        st.error("⚠️ Veuillez entrer une taille supérieure à zéro.")

elif status == 'pieds':
    height = st.number_input("Taille en pieds", min_value=0.0, format="%.2f")
    try:
        height_m = height / 3.28  # conversion en mètres
        bmi = weight / (height_m ** 2)
    except ZeroDivisionError:
        st.error("⚠️ Veuillez entrer une taille supérieure à zéro.")

if st.button('🧮 Calculer votre IMC'):
    if bmi:
        st.success(f"✅ Votre IMC est : {bmi:.2f}")
        
        if bmi < 16:
            st.error("🚨 Vous êtes extrêmement maigre")
        elif bmi < 18.5:
            st.warning("⚠️ Vous êtes en sous-poids")
        elif bmi < 25:
            st.success("✅ Vous êtes en bonne santé")
        elif bmi < 30:
            st.warning("⚠️ Vous êtes en surpoids")
        else:
            st.error("🚨 Obésité")
    else:
        st.error("❌ Veuillez entrer des valeurs valides")
