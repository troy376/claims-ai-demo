import streamlit as st

st.set_page_config(page_title="Claims AI Demo", layout="centered")

st.title("Claims AI Demo")
st.subheader("Automated Insurance Claim Review")

st.markdown(
    """
    This demo simulates how AI can assist insurance claims teams by:
    - Reviewing claim descriptions
    - Flagging potential issues
    - Improving speed and consistency
    """
)

claim_text = st.text_area("Paste a claim description below:")

if st.button("Analyze Claim"):
    if claim_text.strip() == "":
        st.warning("Please enter a claim description.")
    else:
        st.success("Claim analyzed successfully.")
        st.write("**AI Summary:**")
        st.write("No immediate red flags detected. Claim appears consistent.")
