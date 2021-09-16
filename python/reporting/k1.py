from datetime import date, time, datetime
import datetime as dt

def get_balance_by_category_in_period(category: str, start: dt.datetime, end: dt.datetime, *transactions: dict):

  if (isinstance(start, dt.datetime)) and (isinstance(end, dt.datetime)):
    balance = 0
    
    for t in transactions:
      if str(t['category']).lower().strip() == str(category).lower().strip():
        c_time = datetime.fromisoformat(str(t['time'][:-1]))
        
        if (c_time >= start) and (c_time < end):
          balance = balance + t['amount']
  else:
    raise ValueError("start and end expected to be datetime objects")
    
  return float("%0.2f" % (balance))
