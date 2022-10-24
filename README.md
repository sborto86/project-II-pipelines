# Comparison of the hotel booking platforms Booking and Agoda
![Booking](./images/booking.png)
![Agoda](./images/agoda.png)
## Basic information:
- Author: Sergi Portolés
- Project II: Ironhack Data Analyst Bootcamp (pipelines)
- Results might be incorporated in the website [Sapore di Cina](https://www.saporedicina.com/english/)
## Sources:
| Source   |      Type      |  Data extracted  |
|----------|:-------------:|------:|
| [Agoda Partners Portal](https://partners.agoda.com/)|  CSV file<sup>1</sup> | Information of all hotels offered in the portal |
| [Booking](https://www.booking.com/) | Web Scrapping | Number of hotels offered in a country, city or region |
|[Bing](https://www.bing.com/)|Web Scrapping|Seacrh for Booking URL for a certain city
| [Rest Countries](https://restcountries.com/) | API | ISO codes and names of the countries |
 
<sup>1</sup> File not provided in the repo
 
## Python libraries used:
 
| Library   |      Use     |
|----------|:-------------:|
| Pandas | Data Frame manipulation |
| Seaborn | Visualization |
| Matplotlib | Visualization |
| Responses | HTTP Calls |
| Bs4 (BeautifulSoup) | HTML manipulation |
| Geopandas | Country map visualization |
|Unidecode | encode to UTF8 cities names|

## Background:
- Booking.com headquarters are located in Amsterdam, Netherlands.
- Agoda headquarters are located in Singapore
- Currently Agoda is a currently a subsidiary of Booking Holdings.
## Objective of the study
- Compare the hotel booking platforms [Booking](https://www.booking.com/) and [Agoda](https://www.agoda.com/)
 
## Limitations of the study
- The impossibility to access to the Booking.com official data (API or Database) have forced to use web scrapping, this method might under-represent the number of hotels and locations for this platform
- This is a quantitative (number of hotels) not qualitative (prices) due to the lack of easy access to Booking.com data.
- The number of hotels are not filtered by type of accomodation and include hotels, apartments, villas and other types, again accessing booking source data is needed to filter the type of accomodation 

## Results
### Total Number of Hotels Globally
![Total Number of Hotels](./images/total_graph.png)
### Total Number of Hotels by Region
![World Regions](./images/regions_graph.png)
### Top Countries in Booking with more Hotels
![Booking Top 10 Countries](./images/cbooking_graph.png)
### Top Countries in Agoda with more Hotels
![Agoda Top10 Countries](./images/cagoda_graph.png)
### Asia
#### Taiwan
![Taiwan Hotels](./images/taiwan_comp.png)
#### Thailand
![Thailand Hotels](./images/thailand_comp.png)
#### China
![China Agoda Hotels](./images/china_agoda.png)
![China Booking Hotels](./images/china_booking.png)
### Europe
#### Croatia
![Croatia Hotels](./images/croatia.png)
#### Spain
![Spain Hotels](./images/spain.png)

## Results:
- Booking has a more significant number of hotels listed globally
- Booking has more hotels listed in all regions except in Asia
- The region with most hotels listed in Booking is Europe where the headquarters are localized
- The region with more hotels listed in Agoda is Asia where the headquarters are localized
- Created an application to compare Agoda and Booking total number of hotels in any country by cities and plot the results geographically