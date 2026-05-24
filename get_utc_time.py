#!/usr/bin/env python3
"""
Script to get the current UTC time
"""

from datetime import datetime
import pytz

def get_utc_time():
    """Get the current UTC time"""
    utc_timezone = pytz.UTC
    current_utc_time = datetime.now(utc_timezone)
    return current_utc_time

if __name__ == "__main__":
    utc_time = get_utc_time()
    print(f"Current UTC Time: {utc_time}")
    print(f"Formatted: {utc_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
