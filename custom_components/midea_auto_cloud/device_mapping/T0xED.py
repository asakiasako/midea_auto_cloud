from homeassistant.const import Platform, UnitOfTemperature, UnitOfTime, UnitOfElectricPotential, \
    UnitOfVolume, UnitOfMass
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.switch import SwitchDeviceClass

DEVICE_MAPPING = {
    "default": {
        "rationale": ["off", "on"],
        "queries": [{}],
        "centralized": [],
        "entities": {
            Platform.SWITCH: {
                "power": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "heat": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "antifreeze": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "lock": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "sleep": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "keep_warm": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "vacation": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "germicidal": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "lack_water": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "drainage": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "wash_enable": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "water_way": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "soften": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "regeneration": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "maintenance_reminder_switch": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "leak_water_protection": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "micro_leak_protection": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "cl_sterilization": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "holiday_mode": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
            },
            Platform.BINARY_SENSOR: {
                "heat_status": {
                    "device_class": BinarySensorDeviceClass.RUNNING,
                },
                "standby_status": {
                    "device_class": BinarySensorDeviceClass.RUNNING,
                },
                "chlorine_sterilization_error": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "rtc_error": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "low_salt": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "no_salt": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "low_battery": {
                    "device_class": BinarySensorDeviceClass.BATTERY,
                },
                "flowmeter_error": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "salt_level_sensor_error": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "leak_water": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "micro_leak": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                },
                "maintenance_remind": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                }
            },
            Platform.SENSOR: {
                "current_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "input_temperature_Sensing": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "input_temperature_sensing"
                },
                "hot_pot_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "cool_target_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "water_consumption_ml": {
                    "device_class": SensorDeviceClass.VOLUME,
                    "unit_of_measurement": UnitOfVolume.LITERS,
                    "state_class": SensorStateClass.TOTAL_INCREASING
                },
                "keep_warm_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "warm_left_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "salt_alarm_threshold": {
                    "device_class": SensorDeviceClass.WEIGHT,
                    "unit_of_measurement": UnitOfMass.KILOGRAMS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "left_salt": {
                    "device_class": SensorDeviceClass.BATTERY,
                    "unit_of_measurement": "%",
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "salt_setting": {
                    "device_class": SensorDeviceClass.WEIGHT,
                    "unit_of_measurement": UnitOfMass.KILOGRAMS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "supply_voltage": {
                    "device_class": SensorDeviceClass.VOLTAGE,
                    "unit_of_measurement": UnitOfElectricPotential.VOLT,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "battery_voltage": {
                    "device_class": SensorDeviceClass.VOLTAGE,
                    "unit_of_measurement": UnitOfElectricPotential.VOLT,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "water_hardness": {
                    "device_class": SensorDeviceClass.WATER,
                    "unit_of_measurement": "mg/L",
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "water_consumption_big": {
                    "device_class": SensorDeviceClass.VOLUME,
                    "unit_of_measurement": UnitOfVolume.LITERS,
                    "state_class": SensorStateClass.TOTAL_INCREASING
                },
                "water_consumption_today": {
                    "device_class": SensorDeviceClass.VOLUME,
                    "unit_of_measurement": UnitOfVolume.LITERS,
                    "state_class": SensorStateClass.TOTAL_INCREASING
                },
                "water_consumption_average": {
                    "device_class": SensorDeviceClass.VOLUME,
                    "unit_of_measurement": UnitOfVolume.LITERS,
                    "state_class": SensorStateClass.TOTAL_INCREASING
                },
                "soft_available_big": {
                    "device_class": SensorDeviceClass.VOLUME,
                    "unit_of_measurement": UnitOfVolume.LITERS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "regeneration_left_seconds": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.SECONDS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "heat_start": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "regeneration_stages": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "regeneration_current_stages": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "regeneration_count": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "days_since_last_regeneration": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "days_since_last_two_regeneration": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "use_days": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.TOTAL_INCREASING
                },
                "flushing_days": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "pre_regeneration_days": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "remind_maintenance_days": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "maintenance_reminder_setting": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "micro_leak_protection_value": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "leak_water_protection_value": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "mixed_water_gear": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "velocity": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "error": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "category": {
                    "device_class": SensorDeviceClass.ENUM,
                },
            }
        }
    },
    "63200872": {
        "rationale": ["off", "on"],
        "queries": [{}],
        "centralized": [],
        "entities": {
            Platform.SWITCH: {
                "drainage": {"device_class": SwitchDeviceClass.SWITCH},
                "wash": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "translation_key": "wash_filter_cartridge"
                },
                "antifreeze": {"device_class": SwitchDeviceClass.SWITCH},
                "smart_no_obsolete_water": {"device_class": SwitchDeviceClass.SWITCH},
                "extreme_mode": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "translation_key": "no_obsolete_water_extreme_mode"
                },
            },
            Platform.BINARY_SENSOR: {
                "power": {"device_class": BinarySensorDeviceClass.POWER},
                "sleep": {"device_class": BinarySensorDeviceClass.RUNNING},
                "standby_status": {"device_class": BinarySensorDeviceClass.RUNNING},
                "domestic_outlet": {"device_class": BinarySensorDeviceClass.RUNNING},
                "out_water": {
                    "device_class": BinarySensorDeviceClass.RUNNING,
                    "translation_key": "drinking_outlet"
                },
                "lack_water": {"device_class": BinarySensorDeviceClass.PROBLEM},
                "full": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                    "translation_key": "water_tank_full"
                }
            },
            Platform.SENSOR: {
                "input_temperature_Sensing": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "input_temperature_sensing"
                },
                "in_tds": {
                    "device_class": SensorDeviceClass.WATER,
                    "unit_of_measurement": "ppm",
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "out_tds": {
                    "device_class": SensorDeviceClass.WATER,
                    "unit_of_measurement": "ppm",
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "life_1": {
                    "unit_of_measurement": "%",
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "filter_life_1"
                },
                "life_2": {
                    "unit_of_measurement": "%",
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "filter_life_2"
                },
                "maxlife_1": {
                    "unit_of_measurement": "months",
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "filter_max_life_1"
                },
                "maxlife_2": {
                    "unit_of_measurement": "months",
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "filter_max_life_2"
                },
                "water_consumption": {
                    "device_class": SensorDeviceClass.VOLUME,
                    "unit_of_measurement": "ml",
                    "state_class": SensorStateClass.TOTAL_INCREASING
                },
                "error": {
                    "device_class": SensorDeviceClass.ENUM
                }
            }
        }
    },
    "63200867": {
        "rationale": ["off", "on"],
        "queries": [{}],
        "centralized": [],
        "entities": {
            Platform.SWITCH: {
                "lock": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "translation_key": "child_lock"
                },
                "germicidal": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "translation_key": "high_temperature_germicidal"
                },
                "drainage": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "translation_key": "automatic_drainage"
                },
                "human_sensing_switch": {"device_class": SwitchDeviceClass.SWITCH},
                "set_germicidal_countdown": {"device_class": SwitchDeviceClass.SWITCH},
            },
            Platform.BINARY_SENSOR: {
                "lack_water": {
                    "device_class": BinarySensorDeviceClass.RUNNING,
                    "translation_key": "refilling_water"
                },
                "out_water": {"device_class": BinarySensorDeviceClass.RUNNING},
                "sleep": {"device_class": BinarySensorDeviceClass.RUNNING},
                "standby_status": {"device_class": BinarySensorDeviceClass.RUNNING},
            },
            Platform.SENSOR: {
                "current_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "germicidal_countdown": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.DAYS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "germicidal_left_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "water_consumption": {
                    "device_class": SensorDeviceClass.VOLUME,
                    "unit_of_measurement": "ml",
                    "state_class": SensorStateClass.TOTAL_INCREASING
                },
                "error": {"device_class": SensorDeviceClass.ENUM},
            },
            Platform.SELECT: {
                # Current quantification mode: 0 continuous flow, 1 small volume, 2 medium volume, 3 large volume
                "cur_quantify": {
                    "options": {
                        "0": {"cur_quantify": 0},
                        "1": {"cur_quantify": 1},
                        "2": {"cur_quantify": 2},
                        "3": {"cur_quantify": 3},
                    },
                    "translation_key": "cur_quantify_mode"
                },
                # Quantify 1: 50–300 ml, step 50 ml (internal unit = 10 ml, attribute value = displayed_value/10)
                "quantify_1": {
                    "options": {
                        "50ml": {"quantify_1": 5},
                        "100ml": {"quantify_1": 10},
                        "150ml": {"quantify_1": 15},
                        "200ml": {"quantify_1": 20},
                        "250ml": {"quantify_1": 25},
                        "300ml": {"quantify_1": 30},
                    }
                },
                # Quantify 2: 150–500 ml, step 50 ml
                "quantify_2": {
                    "options": {
                        "150ml": {"quantify_2": 15},
                        "200ml": {"quantify_2": 20},
                        "250ml": {"quantify_2": 25},
                        "300ml": {"quantify_2": 30},
                        "350ml": {"quantify_2": 35},
                        "400ml": {"quantify_2": 40},
                        "450ml": {"quantify_2": 45},
                        "500ml": {"quantify_2": 50},
                    }
                },
                # Quantify 3: 300–700 ml, step 50 ml
                "quantify_3": {
                    "options": {
                        "300ml": {"quantify_3": 30},
                        "350ml": {"quantify_3": 35},
                        "400ml": {"quantify_3": 40},
                        "450ml": {"quantify_3": 45},
                        "500ml": {"quantify_3": 50},
                        "550ml": {"quantify_3": 55},
                        "600ml": {"quantify_3": 60},
                        "650ml": {"quantify_3": 65},
                        "700ml": {"quantify_3": 70},
                    }
                },
                "custom_temperature_1": {
                    "options": {
                        "35°C": {"custom_temperature_1": 35},
                        "40°C": {"custom_temperature_1": 40},
                        "45°C": {"custom_temperature_1": 45},
                        "50°C": {"custom_temperature_1": 50},
                        "55°C": {"custom_temperature_1": 55},
                        "60°C": {"custom_temperature_1": 60},
                        "65°C": {"custom_temperature_1": 65},
                        "70°C": {"custom_temperature_1": 70},
                        "75°C": {"custom_temperature_1": 75},
                        "80°C": {"custom_temperature_1": 80},
                        "85°C": {"custom_temperature_1": 85},
                        "90°C": {"custom_temperature_1": 90},
                        "95°C": {"custom_temperature_1": 95},
                    },
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "device_class": SensorDeviceClass.TEMPERATURE
                },
                # Settable germicidal countdown days: 7,10,15,20,25,30
                "set_germicidal_countdown_days": {
                    "options": {
                        "7": {"set_germicidal_countdown_days": 7},
                        "10": {"set_germicidal_countdown_days": 10},
                        "15": {"set_germicidal_countdown_days": 15},
                        "20": {"set_germicidal_countdown_days": 20},
                        "25": {"set_germicidal_countdown_days": 25},
                        "30": {"set_germicidal_countdown_days": 30},
                    }
                },
                # Screen off time: 10s,30s,1m,2m,3m,5m (stored as seconds)
                "screenout_time": {
                    "options": {
                        "10s": {"screenout_time": 10},
                        "30s": {"screenout_time": 30},
                        "1m": {"screenout_time": 60},
                        "2m": {"screenout_time": 120},
                        "3m": {"screenout_time": 180},
                        "5m": {"screenout_time": 300},
                    }
                },
            }
        }
    }
}
