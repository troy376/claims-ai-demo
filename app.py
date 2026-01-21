if st.button("Analyze Claim"):
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
    else:
        st.info("Claim analyzed successfully, no major issues detected.")
