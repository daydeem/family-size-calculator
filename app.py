import streamlit as st

def calculate_family_size(sisters: int, marriage_type: str, wives: int = 1) -> int:
    husband = 1
    sons = 9

    if marriage_type == "Single":
        wives = 1
    elif marriage_type == "Multiple":
        if wives < 1:
            raise ValueError("Wives must be at least 1.")
    else:
        raise ValueError("Marriage type must be Single or Multiple.")

    return husband + wives + sons + sisters


st.set_page_config(page_title="Family Size Calculator", page_icon="👨‍👩‍👧‍👦")

st.title("👨‍👩‍👧‍👦 Family Size Calculator")
st.write("Assumption: 1 husband + 9 sons + configurable wives and sisters")

marriage_type = st.radio("Marriage type", ["Single", "Multiple"], horizontal=True)

wives = 1
if marriage_type == "Multiple":
    wives = st.number_input("Number of wives", min_value=1, value=2, step=1)

sisters = st.number_input("Number of sisters (daughters)", min_value=0, value=1, step=1)

if st.button("Calculate"):
    total = calculate_family_size(int(sisters), marriage_type, int(wives))
    st.success(f"Total family size: {total}")
    st.write(f"Breakdown: 1 husband + {int(wives)} wife/wives + 9 sons + {int(sisters)} sister(s)")
