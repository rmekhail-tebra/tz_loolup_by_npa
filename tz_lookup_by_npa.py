#!/usr/bin/env python
# tz_lookup_by_npa.py

import requests
import json

'''
List of North American Area Codes via
https://www.att.com/ecms/dam/att/smb/help/pdf/Area-Codes-N-America-by-State.pdf
'''
AREA_CODES = [
    205, 251, 256, 334, 938, 907, 403, 587, 780, 480, 520, 602, 623, 928, 479,
    501, 870, 236, 250, 604, 778, 209, 213, 310, 323, 408, 415, 424, 442, 510,
    530, 559, 562, 619, 626, 650, 657, 661, 669, 707, 714, 747, 760, 805, 818,
    831, 858, 909, 916, 925, 949, 951, 303, 719, 720, 970, 203, 475, 860, 302,
    202, 239, 305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863,
    904, 941, 954, 229, 404, 470, 478, 678, 706, 762, 770, 912, 808, 208, 217,
    224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872, 219, 260, 317,
    574, 765, 812, 319, 515, 563, 641, 712, 316, 620, 785, 913, 270, 364, 502,
    606, 859, 225, 318, 337, 504, 985, 207, 204, 431, 240, 301, 410, 443, 667,
    339, 351, 413, 508, 617, 774, 781, 857, 978, 231, 248, 269, 313, 517, 586,
    616, 734, 810, 906, 947, 989, 218, 320, 507, 612, 651, 763, 952, 228, 601,
    662, 769, 314, 417, 573, 636, 660, 816, 406, 308, 402, 531, 702, 725, 775,
    506, 603, 201, 551, 609, 732, 848, 856, 862, 908, 973, 505, 575, 212, 315,
    347, 516, 518, 585, 607, 631, 646, 716, 718, 845, 914, 917, 929, 709, 252,
    336, 704, 828, 910, 919, 980, 984, 701, 902, 216, 234, 330, 419, 440, 513,
    567, 614, 740, 937, 405, 539, 580, 918, 226, 249, 289, 343, 365, 416, 437,
    519, 613, 647, 705, 807, 905, 458, 503, 541, 971, 215, 267, 272, 412, 484,
    570, 610, 717, 724, 814, 878, 418, 438, 450, 514, 579, 581, 819, 873, 401,
    306, 639, 803, 843, 864, 605, 423, 615, 731, 865, 901, 931, 210, 214, 254,
    281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 737, 806, 817, 830,
    832, 903, 915, 936, 940, 956, 972, 979, 710, 385, 435, 801, 802, 276, 434,
    540, 571, 703, 757, 804, 206, 253, 360, 425, 509, 304, 681, 262, 414, 534,
    608, 715, 920, 307, 867, 242, 246, 264, 268, 284, 340, 345, 441, 456, 473,
    500, 533, 544, 566, 577, 600, 649, 664, 670, 671, 684, 700, 721, 758, 767,
    784, 787, 809, 829, 849, 868, 869, 876, 939,
]
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
area_code_timezone = {}
for area_code in AREA_CODES:
    tz_data = get_tz_by_npa(area_code)
    time_zone = tz_data.get("areaCode", {}).get("geographicCodeInformation", {}).get("timeZone", "Not Found").replace('(', '').replace(')', '')
    # assume the firsrt character is the Eastern most time zone
    if time_zone not in TIME_ZONES:
        time_zone = time_zone[0]
    area_code_timezone[area_code] = ZONE_TO_ZONEID.get(time_zone, 'unknown ' + time_zone) 
area_code_map = json.dumps(area_code_timezone, indent=4)
print(area_code_map)
