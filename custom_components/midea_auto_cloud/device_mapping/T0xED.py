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
                "input_temperature_sensing": {
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
    }
}
