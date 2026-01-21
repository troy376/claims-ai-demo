import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Claims AI Demo", layout="centered")

# App header
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

# Input: paste claim description
claim_text = st.text_area("Paste a claim description below:")

# Button: Analyze Claim
if st.button("Analyze Claim"):
    if claim_text.strip() == "":
        st.warning("Please enter a claim description.")
    else:
        # Water Damage
        if "water damage" in claim_text.lower():
            st.success("Claim analyzed successfully.")
            st.write("**AI Summary:**")
            st.write("""
✅ Claim analyzed successfully.

**Key Findings:**
- Water damage detected in kitchen affecting hardwood, baseboards, and drywall.
- Moisture readings indicate high levels (18% main wall, 12% adjoining walls), remediation required.
- Xactimate line items match policy coverage:
    - Floor replacement ✅
    - Baseboard replacement ✅
    - Drywall repair ✅
    - Mold remediation ✅
- Policy coverage confirmed: Water Backup & Overflow endorsement.

**Suggested Actions:**
- Proceed with full remediation per policy limits.
- Ensure documentation of drying process for claim support.
            """)
        
        # Fire & Smoke Damage
        elif "fire" in claim_text.lower():
            st.success("Claim analyzed successfully.")
            st.write("**AI Summary:**")
            st.write("""
✅ Claim analyzed successfully.

**Key Findings:**
- Fire and smoke damage throughout main floor; minor charring observed.
- Moisture readings post-sprinkler activation within expected range.
- Xactimate line items correspond to policy coverage:
    - Soot removal ✅
    - Ceiling repair ✅
    - Hardwood sanding & refinishing ✅
    - Deodorization ✅
- Policy coverage confirmed: Fire & Smoke.

**Suggested Actions:**
- Proceed with full restoration.
- Document odor removal and minor structural repairs for insurer.
            """)
        
        # Roof / Windstorm Damage
        elif "roof" in claim_text.lower() or "windstorm" in claim_text.lower():
            st.success("Claim analyzed successfully.")
            st.write("**AI Summary:**")
            st.write("""
✅ Claim analyzed successfully.

**Key Findings:**
- Windstorm caused roof shingle loss; minor water intrusion in attic.
- Moisture readings indicate minimal water exposure (10% ceiling).
- Xactimate line items covered by policy:
    - Roof shingle replacement ✅
    - Attic water mitigation ✅
    - Ceiling drywall repair ✅
- Policy coverage confirmed: Windstorm.

**Suggested Actions:**
- Repair roof and mitigate attic water damage.
- Document repairs and drying process for claim records.
            """)
        
        # Other / unknown claims
        else:
            st.info("Claim analyzed successfully, no major issues detected.")
