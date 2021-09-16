from datetime import date, time, datetime
import datetime as dt
import hashlib
import json
from operator import itemgetter, attrgetter
import operator

def find_duplicate_transactions(*transactions: dict):
  
  hashdict = {}
  tocheck  = []
  result   = []
  final_result   = []
  
  #transactions = sorted(transactions, key=lambda k: datetime.fromisoformat(k['time'][:-1]))
  for idx,t in enumerate(transactions):
    hash_t = hashlib.sha256(
      str(
       t["sourceAccount"]+t["targetAccount"]+t["category"]+str(t["amount"])
      ).encode('utf-8')).hexdigest()[:16]
    
    if hash_t in hashdict:
      hashdict[hash_t]["count"] += 1
      hashdict[hash_t]["items"].append(t)
      tocheck.append(hash_t)
    else:
      hashdict[hash_t] = {}
      hashdict[hash_t]["count"] = 1
      hashdict[hash_t]["items"] = [t]
      
  tocheck = list(set(tocheck))
  
  for c in tocheck:
    n = 0
    result   = []
    tmp_trans = sorted(hashdict[c]["items"], key=lambda k: datetime.fromisoformat(k['time'][:-1]))
    
    while n < len(tmp_trans)-1:
      cur = tmp_trans[n]
      nex = tmp_trans[n+1]
        
      if ((abs((datetime.fromisoformat(str(cur["time"][:-1])) - datetime.fromisoformat(str(nex["time"][:-1]))).total_seconds())) >= 0) and ((abs((datetime.fromisoformat(str(cur["time"][:-1])) - datetime.fromisoformat(str(nex["time"][:-1]))).total_seconds())) < 60) and (cur["id"] != nex["id"]):
        if (len(result) == 0) or (result[-1] != cur):
          result.append(cur)
        result.append(nex)
      n += 1
    #result = sorted(result, key=lambda k: datetime.fromisoformat(k['time'][:-1]))
    if len(result) > 0:
      final_result.append(result)
  
  #print(sorted(final_result, key=lambda k: [print(i['time']) for i in k] ))
  return sorted(final_result, key=lambda k: [i['time'] for i in k] )
