from datetime import datetime
from enum import Enum
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T", bound=BaseModel)


class TimeStep(str, Enum):
    MINUTELY = "1m"
    HOURLY = "1h"
    DAILY = "1d"


class Units(str, Enum):
    METRIC = "metric"
    IMPERIAL = "imperial"


class Location(BaseModel):
    lat: float
    lon: float
    name: str
    type: str


class HourlyValues(BaseModel):
    cloud_base: Optional[float] = Field(default=0, alias="cloudBase")
    cloud_ceiling: Optional[float] = Field(default=0, alias="cloudCeiling")
    cloud_cover: float = Field(default=0, alias="cloudCover")
    dew_point: float = Field(default=0, alias="dewPoint")
    evapotranspiration: float = Field(default=0)
    freezing_rain_intensity: float = Field(default=0, alias="freezingRainIntensity")
    humidity: float = Field(default=0)
    ice_accumulation: float = Field(default=0, alias="iceAccumulation")
    ice_accumulation_lwe: float = Field(default=0, alias="iceAccumulationLwe")
    precipitation_probability: float = Field(default=0, alias="precipitationProbability")
    pressure_surface_level: float = Field(default=0, alias="pressureSurfaceLevel")
    rain_accumulation: float = Field(default=0, alias="rainAccumulation")
    rain_accumulation_lwe: float = Field(default=0, alias="rainAccumulationLwe")
    rain_intensity: float = Field(default=0, alias="rainIntensity")
    sleet_accumulation: float = Field(default=0, alias="sleetAccumulation")
    sleet_accumulation_lwe: float = Field(default=0, alias="sleetAccumulationLwe")
    sleet_intensity: float = Field(default=0, alias="sleetIntensity")
    snow_accumulation: float = Field(default=0, alias="snowAccumulation")
    snow_accumulation_lwe: float = Field(default=0, alias="snowAccumulationLwe")
    snow_intensity: float = Field(default=0, alias="snowIntensity")
    temperature: float = Field(default=0)
    temperature_apparent: float = Field(default=0, alias="temperatureApparent")
    uv_health_concern: int = Field(default=0, alias="uvHealthConcern")
    uv_index: int = Field(default=0, alias="uvIndex")
    visibility: float = Field(default=0)
    weather_code: int = Field(default=0, alias="weatherCode")
    wind_direction: float = Field(default=0, alias="windDirection")
    wind_gust: float = Field(default=0, alias="windGust")
    wind_speed: float = Field(default=0, alias="windSpeed")


class DailyValues(BaseModel):
    cloud_base_avg: float = Field(default=0, alias="cloudBaseAvg")
    cloud_base_max: float = Field(default=0, alias="cloudBaseMax")
    cloud_base_min: float = Field(default=0, alias="cloudBaseMin")
    cloud_ceiling_avg: float = Field(default=0, alias="cloudCeilingAvg")
    cloud_ceiling_max: float = Field(default=0, alias="cloudCeilingMax")
    cloud_ceiling_min: float = Field(default=0, alias="cloudCeilingMin")
    cloud_cover_avg: float = Field(default=0, alias="cloudCoverAvg")
    cloud_cover_max: float = Field(default=0, alias="cloudCoverMax")
    cloud_cover_min: float = Field(default=0, alias="cloudCoverMin")
    dew_point_avg: float = Field(default=0, alias="dewPointAvg")
    dew_point_max: float = Field(default=0, alias="dewPointMax")
    dew_point_min: float = Field(default=0, alias="dewPointMin")
    evapotranspiration_avg: float = Field(default=0, alias="evapotranspirationAvg")
    evapotranspiration_max: float = Field(default=0, alias="evapotranspirationMax")
    evapotranspiration_min: float = Field(default=0, alias="evapotranspirationMin")
    evapotranspiration_sum: float = Field(default=0, alias="evapotranspirationSum")
    freezing_rain_intensity_avg: float = Field(default=0, alias="freezingRainIntensityAvg")
    freezing_rain_intensity_max: float = Field(default=0, alias="freezingRainIntensityMax")
    freezing_rain_intensity_min: float = Field(default=0, alias="freezingRainIntensityMin")
    humidity_avg: float = Field(default=0, alias="humidityAvg")
    humidity_max: float = Field(default=0, alias="humidityMax")
    humidity_min: float = Field(default=0, alias="humidityMin")
    ice_accumulation_avg: float = Field(default=0, alias="iceAccumulationAvg")
    ice_accumulation_lwe_avg: float = Field(default=0, alias="iceAccumulationLweAvg")
    ice_accumulation_lwe_max: float = Field(default=0, alias="iceAccumulationLweMax")
    ice_accumulation_lwe_min: float = Field(default=0, alias="iceAccumulationLweMin")
    ice_accumulation_max: float = Field(default=0, alias="iceAccumulationMax")
    ice_accumulation_min: float = Field(default=0, alias="iceAccumulationMin")
    ice_accumulation_sum: float = Field(default=0, alias="iceAccumulationSum")
    moonrise_time: datetime = Field(alias="moonriseTime")
    moonset_time: Optional[datetime] = Field(None, alias="moonsetTime")
    precipitation_probability_avg: float = Field(default=0, alias="precipitationProbabilityAvg")
    precipitation_probability_max: float = Field(default=0, alias="precipitationProbabilityMax")
    precipitation_probability_min: float = Field(default=0, alias="precipitationProbabilityMin")
    pressure_surface_level_avg: float = Field(default=0, alias="pressureSurfaceLevelAvg")
    pressure_surface_level_max: float = Field(default=0, alias="pressureSurfaceLevelMax")
    pressure_surface_level_min: float = Field(default=0, alias="pressureSurfaceLevelMin")
    rain_accumulation_avg: float = Field(default=0, alias="rainAccumulationAvg")
    rain_accumulation_lwe_avg: float = Field(default=0, alias="rainAccumulationLweAvg")
    rain_accumulation_lwe_max: float = Field(default=0, alias="rainAccumulationLweMax")
    rain_accumulation_lwe_min: float = Field(default=0, alias="rainAccumulationLweMin")
    rain_accumulation_max: float = Field(default=0, alias="rainAccumulationMax")
    rain_accumulation_min: float = Field(default=0, alias="rainAccumulationMin")
    rain_accumulation_sum: float = Field(default=0, alias="rainAccumulationSum")
    rain_intensity_avg: float = Field(default=0, alias="rainIntensityAvg")
    rain_intensity_max: float = Field(default=0, alias="rainIntensityMax")
    rain_intensity_min: float = Field(default=0, alias="rainIntensityMin")
    sleet_accumulation_avg: float = Field(default=0, alias="sleetAccumulationAvg")
    sleet_accumulation_lwe_avg: float = Field(default=0, alias="sleetAccumulationLweAvg")
    sleet_accumulation_lwe_max: float = Field(default=0, alias="sleetAccumulationLweMax")
    sleet_accumulation_lwe_min: float = Field(default=0, alias="sleetAccumulationLweMin")
    sleet_accumulation_max: float = Field(default=0, alias="sleetAccumulationMax")
    sleet_accumulation_min: float = Field(default=0, alias="sleetAccumulationMin")
    sleet_intensity_avg: float = Field(default=0, alias="sleetIntensityAvg")
    sleet_intensity_max: float = Field(default=0, alias="sleetIntensityMax")
    sleet_intensity_min: float = Field(default=0, alias="sleetIntensityMin")
    snow_accumulation_avg: float = Field(default=0, alias="snowAccumulationAvg")
    snow_accumulation_lwe_avg: float = Field(default=0, alias="snowAccumulationLweAvg")
    snow_accumulation_lwe_max: float = Field(default=0, alias="snowAccumulationLweMax")
    snow_accumulation_lwe_min: float = Field(default=0, alias="snowAccumulationLweMin")
    snow_accumulation_max: float = Field(default=0, alias="snowAccumulationMax")
    snow_accumulation_min: float = Field(default=0, alias="snowAccumulationMin")
    snow_accumulation_sum: float = Field(default=0, alias="snowAccumulationSum")
    snow_intensity_avg: float = Field(default=0, alias="snowIntensityAvg")
    snow_intensity_max: float = Field(default=0, alias="snowIntensityMax")
    snow_intensity_min: float = Field(default=0, alias="snowIntensityMin")
    sunrise_time: datetime = Field(alias="sunriseTime")
    sunset_time: datetime = Field(alias="sunsetTime")
    temperature_apparent_avg: float = Field(default=0, alias="temperatureApparentAvg")
    temperature_apparent_max: float = Field(default=0, alias="temperatureApparentMax")
    temperature_apparent_min: float = Field(default=0, alias="temperatureApparentMin")
    temperature_avg: float = Field(default=0, alias="temperatureAvg")
    temperature_max: float = Field(default=0, alias="temperatureMax")
    temperature_min: float = Field(default=0, alias="temperatureMin")
    uv_health_concern_avg: int = Field(default=0, alias="uvHealthConcernAvg")
    uv_health_concern_max: int = Field(default=0, alias="uvHealthConcernMax")
    uv_health_concern_min: int = Field(default=0, alias="uvHealthConcernMin")
    uv_index_avg: int = Field(default=0, alias="uvIndexAvg")
    uv_index_max: int = Field(default=0, alias="uvIndexMax")
    uv_index_min: int = Field(default=0, alias="uvIndexMin")
    visibility_avg: float = Field(default=0, alias="visibilityAvg")
    visibility_max: float = Field(default=0, alias="visibilityMax")
    visibility_min: float = Field(default=0, alias="visibilityMin")
    weather_code_max: int = Field(default=0, alias="weatherCodeMax")
    weather_code_min: int = Field(default=0, alias="weatherCodeMin")
    wind_direction_avg: float = Field(default=0, alias="windDirectionAvg")
    wind_gust_avg: float = Field(default=0, alias="windGustAvg")
    wind_gust_max: float = Field(default=0, alias="windGustMax")
    wind_gust_min: float = Field(default=0, alias="windGustMin")
    wind_speed_avg: float = Field(default=0, alias="windSpeedAvg")
    wind_speed_max: float = Field(default=0, alias="windSpeedMax")
    wind_speed_min: float = Field(default=0, alias="windSpeedMin")


class MinutelyValues(BaseModel):
    cloud_base: Optional[float] = Field(default=0, alias="cloudBase")
    cloud_ceiling: Optional[float] = Field(default=0, alias="cloudCeiling")
    cloud_cover: float = Field(default=0, alias="cloudCover")
    dew_point: float = Field(default=0, alias="dewPoint")
    freezing_rain_intensity: float = Field(default=0, alias="freezingRainIntensity")
    humidity: float = Field(default=0)
    precipitation_probability: float = Field(default=0, alias="precipitationProbability")
    pressure_surface_level: float = Field(default=0, alias="pressureSurfaceLevel")
    rain_intensity: float = Field(default=0, alias="rainIntensity")
    sleet_intensity: float = Field(default=0, alias="sleetIntensity")
    snow_intensity: float = Field(default=0, alias="snowIntensity")
    temperature: float = Field(default=0)
    temperature_apparent: float = Field(default=0, alias="temperatureApparent")
    uv_health_concern: int = Field(default=0, alias="uvHealthConcern")
    uv_index: int = Field(default=0, alias="uvIndex")
    visibility: float = Field(default=0)
    weather_code: int = Field(default=0, alias="weatherCode")
    wind_direction: float = Field(default=0, alias="windDirection")
    wind_gust: float = Field(default=0, alias="windGust")
    wind_speed: float = Field(default=0, alias="windSpeed")


class HourlyData(BaseModel):
    time: datetime
    values: HourlyValues


class DailyData(BaseModel):
    time: datetime
    values: DailyValues


class MinutelyData(BaseModel):
    time: datetime
    values: MinutelyValues


class Timeline(BaseModel):
    minutely: Optional[List[MinutelyData]] = None
    hourly: Optional[List[HourlyData]] = None
    daily: Optional[List[DailyData]] = None


class ForecastResponse(BaseModel):
    timelines: Timeline
    location: Location


class ApiResponse(BaseModel, Generic[T]):
    """Wrapper for API responses that includes rate limits and metadata."""

    correlation_id: str
    data: T
