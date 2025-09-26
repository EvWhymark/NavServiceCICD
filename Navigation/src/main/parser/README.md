## FAA NASR Data Parser

Data is updated monthly by the FAA here:
https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/

After downloading your desired dataset you will need to extract it. 
We do not need to extract the entire dataset. All we need is the APT_BASE.csv.
On top of that we require you have the airports1.csv file. This should be on the repo.

## Reading the dataset

If the terms are not familiar to you or need help reading what the tags mean
use this resource: https://www.faa.gov/documentLibrary/media/Advisory_Circular/arp-aas-amr-data-dictionary-2024-08.pdf

## Running the parser
Just run the python code however you want (terminal/IDE).
When you run the program it will query you for a date to be used
with the file name. The format for this is month-year. For example
09-2025 for september 2025. This date should correspond to when you
got the data set from the FAA dataset.




## Cypher Query

```
// Step 1: Delete all existing Airport nodes
MATCH (a:Airport)
DETACH DELETE a;

// Step 2: Load new data and create Airport nodes
LOAD CSV WITH HEADERS FROM 'file:///APT_BASE_09-2025.csv' AS row
CREATE (a:Airport {
    ident: row.ARPT_ID,
    elev: row.ELEV,
    tpa: row.TPA,
    dist_city: row.DIST_CITY,
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
    lndg_fee_flag: row.LNDG_FEE_FLAG,
    trns_strg_buoy_flag: row.TRNS_STRG_BUOY_FLAG,
    trns_strg_hgr_flag: row.TRNS_STRG_HGR_FLAG,
    trns_strg_tie_flag: row.TRNS_STRG_TIE_FLAG,
    other_services: row.OTHER_SERVICES,
    icao: row.ICAO_ID,
    user_fee_flag: row.USER_FEE_FLAG,
    name: row.ARPT_NAME,
    dist_city_to_airport: row.DIST_CITY_TO_AIRPORT,
    longitude: row.LONG_DECIMAL,
    latitude: row.LAT_DECIMAL,
    iapExists: row.IAP_EXISTS
});
```
