import sys
from datetime import datetime

# Map values set as a list to dynamically add more
labelMap = {
    "identificationVerificationStatus" : ["SPRELIABCODE"],
    "individualCount" : ["NUMOBSERVED"],
    "eventDate" : ["SIGHTINGDATE"],
    "indentifiedBy" : ["OBSERVER"],
    "verbatimElevation" : ["RELIABDESC"],
    "decimalLatitude" : ["LATITUDE"],
    "deciamlLongitude" : ["LONGITUDE"],
    "verbatimLocality" : ["LOCATIONCOMM"],
    "collectionCode" : ["SOURCE"],
    "habitat" : ["HABITATCOMM"],
    "vernacularName" : ["COMNAME1"],
    "family" : ["FAMILYNAME"],
    "specificEpithet" : ["SPECIES"],
    "locationAccordingTo" : ["SURVEYNAME"],
    "identificationID" : ["FLORACODE"],
    "occurrenceRemarks" : ["SIGHTINGCOMM"]
}

# Generate reverse lookup from above dictionary
labelLookup = {label: key for key, value in labelMap.items() for label in value}

# Columns to discard
discard = [
    "NSXCODE",
    "ï»¿KEY" 
]

# Headers that should be converted to ISO 8601
convertDate = {
    "eventDate" : "%d/%m/%y"
}

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please give a path to a file to convert as argument.")
        sys.exit()
    
    inp = sys.argv[1]
    if not inp.endswith(".csv"):
        print("Invalid file type. Input file should be of type .csv")
        sys.exit()

    with open(inp) as fp:
        data = fp.read()

    dataLines = data.split('\n')

    ignoreCols = []
    reformatDateCols = {}

    colHeaders = []
    for ref, colName in enumerate(dataLines.pop(0).split(',')):
        if colName in discard:
            ignoreCols.append(ref)
            continue

        header = labelLookup.get(colName, colName)
        colHeaders.append(header)

        if header in convertDate:
            reformatDateCols[ref] = convertDate[header]

    output = ",".join(colHeaders)

    while dataLines:
        entry = dataLines.pop(0)
        lineValues = []
        for ref, value in enumerate(entry.split(',')):
            if ref in ignoreCols:
                continue

            if ref in reformatDateCols:
                date = datetime.strptime(value, reformatDateCols[ref])
                lineValues.append(date.isoformat())
                continue

            lineValues.append(value)

        output += f"\n{','.join(lineValues)}"
            
    with open("output.csv", 'w') as fp:
        fp.write(output)
