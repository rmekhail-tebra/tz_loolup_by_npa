#!/usr/bin/env python
# fetch_area_codes.py

import requests
from bs4 import BeautifulSoup

def fetch_area_codes():
    """
    Fetches area codes from https://www.npanxxsource.com/area-codes.htm,
    sorts them, and returns them as a list of integers.
    """
    url = "https://www.npanxxsource.com/area-codes.htm"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')

    area_codes = []
    # Find the table containing the area codes.
    # A bit brittle, but the table is currently the first one on the page.
    # NOTE: This table does also contain an associated timezone, but it doesn't
    #       have entries for every area code (e.g.: 670, 671). We'll continue
    #       to use the lookup script, instead.
    table = soup.find('table')
    if not table:
        raise ValueError("No table found on the page.")

    # Iterate over the rows, skipping the header
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if cells:
            area_code_str = cells[0].text.strip()
            if area_code_str.isdigit():
                area_codes.append(int(area_code_str))

    return sorted(list(set(area_codes)))

if __name__ == "__main__":
    try:
        codes = fetch_area_codes()
        with open("area_codes.txt", "w") as f:
            for code in codes:
                f.write(f"{code}\n")
        print(f"Successfully wrote {len(codes)} area codes to area_codes.txt")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except (ValueError, IndexError) as e:
        print(f"Error parsing HTML: {e}")

