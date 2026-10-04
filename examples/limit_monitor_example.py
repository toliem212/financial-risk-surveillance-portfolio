"""Sanitized example of limit utilisation classification."""


def classify_limit(current: float, limit: float) -> tuple[float, str]:
    if limit <= 0:
        raise ValueError("limit must be positive")

    utilisation = abs(current) / limit
    if utilisation >= 1.0:
        status = "BREACH"
    elif utilisation >= 0.8:
        status = "WARNING"
    else:
        status = "NORMAL"
    return utilisation, status
