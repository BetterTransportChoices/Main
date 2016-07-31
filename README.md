# Transport Alert

Road and public transport disruptions.

## Data sources used

The disruption screen displays a Google Map with two disruption layers:

1. Google Maps Traffic layer (as VicRoads traffic API was not available in time for GovHack)
2. Real-time disruption information from the PTV Timetable API. This needs to be parsed in two steps:

    1. Display PTV stops in the selected area
    2. Parse the text descriptions in the disruption data to correlate them with nearby stops (as disruption data does not provide geographical data)
