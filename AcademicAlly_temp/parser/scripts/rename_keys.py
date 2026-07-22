import json
import re

def convert_key(k):
    # Matches patterns like 3Q1A, 3C81B, 1A1E
    # Where the last character is a letter A-Z and the rest looks like a subgroup
    if re.match(r'^[1-4][A-Z]\d{1,2}[A-Z]$', k):
        last_char = k[-1]
        num = ord(last_char) - ord('A') + 1
        return k[:-1] + str(num)
    return k

with open('d:/ACM_Timetable/ACMTimeTable/src/assets/results_updated.json', 'r') as f:
    results = json.load(f)

new_results = {}
for k, v in results.items():
    if k is None or str(k) in ['None', 'null', 'DAY', 'HOURS']: continue
    new_results[convert_key(k)] = v

with open('d:/ACM_Timetable/ACMTimeTable/src/assets/results_updated.json', 'w') as f:
    json.dump(new_results, f, indent=4)

with open('d:/ACM_Timetable/ACMTimeTable/src/assets/subgroup.json', 'r') as f:
    subgroups = json.load(f)

new_subgroups = {}
for k in subgroups.keys():
    if k is None or str(k) in ['None', 'null', 'DAY', 'HOURS']: continue
    new_key = convert_key(k)
    new_subgroups[new_key] = new_key

with open('d:/ACM_Timetable/ACMTimeTable/src/assets/subgroup.json', 'w') as f:
    json.dump(new_subgroups, f, indent=4)

print("Keys successfully renamed.")
