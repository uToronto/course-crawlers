#!/usr/bin/env python

import arrow
import csv
import requests

if __name__ == "__main__":
    url = "https://www.utsc.utoronto.ca/~registrar/timetable_src/export.php"

    inputfields = (
            "course",
            "room", 
            "note",
            "weekday",
            "start",
            "end",
            "room",
            "instructor",
            "changes",
            )

    outputfields = (
            "course",
            "section", 
            "room",
            "instructor",
            "weekday",
            "start",
            "end",
            )

    data = requests.get(url)
    courses = csv.DictReader(data.text.splitlines(), fieldnames = inputfields)
    result = []
    courses.next() # Skip the headers.
    with open("courses.csv", "wb") as output:
        outdict = csv.DictWriter(output, fieldnames = outputfields)
        outdict.writeheader()
        for row in courses:
            # Add section
            row["course"], row["section"] = row["course"].split()
            row.pop("note")
            row.pop("changes")
            outdict.writerow(row)
