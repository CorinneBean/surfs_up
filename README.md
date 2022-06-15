# Surfs_up Challenge
 
## Overview of  the statistical analysis
The purpose of this project was to review data related to temperature for the months of June and December in Oahu, Hawaii. This data will be used by a local surf shop to determine weather trends prior to opening.

Steps taken to complete the analysis:
1. Filter the date column of the Measurements table using Python, Pandas and SQLAlchemy in the hawaii.sqlite database to retrieve all the temperatures for the month of June. The temperatures will then be converted to a list in order to create a Dataframe from the list which will then be used to generate the summary statistics.

2. Filter the date column of the Measurements table using Python, Pandas and SQLAlchemy in the [hawaii.sqlite](https://github.com/CorinneBean/surfs_up/blob/28a3a5e360f3189a7d0a167f9c93462e367e6e79/hawaii.sqlite) database to retrieve all the temperatures for the month of December. The temperatures will then be converted to a list in order to create a Dataframe from the list which will then be used to generate the summary statistics.

3. Review the results of the analysis and compile a report of the findings.

## Results
On inital review of the data it is clear to see that the weather in Oahu is pretty consistent throughout the year. However, there are a few slight differences.

Three Key Differences between weather in June and December
- There was more temperature reading data to review for June (1700) vs December (1517) 
- Max temperature recorded in June was 85 vs 83 in December.
- The minimum temperature in June was 64 vs 56 in December.

June Weather Data:
![June Weather Data](https://github.com/CorinneBean/surfs_up/blob/865804053acf6295b9a35000b63204a251aa91b5/Resources/June%20Weather.png "June Weather Data")
December Weather Data:
![December Weather Data](https://github.com/CorinneBean/surfs_up/blob/865804053acf6295b9a35000b63204a251aa91b5/Resources/December%20Weather.png "December Weather Data")

## Summary
The data reviewed gave us a general understanding of what the weather would be like in the months of June and December. While this information is generally helpful to the shop owner to determine if they should open their shop in Oahu. It doesn't provide a full picture and additional queries would be recommended to look at different weather conditions during that time frame. Weather conditions such as precipitation can affect customer traffic so this would be important information to review. 