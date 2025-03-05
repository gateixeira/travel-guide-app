def check_destination(destination: str) -> bool:
    # Validate that the destination is a non-empty string
    return isinstance(destination, str) and len(destination) > 0

def check_days(days: int) -> bool:
    # Validate that the number of days is a positive integer
    return isinstance(days, int) and days > 0