# tz_lookup_by_npa
This repository contains scripts to generate a JSON map from North American Numbering Plan (NANP) area codes to their corresponding canonical time zone names. For example, an area code of "310" will map to "America/Los_Angeles".

## Scripts

### `fetch_area_codes.py`
This script fetches the list of area codes from an official source at `https://www.npanxxsource.com/area-codes.htm`. It then parses the HTML to extract the area codes, sorts them, and writes them to `area_codes.txt`.

**Usage:**
```bash
python fetch_area_codes.py
```

### `tz_lookup_by_npa.py`
This script reads the list of area codes from `area_codes.txt` and uses the North American Numbering Plan Administrator (NANPA) API to look up the time zone for each area code. It then generates a JSON file named `tz_map.json` containing the mapping.

**Usage:**
```bash
python tz_lookup_by_npa.py
```

## Workflow
1. Run `fetch_area_codes.py` to get the most up-to-date list of area codes.
2. Run `tz_lookup_by_npa.py` to generate the `tz_map.json` file.