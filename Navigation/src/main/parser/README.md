## FAA NASR Data Parser

Data is updated monthly by the FAA here:
https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/

After downloading your desired dataset you will need to extract it. 
We do not need to extract the entire dataset. All we need is the APT_BASE.csv.
On top of that we require you have the airports1.csv file. This should be on the repo.
These files should be placed inside the ./parser folder.

## Running the parser
Just run the python code however you want (terminal/IDE).
When you run the program it will query you for a date to be used
with the file name. The format for this is month-year. For example
09-2025 for september 2025. This date should correspond to when you
got the data set from the FAA dataset. In the Cypher query below I
am using the 09-2025 dataset as an example. This line:  
LOAD CSV WITH HEADERS FROM 'file:///APT_BASE_09-2025.csv' AS row  
will need to be modified accordingly to what you set the file name to.



## Cypher Query

```
// Step 1: Delete all existing Airport nodes
MATCH (a:Airport)
DETACH DELETE a;

// Step 2: Load new data and create Airport nodes
LOAD CSV WITH HEADERS FROM 'file:///APT_BASE_09-2025.csv' AS row
CREATE (a:Airport {
    ident: row.ARPT_ID,
    elev: CASE WHEN row.ELEV = '' THEN null ELSE toInteger(row.ELEV) END,
    tpa: CASE WHEN row.TPA = '' THEN null ELSE toInteger(row.TPA) END,
    phone_no: row.PHONE_NO,
    fuel_types: row.FUEL_TYPES,
    airframe_repair_ser_code: row.AIRFRAME_REPAIR_SER_CODE,
    pwr_plant_repair_ser: row.PWR_PLANT_REPAIR_SER,
    bottled_oxy_type: row.BOTTLED_OXY_TYPE,
    bulk_oxy_type: row.BULK_OXY_TYPE,
    lgt_sked: row.LGT_SKED,
    bcn_lgt_sked: row.BCN_LGT_SKED,
    twr_type_code: row.TWR_TYPE_CODE,
    bcn_lens_color: row.BCN_LENS_COLOR,
    lndg_fee_flag: CASE WHEN row.LNDG_FEE_FLAG = '' THEN null ELSE toBoolean(row.LNDG_FEE_FLAG) END,
    trns_strg_buoy_flag: CASE WHEN row.TRNS_STRG_BUOY_FLAG = '' THEN null ELSE toBoolean(row.TRNS_STRG_BUOY_FLAG) END,
    trns_strg_hgr_flag: CASE WHEN row.TRNS_STRG_HGR_FLAG = '' THEN null ELSE toBoolean(row.TRNS_STRG_HGR_FLAG) END,
    trns_strg_tie_flag: CASE WHEN row.TRNS_STRG_TIE_FLAG = '' THEN null ELSE toBoolean(row.TRNS_STRG_TIE_FLAG) END,
    other_services: row.OTHER_SERVICES,
    icao: row.ICAO_ID,
    name: row.ARPT_NAME,
    dist_city_to_airport: CASE WHEN row.DIST_CITY_TO_AIRPORT = '' THEN null ELSE toInteger(row.DIST_CITY_TO_AIRPORT) END,
    longitude: CASE WHEN row.LONG_DECIMAL = '' THEN null ELSE toFloat(row.LONG_DECIMAL) END,
    latitude: CASE WHEN row.LAT_DECIMAL = '' THEN null ELSE toFloat(row.LAT_DECIMAL) END,
    iapExists: CASE WHEN row.IAP_EXISTS = '' THEN null ELSE toInteger(row.IAP_EXISTS) END
});
```

## Dictionary
The values names are not necessarily self-explanatory. I will
list what all the values stand for in the database. If any value is null
assume the value is false/null/no. The reference for this dictionary is here:
https://www.faa.gov/documentLibrary/media/Advisory_Circular/arp-aas-amr-data-dictionary-2024-08.pdf

| Field                    | What it stand for                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------|
| ident                    | Airport Identifier (3 Characters)                                                                     |
| elev                     | elevation (in feet)                                                                                   |
| TPA                      | Traffic Pattern Altitude (in feet)                                                                    |
| phone_no                 | Airport Phone number                                                                                  |
| Fuel types               | Fuel offered at the airport (See doc for specific types of fuel)                                      |
| airframe_repair_ser_code | Type of airframe repair offered at the airport (Either major, minor, none)                            |
| pwr_plant_repair_ser     | Types of power plant repair available at the airport (Either major, minor, none)                      |
| bottled_oxy_type         | Type of bottle oxygen available for sale to general public (Either high or Low)                       |
| bulk_oxy_type            | Type of bulk storage oxygen available to general public (Eihter high or low)                          |
| lgt_sked                 | Lighting Schedule (Either see remark or SS-SR (Sunset to Sunrise))                                    |
| bcn_lgt_sked             | Beacon Lighting Schedule (Either see remark or SS-SR (Sunset to Sunrise)                              |
| twr_type_code            | Either ATCT (Air Traffic Control Tower) or NON-ATCT                                                   |
| bcn_lens_color           | See Doc for specific colors                                                                           |
| lndg_fee_flag            | If landing fee is charged to non-commercial users of the airport                                      |
| trns_strg_buoy_flag      | If Buoy storage type is available (Either Yes or No)                                                  |
| trns_strg_hgr_flag       | If hangar storage type is available (Either Yes or No)                                                |
| trns_strg_tie_flag       | If tie down storage type is available (Either Yes or No)                                              |
| other_services           | A variety of other services available at the airport. See other services section                      |
| icao                     | Airport ICAO code                                                                                     |
| name                     | Full airport name                                                                                     |
| dist_city_to_airport     | Distance from city to airport (In miles)                                                              |
| longitude                | Longitude (8 decimal points)                                                                          |
| latitude                 | Latitude (8 decimal points)                                                                           |
| iapExists                | If an instrument approach exists. A bunch of airports are missing this data                           |


## Other Services
Other services is a vague tag that the FAA assigns. This can relate to a
bunch of different tags for airports. In the parser we are removing
some unnecessary tags. These tags will be listed in the other services key in the response.
Here are the list of the current tags we support and what they mean:

AVNCS = Avionics  
GLD = Glider  
INSTR = Flight Instruction  
PAJA = Parachute Jumping  
RNTL = Aircraft Rental  
SALES = Aircraft Dealer  
SURV = Aerial Surveying  
SLF_SVC = Self-Serve  
SLF_SVC_24 = Self-Serve Available 24 HRs  
TOW = Glider Towing  
