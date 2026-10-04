"""Sanitized educational example — not production Risk Engine code."""


def approximate_pv01(market_value: float, modified_duration: float) -> float:
    """Approximate value change for a +1 bp yield move."""
    return -modified_duration * market_value * 0.0001


if __name__ == "__main__":
    value = approximate_pv01(market_value=100_000_000_000, modified_duration=4.2)
    print(f"Approximate PV01: {value:,.0f} VND")
