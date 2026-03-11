#!/usr/bin/env python
# tz_lookup_by_npa.py

import requests
import json

def load_area_codes(filename="area_codes.txt"):
    """Loads area codes from a text file."""
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]

AREA_CODES = load_area_codes()
TIME_ZONES = {'UTC-11', 'UTC-10', 'AK', 'P', 'M', 'C', 'E', 'A', 'N', 'UTC+10'}
ZONE_TO_ZONEID = {'UTC-11': 'Pacific/Pago_Pago', 'UTC-10': 'Pacific/Honolulu',
                   'AK': 'America/Anchorage', 'P': 'America/Los_Angeles', 
                   'M': 'America/Denver', 'C': 'America/Chicago', 
                   'E': 'America/New_York', 'A': 'America/Puerto_Rico', 
                   'N': 'America/St_Johns', 'UTC+10': 'Pacific/Guam'}
def get_tz_by_npa(npa):
    url = f"https://api.nanpa.com/reports/public/npa/areaCodeListing?npa={npa}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    area_code_timezone = {}
    for idx, area_code in enumerate(AREA_CODES):
        tz_data = get_tz_by_npa(area_code)
        print(f"Got tz data for {area_code} ({idx}/{len(AREA_CODES)})", end="")
        time_zone = tz_data.get("areaCode", {}).get("geographicCodeInformation", {}).get("timeZone", "Not Found").replace('(', '').replace(')', '')
        # assume the firsrt character is the Eastern most time zone
        if time_zone not in TIME_ZONES:
            time_zone = time_zone[0]
        time_zone = ZONE_TO_ZONEID.get(time_zone, 'unknown ' + time_zone) 
        area_code_timezone[area_code] = time_zone
        print(time_zone)
    area_code_map = json.dumps(area_code_timezone, indent=4)
    with open("tz_map.json", "w") as f:
        f.write(area_code_map)
    print(f"Successfully wrote {len(area_code_timezone)} area codes to tz_map.json")
