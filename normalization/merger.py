def merge_field(existing, incoming):
    """
    Decide which value to keep at batch level
    """

    # If existing missing, take incoming
    if existing is None:
        return incoming

    # If incoming missing, keep existing
    if incoming["value"] is None:
        return existing

    # If incoming more confident, replace
    if incoming["confidence"] > existing["confidence"]:
        return incoming

    return existing
