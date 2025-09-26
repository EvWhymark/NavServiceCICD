import csv

# Tags we care about in OTHER_SERVICES
SERVICE_TAGS = {
    "AVNCS", "GLD", "INSTR", "PAJA", "RNTL", "SALES",
    "SURV", "SLF_SVC", "SLF_SVC_24", "TOW"
}

def format_airport_name(name):
    """Convert airport name to title case, preserving single-letter abbreviations."""
    parts = name.split()
    formatted_parts = [p if len(p) == 1 else p.capitalize() for p in parts]
    return " ".join(formatted_parts)

def filter_services(service_str):
    """Keep only the allowed tags from OTHER_SERVICES."""
    if not service_str:
        return ""
    # Split on comma, then split each tag on '=' to discard descriptions
    tags = [s.split('=')[0].strip() for s in service_str.split(',')]
    filtered = [t for t in tags if t in SERVICE_TAGS]
    return ", ".join(filtered)

def parse_csv(input_file="APT_BASE.csv", airports1_file="airports1.csv"):
    keep_columns = [
        "ARPT_ID", "ELEV", "TPA", "DIST_CITY", "PHONE_NO",
        "FUEL_TYPES", "AIRFRAME_REPAIR_SER_CODE", "PWR_PLANT_REPAIR_SER",
        "BOTTLED_OXY_TYPE", "BULK_OXY_TYPE", "LGT_SKED", "BCN_LGT_SKED",
        "TWR_TYPE_CODE", "BCN_LENS_COLOR", "LNDG_FEE_FLAG",
        "TRNS_STRG_BUOY_FLAG", "TRNS_STRG_HGR_FLAG", "TRNS_STRG_TIE_FLAG",
        "OTHER_SERVICES", "ICAO_ID", "USER_FEE_FLAG", "ARPT_NAME",
        "DIST_CITY_TO_AIRPORT", "LONG_DECIMAL", "LAT_DECIMAL",
    ]

    # Add new column for IAP_EXISTS
    keep_columns.append("IAP_EXISTS")

    # Load airports1.csv into a dictionary mapping ident -> value (1 or 0)
    iap_lookup = {}
    with open(airports1_file, newline='', encoding='utf-8') as f1:
        reader1 = csv.DictReader(f1)
        for row in reader1:
            ident = row["ident"].strip().upper()
            value = row.get("IAP_EXISTS", row.get("iapExists", None))
            if value is not None:
                iap_lookup[ident] = value.strip()  # store 1 or 0 as string

    # Ask user for date string for output
    date_str = input("Enter date (format: month-year, e.g. 8-2025): ").strip()
    output_file = f"APT_BASE_{date_str}.csv"

    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        columns_to_keep = [col for col in keep_columns if col in reader.fieldnames or col == "IAP_EXISTS"]

        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
            writer.writeheader()

            for row in reader:
                # Skip row if ARPT_STATUS is not "O"
                if "ARPT_STATUS" in row and row["ARPT_STATUS"].strip().upper() != "O":
                    continue

                filtered_row = {col: row.get(col, "") for col in columns_to_keep}

                # Format airport name
                if "ARPT_NAME" in filtered_row:
                    filtered_row["ARPT_NAME"] = format_airport_name(filtered_row["ARPT_NAME"])

                # Filter OTHER_SERVICES
                if "OTHER_SERVICES" in filtered_row:
                    filtered_row["OTHER_SERVICES"] = filter_services(filtered_row["OTHER_SERVICES"])

                # Add IAP_EXISTS from airports1.csv if it exists, else null
                filtered_row["IAP_EXISTS"] = iap_lookup.get(row["ARPT_ID"].strip().upper(), "null")

                writer.writerow(filtered_row)

    print(f"Filtered CSV written to: {output_file}")

if __name__ == "__main__":
    parse_csv()
