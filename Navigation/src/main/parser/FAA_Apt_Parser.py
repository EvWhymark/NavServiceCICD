import csv

def parse_csv(input_file="APT_BASE.csv"):
    # Columns we want to keep
    keep_columns = [
        "ARPT_ID", "ELEV", "TPA", "DIST_CITY", "PHONE_NO",
        "FUEL_TYPES", "AIRFRAME_REPAIR_SER_CODE", "PWR_PLANT_REPAIR_SER",
        "BOTTLED_OXY_TYPE", "BULK_OXY_TYPE", "LGT_SKED", "BCN_LGT_SKED",
        "TWR_TYPE_CODE", "BCN_LENS_COLOR", "LNDG_FEE_FLAG",
        "TRNS_STRG_BUOY_FLAG", "TRNS_STRG_HGR_FLAG", "TRNS_STRG_TIE_FLAG",
        "OTHER_SERVICES", "ICAO_ID", "USER_FEE_FLAG", "ARPT_NAME"
    ]

    # Get user input for date
    date_str = input("Enter date (format: month-year, e.g. 8-2025): ").strip()

    # Build output filename
    output_file = f"APT_BASE_{date_str}.csv"

    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Filter only the columns that exist in the file
        columns_to_keep = [col for col in keep_columns if col in reader.fieldnames]

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
            writer.writeheader()

            for row in reader:
                filtered_row = {col: row[col] for col in columns_to_keep}
                writer.writerow(filtered_row)

    print(f"Filtered CSV written to: {output_file}")


if __name__ == "__main__":
    parse_csv()
