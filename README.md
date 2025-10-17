# tz_lookup_by_npa
Uses NANPA to look up a time zone by the numbering plan area code (NPA/area code) and produces a map of the code => the canonical time zone name. For example, if the area code is "310", then it will map "310": "America/Los_Angeles".

## Assumptions
* Area code list from AT&T: 
* The time zones values are one of
    - UTC-11
    - UTC-10
    - AK
    - P
    - M
    - C
    - E
    - A
    - N
    - UTC+10
