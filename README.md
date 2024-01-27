# Uber_Taxi_NYC_Project

Uber and Taxi Analysis in NYC
In the dynamic landscape of urban transportation, the emergence of ride-sharing services, notably Uber, has significantly reshaped the way people navigate through cities. A series of articles have emphasized the impact of Uber on the iconic streets of New York City. This project embarks on a comprehensive exploration, not only delving into the transformative impact of Uber's millions of rides but also incorporating the traditional taxi landscape into the narrative.

Utilizing robust methodologies of Exploratory Data Analysis (EDA) and the transformative potential of Extract, Transform, Load (ETL) processes, the main objective is to uncover intricate trends and patterns in both Uber and NYC's taxi influence. By examining the coexistence of these two transportation modes, the objective is to provide a nuanced understanding of their collective influence on New York City's intricate transportation network.

Beyond quantifying shifts in pickup rates, this analysis seeks to shed light on the intricate nuances that shape the urban mobility landscape. By discerning the intricate interplay of Uber and traditional taxis within the city, the goal is to unveil the multifaceted effects these services have on New York City's transportation ecosystem. This holistic approach will contribute to a more comprehensive and nuanced understanding of the evolving dynamics between ride-sharing and traditional taxi services in New York City.

Background, Data and Goal
The articles Uber Is Serving New York’s Outer Boroughs More Than Taxis Are,Public Transit Should Be Uber’s New Best Friend,Uber Is Taking Millions Of Manhattan Rides Away From Taxis, and Is Uber Making NYC Rush-Hour Traffic Worse?,investigates Uber's significant growth and its potential contribution to the city's traffic congestion.

These articles delve into the complex relationship between Uber's expansion, its increasing number of pickups, and the implications for congestion levels in different areas of New York City. Through data analysis and exploration, these articles shed light on how Uber's presence in various boroughs, particularly in Manhattan, has impacted traffic patterns, especially during peak hours.

The investigation aims to utilize data-driven analysis similar to the approaches presented in these articles to further understand the dynamics of Uber's growth and its potential role in influencing traffic congestion within the city.

# Background, Data and Goal
The articles [Uber Is Serving New York’s Outer Boroughs More Than Taxis Are](https://fivethirtyeight.com/features/uber-is-serving-new-yorks-outer-boroughs-more-than-taxis-are/),[Public Transit Should Be Uber’s New Best Friend](https://fivethirtyeight.com/features/public-transit-should-be-ubers-new-best-friend/),[Uber Is Taking Millions Of Manhattan Rides Away From Taxis](https://fivethirtyeight.com/features/uber-is-taking-millions-of-manhattan-rides-away-from-taxis/), and [Is Uber Making NYC Rush-Hour Traffic Worse?](https://fivethirtyeight.com/features/is-uber-making-nyc-rush-hour-traffic-worse/),investigates Uber's significant growth and its potential contribution to the city's traffic congestion.

These articles delve into the complex relationship between Uber's expansion, its increasing number of pickups, and the implications for congestion levels in different areas of New York City. Through data analysis and exploration, these articles shed light on how Uber's presence in various boroughs, particularly in Manhattan, has impacted traffic patterns, especially during peak hours.

The investigation aims to utilize data-driven analysis similar to the approaches presented in these articles to further understand the dynamics of Uber's growth and its potential role in influencing traffic congestion within the city.

## Uber Data
The [data](https://github.com/fivethirtyeight/uber-tlc-foil-response/blob/master/README.md) comprises six different files for the period of April to September 2014,respectively. Each file contains the following columns:

### Uber Pickups Dataset Columns (April-September 2014)

| Header       | Definition                              |
|--------------|-----------------------------------------|
| Date/Time    | The timestamp of the Uber pickup        |
| Lat          | Latitude of the Uber pickup location    |
| Lon          | Longitude of the Uber pickup location   |
| Base         | TLC base company code affiliated        |

Additionally, there's a file named `uber-raw-data-janjune-15.csv.zip`, which, once unzipped, provides data with the following columns:

### Uber Raw Data Columns (January-June 2015)

| Header              | Definition                                      |
|---------------------|-------------------------------------------------|
| Dispatching_base_num| TLC base company code of the dispatching base    |
| Pickup_date         | Timestamp of the Uber pickup                     |
| Affiliated_base_num | TLC base company code affiliated with the pickup |
| locationID          | Pickup location ID affiliated with the pickup 

The TLC base company codes correspond to the following Uber bases:
| Base Code | Base Name    |
|-----------|--------------|
| B02512    | Unter        |
| B02598    | Hinter       |
| B02617    | Weiter       |
| B02682    | Schmecken    |
| B02764    | Danach-NY    |
| B02765    | Grun         |
| B02835    | Dreist       |
| B02836    | Drinnen      |

Lastly, there's a file named `Uber-Jan-Feb-FOIL.csv`, which once unzipped, provides data with the following columns:

###  Uber aggregated trip statistics (January-Febuary 2015)
| Column Name           | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| dispatching_base_number | TLC base company code of the dispatching base |
| date                  | Date corresponding to the data entry, indicating the time of record or collection. |
| active_vehicles       | Count of Uber vehicles actively in operation or available for service on the recorded date. |
| trips                 | Total number of trips completed or undertaken by Uber vehicles affiliated with the specified TLC base on the given date. |

## Taxi Data

The [data](https://data.cityofnewyork.us/browse?Data-Collection_Data-Collection=TLC%20Trip%20Data&sortBy=alpha) represents information from a single file covering the timeframe from April to September 2014. The data has undergone filtering and extraction processes before being exported.

### NYC Taxi Pickups Dataset Columns (April-September 2014)

| Column                  | Definition                                   |
|-------------------------|----------------------------------------------|
| vendorid                | A code indicating the TPEP provider that provided the record.                                       |
| pickup_datetime         | The date and time when the meter was engaged.                                                        |
| dropoff_datetime        | The date and time when the meter was disengaged.                                                    |
| Store_and_fwd_flag      | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor. |
| rate_code               | The final rate code in effect at the end of the trip.                                                |
| Pickup_longitude        | Longitude of the pickup location.                                                                     |
| Pickup_latitude         | Latitude of the pickup location.                                                                      |
| Dropoff_longitude       | Longitude of the dropoff location.                                                                    |
| Dropoff_latitude        | Latitude of the dropoff location.                                                                     |
| Passenger_count         | The number of passengers in the vehicle.                                                            |
| Trip_distance           | The elapsed trip distance in miles reported by the taximeter.                                       |
| Fare_amount             | The time-and-distance fare calculated by the meter.                                                 |
| Extra                   | Miscellaneous extras and surcharges.                                                                |
| MTA_tax                 | Tax that is automatically triggered based on the metered rate in use.                               |
| Tip_amount              | Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.|
| Tolls_amount            | Total amount of all tolls paid in the trip.                                                         |
| Ehail_fee               | Electronic Hail Fee (if applicable).                                                                |
| Improvement_surcharge   | Improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.|
| Total_amount            | The total amount charged to passengers. Does not include cash tips.                                  |
| Payment_type            | A numeric code signifying how the passenger paid for the trip.                                       |
| Trip_type               | A code indicating the type of trip (e.g., street-hail, dispatch).                                   |
                                     
Additionally, there's a file named `2015_Green_Taxi_Trip_Dataq1_q2`, which, once unzipped, provides data with the same columns listed above respectively.


# Project Goal
The primary aim of this project is to:


1. Explore temporal and spatial patterns in Uber and Taxi pickups, investigating correlations across different times of the hour, weekday, and month to discern alignment or divergence between the two modes of transportation.
2. Visualize Uber's growth trends and assess their potential impact on traffic dynamics in diverse areas of New York City.
3. Conduct a comprehensive comparative analysis between Uber and the traditional taxi ecosystem in NYC.
4. Derive actionable insights and recommendations for urban transportation based on the findings from the analysis of Uber and Taxi datasets.
