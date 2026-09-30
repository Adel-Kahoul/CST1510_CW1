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

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

source_IP = input("Enter source IP: ")      # replace with an input() call
failed_logins = float(input("Enter failed logins: "))     # replace with an input() call, converted with float()
total_attempts = float(input("Enter total attempts: "))     # replace with an input() call, converted with float()

# | **Cyber Security** | source IP, failed logins, total attempts | `10.0.0.5`, `12`, `400` |
# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference =  total_attempts - failed_logins  # replace with your calculation
percent = (failed_logins / total_attempts * 100)       # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"  # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

'''
==================================
  RECORD CHECK  -  srv-01
==================================
  Used        :      87.00
  Total       :     120.00
  Free        :      33.00
  Percent     :      72.50 %
  Status      :         OK
==================================

'''


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_IP}")
print("=" * 34)
print(f"  Used        : {failed_logins:>10.2f}")
print(f"  Total       : {total_attempts:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Percent     : {percent:>10.2f}%")
print(f"  Status      : {status:>10}")
print("=" * 34)



# your report lines go here



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
