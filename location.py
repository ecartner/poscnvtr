"""Provides basic class and tools for working with overlay locations"""

import re
import math
from typing import Optional

class Location:
    """Class for UI-View overlay entries"""
    def __init__(self, name, lat, lon, table, symbol) -> None:
        self.name = name
        self.latitude = lat
        self.longitude = lon
        self.table = table
        self.symbol = symbol

    def __str__(self) -> str:
        return f"{self.name} ({self.latitude}{self.longitude})"

    def json_str(self) -> str:
        """Return this location in RadarScope style JSON"""
        name = f"\"name\": \"{self.name}\""
        lat = f"\"lat\": {self.latitude:f}"
        lon = f"\"lon\": {self.longitude:f}"
        return f"{{{name}, {lat}, {lon}}}"

    def lat_deg_min(self) -> str:
        """Return latitude as a degree and decimal minute string"""
        hemisphere = 'N' if self.latitude >= 0 else 'S'
        abs_degrees = abs(self.latitude)
        mod_degrees = math.modf(abs_degrees)
        whole_degrees= int(mod_degrees[1])
        minutes = mod_degrees[0] * 60

        return f"{whole_degrees:0>2d}{minutes:0>4.2f}{hemisphere}"

    def lon_deg_min(self) -> str:
        """Return longitude as a degree and decimal minute string"""
        hemisphere = 'E' if self.longitude >= 0 else 'W'
        abs_degrees = abs(self.longitude)
        mod_degrees = math.modf(abs_degrees)
        whole_degrees = int(mod_degrees[1])
        minutes = mod_degrees[0] * 60

        return f"{whole_degrees:0>3d}{minutes:0>4.2f}{hemisphere}"

    def pos_str(self) -> str:
        """Return this location as a APRS/UI-View formatted string"""
        return f"{self.name}!{self.lat_deg_min()}{self.table}{self.lon_deg_min()}{self.symbol}"

    def xastir_str(self, timestamp) -> str:
        """Return this location as a Xastir log formatted string"""
        return f";{self.name:9.9s}*{timestamp}{self.lat_deg_min()}{self.table}{self.lon_deg_min()}{self.symbol}"

# Format is [name]![latitude][icon][bunch of stuff we don't care about]
# [name] is call sign or name 9 characters or less
# [latitude] latitude in Degrees, decimal minutes and then N or S: DDMM.MM[NS]
# [longitude] longitude in Degrees, decimal minutes and then E or W: DDDMM.MM[EW]
pos_pattern = re.compile(r"(.+)!(\d\d)(\d\d\.\d\d)([SN])([/\\0-9A-J])(\d\d\d)(\d\d\.\d\d)([EW])([/\\0-9A-J]).*")

def loc_from_pos(pos) -> Optional[Location]:
    """Extract a Location from an APRS/UI-View POS string"""
    if match := pos_pattern.match(pos):
        name = match.group(1)
        lat_d = match.group(2)
        lat_m = match.group(3)
        lat_hemisphere = match.group(4)
        sym_table = match.group(5)
        lon_d = match.group(6)
        lon_m = match.group(7)
        lon_hemisphere = match.group(8)
        symbol = match.group(9)

        lat = float(lat_d) + float(lat_m) / 60.0
        if lat_hemisphere == 'S':
            lat *= -1.0

        lon = float(lon_d) + float(lon_m) / 60.0
        if lon_hemisphere == 'W':
            lon *= -1.0

        return Location(name, lat, lon, sym_table, symbol)

    return None
