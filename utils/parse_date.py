from datetime import datetime

def parse_date(date_str: str | None):
  if not date_str:
    return None
  try:
    return datetime.fromisoformat(date_str).date()
  except ValueError:
    return datetime.fromisoformat(date_str.split("T")[0]).date()
