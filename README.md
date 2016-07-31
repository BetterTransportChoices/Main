# Transport Alert

Transport Alert is a mobile application which alerts the user to localized road and public disruptions and events.

## Data sources used

The disruption screen displays a Google Map with two disruption layers:

1. [Google Maps Traffic Layer](https://developers.google.com/maps/documentation/javascript/trafficlayer) (as VicRoads live traffic API was not available in time for GovHack)
2. Real-time disruption information from the [PTV Timetable API](https://www.data.vic.gov.au/data/dataset/ptv-timetable-api). This needs to be parsed in two steps:

    1. Display PTV stops in the selected area
    2. Parse the text descriptions in the disruption data to correlate them with nearby stops (as disruption data does not provide geographical data)
