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

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Return the difference, percent of limit and status for one record."""
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report line for one record."""
    print(f"{label}: {value:.1f} of {limit:.1f} ({percent:.1f}%), difference {difference:+.1f}, {status}")


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


def save_results(path, results):
    """Write one label,status line per record to a new file."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

try:
    records = load_records("login_data.txt")
except FileNotFoundError:
    print("login_data.txt not found, starting with no records")
    records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_count = 0
results = []

for rec in records:
    difference, percent, status = check_record(rec["value"], rec["limit"])
    print_report(rec["label"], rec["value"], rec["limit"], difference, percent, status)
    results.append((rec["label"], status))
    if status == "OVER LIMIT":
        over_count += 1

print(f"{over_count} record(s) OVER LIMIT")
save_results("results.txt", results)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
