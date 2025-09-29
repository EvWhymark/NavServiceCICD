package com.flightIQ.Navigation.Models;

import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;
import org.springframework.data.neo4j.core.schema.Property;
import org.springframework.data.neo4j.core.schema.Relationship;
import org.springframework.data.neo4j.core.schema.Relationship.Direction;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Node("Airport")
public class Airport {

	@Id
	@Property("ident")
	private String ident;

	@Property("icao")
	private String icao;

	@Property("name")
	private String name;

	@Property("latitude")
	private Double latitude;

	@Property("longitude")
	private Double longitude;

	@Property("iapExists")
	private Integer iapExists;

	@Property("elev")
	private Integer elev;

	@Property("tpa")
	private Integer tpa;

	@Property("dist_city")
	private String distCity;

	@Property("phone_no")
	private String phoneNo;

	@Property("fuel_types")
	private String fuelTypes;

	@Property("airframe_repair_ser_code")
	private String airframeRepairSerCode;

	@Property("pwr_plant_repair_ser")
	private String pwrPlantRepairSer;

	@Property("bottled_oxy_type")
	private String bottledOxyType;

	@Property("bulk_oxy_type")
	private String bulkOxyType;

	@Property("lgt_sked")
	private String lgtSked;

	@Property("bcn_lgt_sked")
	private String bcnLgtSked;

	@Property("twr_type_code")
	private String twrTypeCode;

	@Property("bcn_lens_color")
	private String bcnLensColor;

	@Property("lndg_fee_flag")
	private Boolean lndgFeeFlag;

	@Property("trns_strg_buoy_flag")
	private Boolean trnsStrgBuoyFlag;

	@Property("trns_strg_hgr_flag")
	private Boolean trnsStrgHgrFlag;

	@Property("trns_strg_tie_flag")
	private Boolean trnsStrgTieFlag;

	@Property("other_services")
	private String otherServices;

	@Property("user_fee_flag")
	private Boolean userFeeFlag;

	@Property("dist_city_to_airport")
	private Integer distCityToAirport;

	//	@Relationship(type="HAS_DEPARTURE_FIX", direction=Direction.OUTGOING)
	//	private List<FIXX> departureFixxes = new ArrayList<>();
	//
	//	@Relationship(type="HAS_ARRIVAL_FIX", direction=Direction.OUTGOING)
	//	private List<FIXX> arrivalFixxes = new ArrayList<>();

	@Override
	public String toString() {
		return "Airport{" +
				"ident='" + ident + '\'' +
				", icao='" + icao + '\'' +
				", name='" + name + '\'' +
				", latitude=" + latitude +
				", longitude=" + longitude +
				", iapExists=" + iapExists +
				", elev=" + elev +
				", tpa=" + tpa +
				", distCity='" + distCity + '\'' +
				", phoneNo='" + phoneNo + '\'' +
				", fuelTypes='" + fuelTypes + '\'' +
				", airframeRepairSerCode='" + airframeRepairSerCode + '\'' +
				", pwrPlantRepairSer='" + pwrPlantRepairSer + '\'' +
				", bottledOxyType='" + bottledOxyType + '\'' +
				", bulkOxyType='" + bulkOxyType + '\'' +
				", lgtSked='" + lgtSked + '\'' +
				", bcnLgtSked='" + bcnLgtSked + '\'' +
				", twrTypeCode='" + twrTypeCode + '\'' +
				", bcnLensColor='" + bcnLensColor + '\'' +
				", lndgFeeFlag=" + lndgFeeFlag +
				", trnsStrgBuoyFlag=" + trnsStrgBuoyFlag +
				", trnsStrgHgrFlag=" + trnsStrgHgrFlag +
				", trnsStrgTieFlag=" + trnsStrgTieFlag +
				", otherServices='" + otherServices + '\'' +
				", userFeeFlag=" + userFeeFlag +
				", distCityToAirport=" + distCityToAirport +
				'}';
	}
}
