def guidance_for_risks(risks):
    suggestions = []

    for r in risks:
        if "cotton_percent" in r:
            suggestions.append(
                "Provide verified cotton percentage (e.g. lab test or supplier declaration)."
            )
        elif "energy_source" in r:
            suggestions.append(
                "Specify energy source used (grid, solar, gas) with estimate."
            )
        else:
            suggestions.append(
                "Provide missing or low-confidence data for this field."
            )

    return suggestions
