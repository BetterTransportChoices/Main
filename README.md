# Transport Alert

Transport Alert is a mobile application that alerts users to localised road and public disruptions and events. Existing transport apps (such as official PTV apps and TripGo) make use of maps and timetable data but do not incorporate real-time disruptions.

Transport Alert was inspired by the [Victorian FireReady app](http://www.cfa.vic.gov.au/plan-prepare/fireready-app/) that notifies users of local fires and other emergencies.

A prototype is available on [POP](https://popapp.in/w/projects/579d562a81201bbf39c85000/mockups/579d564a2fc58b953ed1cb57). It currently includes:

* The user's current location and a list of user-defined watch zones
* Map and list views of a watch zone with current traffic conditions and disruptions
* Details about specific disruptions
* A share sheet for sharing disruption information to social media

A video explanation is provided on [YouTube](https://youtu.be/IdgftHm7h6k).

The disruption screen displays a Google Map with two layers:

1. [Google Maps Traffic Layer](https://developers.google.com/maps/documentation/javascript/trafficlayer) displaying current traffic conditions (as VicRoads live traffic API was not available in time for GovHack)
2. Real-time disruption information from the [PTV Timetable API](https://www.data.vic.gov.au/data/dataset/ptv-timetable-api). This needs to be parsed in two steps:

    1. Display PTV stops in the selected area
    2. Parse the text descriptions in the disruption data to correlate them with nearby stops (as disruption data does not provide geographical data)

## The Team

* Andrey Pakhomov – Project management and media
* Rosa Kim – UX design
* Wie Cahya – UI design
* Claudine Chionh – Data discovery and development
* Cin Khant – Data discovery and development
