"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
from pathlib import Path
# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    line = raw_line.strip().lower()
    record = {}
    for piece in line.split(","):
        if "=" not in piece:
            continue
        key, value = piece.split("=")
        key = key.strip()
        value = value.strip()
        if key == "attempts":
            try:
                value = int(value)
            except ValueError:
                value = None
        record[key] = value
    return record
def status_of(record, limit=10):
    attempts = record.get("attempts") or 0
    if record.get("result") == "failed" and  attempts >= limit:
      return "FLAGGED"
    return "OK"  




# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

RECORDS_FILE = Path(__file__).parent / "cyber_records.txt"
raw_records = []   # replace with your code
with open(RECORDS_FILE) as file:
    for line in file:
        if line.strip() != "":
            raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
flagged_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, "->", status)
    if status == "FLAGGED":
        flagged_count += 1
print(f"{len(raw_records)} records processed, {flagged_count} flagged.")  # replace with your code


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
