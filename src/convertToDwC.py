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
    "organismID" : ["FLORACODE"],
    "identificationID" : ["ï»¿KEY" ],
    "occurrenceRemarks" : ["SIGHTINGCOMM"]
}

# Headers that should be converted to ISO 8601, and their format
convertMap = {
    "%d/%m/%y" : ["SIGHTINGDATE"]
}

# Columns to discard
discard = [
    "NSXCODE"
]

# Generate reverse lookup from above dictionarys
labelLookup = {colName: converted for converted, colList in labelMap.items() for colName in colList}
convertLookup = {colName: fmt for fmt, colList in convertMap.items() for colName in colList}

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please give a path to a csv file to convert as first arg, and path to an output file optionally as second arg.")
        sys.exit()
    
    inp = sys.argv[1]
    if not inp.endswith(".csv"):
        print("Invalid file type. Input file should be of type .csv")
        sys.exit()

    if len(sys.argv) > 2:
        out = sys.argv[2]
        if not out.endswith(".csv"):
            print("Output file should end with .csv")
            sys.exit()
    else:
        out = "output.csv"

    with open(inp) as fp:
        data = fp.read()

    dataLines = data.split('\n')

    ignoreCols = [] # list of column indexes to ignore
    reformatDateCols = {} # dictionary of form {index: date format} for converting to ISO 8601

    colHeaders = [] # list of converted headers
    for ref, colName in enumerate(dataLines.pop(0).split(',')): # Pop first line to get headers
        if colName in discard:
            ignoreCols.append(ref)
            continue

        if colName in convertLookup:
            reformatDateCols[ref] = convertLookup[colName]

        colHeaders.append(labelLookup.get(colName, colName))

    output = ",".join(colHeaders) # Create output from headers list

    while dataLines:
        lineValues = []
        entry = dataLines.pop(0) # Pop columns to reduce memory overhead of potentially large files
        for ref, value in enumerate(entry.split(',')):
            if ref in ignoreCols:
                continue

            if ref in reformatDateCols:
                date = datetime.strptime(value, reformatDateCols[ref])
                lineValues.append(date.isoformat())
                continue

            lineValues.append(value)

        output += f"\n{','.join(lineValues)}"
            
    with open(out, 'w') as fp:
        fp.write(output)
