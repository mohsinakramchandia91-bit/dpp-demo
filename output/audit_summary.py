def generate_audit_summary(dpp_obj):
    lines = []

    cr = dpp_obj.compliance_report

    lines.append("DIGITAL PRODUCT PASSPORT – AUDIT SUMMARY")
    lines.append("=" * 45)
    lines.append(f"Product ID      : {dpp_obj.product_id}")
    lines.append(f"Batch ID        : {dpp_obj.batch_id}")
    lines.append(f"DPP Version     : {dpp_obj.version}")
    lines.append(f"Created At      : {dpp_obj.created_at}")
    lines.append("")
    lines.append("COMPLIANCE STATUS")
    lines.append("-" * 20)
    lines.append(f"Status          : {cr.get('status')}")
    lines.append(f"Batch Confidence: {cr.get('batch_confidence')}")
    lines.append("")

    lines.append("RISKS IDENTIFIED")
    lines.append("-" * 20)
    if cr.get("risks"):
        for r in cr.get("risks"):
            lines.append(f"- {r}")
    else:
        lines.append("None")

    lines.append("")
    lines.append("GUIDANCE / NEXT ACTIONS")
    lines.append("-" * 20)
    if cr.get("guidance"):
        for g in cr.get("guidance"):
            lines.append(f"- {g}")
    else:
        lines.append("None")

    lines.append("")
    lines.append("NOTE:")
    lines.append("This summary is system-generated and based on provided data.")
    lines.append("All values include confidence scoring and are auditable.")

    return "\n".join(lines)
