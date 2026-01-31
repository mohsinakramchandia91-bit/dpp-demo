def base_confidence(source_type, value):
    """
    Very conservative defaults
    """

    if value is None:
        return 0

    if source_type == "manual":
        return 50

    if source_type == "excel":
        return 70

    if source_type == "erp":
        return 90

    return 40
