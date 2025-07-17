import streamlit as st

st.title("🚗 Speed Calculator")

distance = st.number_input("Enter distance (in kilometers):", min_value=0.0, format="%.2f")
time = st.number_input("Enter time (in hours):", min_value=0.0, format="%.2f")

if time > 0:
    speed = distance / time
    st.success(f"Calculated speed: **{speed:.2f} km/h**")
elif time == 0 and distance > 0:
    st.warning("⚠️ Time must be greater than zero.")
else:
    st.info("Please enter both distance and time.")
