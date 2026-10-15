# Gilgit-Baltistan Historical Weather Dataset

A 35-year daily weather dataset (1990 to 2024) for Gilgit-Baltistan, Pakistan, sourced from ERA5 reanalysis and bias-corrected for the known ERA5 discontinuity between December 2016 and January 2017 before any analysis.

![Period](https://img.shields.io/badge/Period-1990_to_2024-1f6feb)
![Stations](https://img.shields.io/badge/Stations-5_of_8-2ea043)
![Source](https://img.shields.io/badge/Source-ERA5_via_Open__Meteo-8957e5)
![Variables](https://img.shields.io/badge/Daily_variables-25-f0883e)
![License](https://img.shields.io/badge/License-CC_BY_4.0-a371f7)

The data comes from the Open-Meteo Historical Archive API, which serves ERA5 reanalysis produced by ECMWF. The repository ships the full pipeline: download, bias correction, trend analysis, and reporting.

> **Update, October 2026.** Earlier versions placed the ERA5 break at 1 January 2016. The step actually happens between December 2016 and January 2017, so 2016 was left uncorrected and read 4 to 5 C too cold at most stations. The break is now 1 January 2017, every corrected file and chart has been regenerated, and the findings below have been recomputed. The `era5_period` column now reads `pre_2017` / `post_2017`. If you downloaded the data before this date, download it again. See [Changelog](#changelog).

## Climate Change Report

<p align="center">
  <img src="GB_Climate_Report.png" alt="Gilgit-Baltistan Climate Change Report 1990 to 2024" width="100%">
</p>

## Key Findings at a Glance

| Metric | Corrected data | Raw data claimed |
|---|---|---|
| Warming rate, 1990 to 2024 | +0.08 C per decade (a lower bound, see below) | +1.42 C per decade |
| Warming rate, 1990 to 2016 (no break inside) | +0.14 C per decade | not applicable |
| Rainfall, 1990 to 2016 | Down at all 5 stations, 1 to 9 percent per decade | not applicable |
| Snowfall below 2,500 m, 1990s to 2010-16 | Down 12 to 18 percent | not applicable |
| Fastest warming | Gilgit and Chilas | not applicable |
| Most stable | Khunjerab (4693 m) | not applicable |

### Why the raw data was wrong: 16 times too much warming

<p align="center">
  <img src="chart3_fake_vs_real.png" alt="What the model was told versus what is actually happening" width="95%">
</p>

A linear trend on the raw ERA5 data reports +1.42 C per decade of warming for Gilgit-Baltistan. After correcting the discontinuity, the trend is +0.08 C per decade, so the raw number was about 17 times too high. The red bars are a data artefact.

The corrected number should be read as a lower bound. The correction matches each month's average before and after 2017, which removes the artificial step but also any real change between the two periods. The cleanest estimate comes from 1990 to 2016, a stretch with no break inside it: +0.14 C per decade on average.

## Temperature and Snow: the corrected picture

<table>
<tr>
<td width="50%"><img src="clean_temperature.png" alt="Corrected temperature trend" width="100%"></td>
<td width="50%"><img src="chart5_rain_snow.png" alt="Rain replacing snow at lower elevations" width="100%"></td>
</tr>
<tr>
<td align="center"><em>Warming is modest. In this record the low valleys (Gilgit, Chilas) warm faster than the high stations.</em></td>
<td align="center"><em>Snowfall fell 12 to 18 percent below 2,500 m from the 1990s to 2010-16. Rain shows no consistent change, so this is less snow, not snow turning into rain.</em></td>
</tr>
</table>

## The ERA5 2016/2017 Problem

ERA5 reanalysis has a systematic discontinuity between December 2016 and January 2017, linked to changes in the ECMWF data assimilation system and satellite input streams. Over complex mountain terrain like Gilgit-Baltistan this creates a hard step change, not a real climate signal.

<p align="center">
  <img src="chart1_problem.png" alt="The 2017 jump in raw ERA5 data" width="95%">
</p>

What it looked like in raw data:

Average step in mean temperature at the break (all 12 monthly corrections averaged; winter steps are larger, up to +9.9 C at Gilgit in January):

| Station | Step at January 2017 |
|---|---|
| Skardu | +6.6 C |
| Gilgit | +6.4 C |
| Chilas | +5.2 C |
| Hunza | +4.9 C |
| Khunjerab | -0.7 C |

<table>
<tr>
<td width="50%"><img src="bias_heatmap.png" alt="Bias correction heatmap by station and month" width="100%"></td>
<td width="50%"><img src="clean_jump_proof.png" alt="Before and after proof the 2017 jump is removed" width="100%"></td>
</tr>
<tr>
<td align="center"><em>Monthly correction factors applied per station and variable.</em></td>
<td align="center"><em>The artificial step at 2017 is gone after correction.</em></td>
</tr>
</table>

## Stations

| Station | District | Elevation | Latitude | Longitude | Status |
|---|---|---|---|---|---|
| Gilgit | Gilgit | 1500 m | 35.9208 | 74.3083 | Downloaded |
| Skardu | Skardu-Baltistan | 2228 m | 35.2971 | 75.6875 | Downloaded |
| Hunza | Hunza | 2438 m | 36.3167 | 74.6500 | Downloaded |
| Chilas | Diamer | 1250 m | 35.4167 | 74.1000 | Downloaded |
| Khunjerab | Hunza | 4693 m | 36.8333 | 75.4167 | Downloaded |
| Astore | Astore | 2168 m | 35.3667 | 74.9167 | Rate-limited, retry needed |
| Gupis | Ghizer | 2156 m | 36.1667 | 73.4000 | Rate-limited, retry needed |
| Bunji | Astore | 760 m | 35.6500 | 74.6333 | Rate-limited, retry needed |

## Variables (25 daily)

| Category | Variables |
|---|---|
| Temperature | temperature_2m_max, temperature_2m_min, temperature_2m_mean, apparent_temperature_max, apparent_temperature_min, apparent_temperature_mean |
| Precipitation | precipitation_sum, rain_sum, snowfall_sum, precipitation_hours |
| Wind | wind_speed_10m_max, wind_speed_10m_mean, wind_gusts_10m_max, wind_direction_10m_dominant |
| Solar | shortwave_radiation_sum, et0_fao_evapotranspiration, uv_index_max, sunshine_duration, daylight_duration |
| Sky | cloud_cover_mean, weather_code |
| Astronomical | sunrise, sunset |

## Bias Correction Method

Monthly Delta Bias Correction, applied per station and per variable.

Rows before 1 January 2017 are shifted onto the 2017 to 2024 baseline.

For additive variables (temperature, wind, radiation):
```
delta(month)  = mean_post(month) - mean_pre(month)
corrected_pre = raw_pre + delta(month)
```

For multiplicative variables (precipitation, snowfall):
```
ratio(month)  = mean_post(month) / mean_pre(month)
corrected_pre = raw_pre * ratio(month)
```

Monthly factors are used instead of a single annual factor because one annual number would fix one season while breaking another. Monthly deltas correct each season independently and preserve seasonality.

What the method cannot do:
- It removes real change across the break along with the artefact, so trends that span 2017 are conservative, and any before-versus-after-2017 comparison on corrected data is mostly set by the correction itself. Compare periods within 1990 to 2016 instead.
- It corrects means, not the shape of the distribution, so extremes may still carry some of the old regime.

## Files

| File | Description |
|---|---|
| `fetch_gb_weather.py` | Downloads all station data from the Open-Meteo API |
| `bias_correct.py` | Applies monthly delta bias correction |
| `trend_analysis.py` | Decadal trends plus pre and post 2017 comparison |
| `visualize_clean.py` | Clean, accurate plots (annual aggregation plus 3-year rolling) |
| `simple_charts.py` | Plain-English charts for non-technical readers |
| `report.py` | Generates `GB_Climate_Report.png` |
| `gb_weather_corrected.csv.gz` | Bias-corrected combined dataset. Use this for training |
| `gb_weather_combined.csv.gz` | Raw uncorrected combined dataset |
| `bias_correction_report.json` | Full audit trail of every correction factor applied |
| `<station>_weather.csv` and `<station>_corrected.csv` | Per-station raw and corrected series |

The two combined datasets are stored gzipped because of their size. Decompress with:

```bash
gunzip -k gb_weather_corrected.csv.gz
```

The per-station corrected CSVs are stored uncompressed and can be used directly.

## For Model Training

Use `gb_weather_corrected.csv` (from the gzipped combined file, or concatenate the per-station `*_corrected.csv` files).

Column guidance:
- `bias_corrected = 1` means the row was adjusted (before 2017). Keep it as a feature.
- `era5_period` is `pre_2017` or `post_2017`. Include it as a categorical feature.
- Do not train on `gb_weather_combined.csv`, which contains the uncorrected jump.

Noise reduction used in analysis:
1. Aggregate daily data to annual means.
2. Apply a 3-year rolling mean on the annual series.
3. Fit linear trends via `numpy.polyfit` on the smoothed annual series.

## Key Findings (detail)

Temperature. The corrected 1990 to 2024 trend is +0.08 C per decade, about +0.3 C over 35 years. Because the correction also absorbs real change across 2017, this is a lower bound. Within the clean 1990 to 2016 period the average is +0.14 C per decade, led by Gilgit (+0.34) and Chilas (+0.23), with Skardu, Hunza and Khunjerab close to zero. No single station's trend is statistically significant at the 95 percent level over 27 years, and the low valleys warming fastest runs against the usual finding that high mountains warm faster. Treat station-level numbers from a 9 to 25 km grid with care.

Rainfall. From 1990 to 2016, total precipitation fell at all five stations, by 1 to 9 percent per decade. Only Gilgit's decline (about 9 percent per decade) is statistically clear on its own.

Snowfall. From the 1990s to 2010-16, snowfall fell 12 to 18 percent at the four stations below 2,500 m and 3 percent at Khunjerab. Rain did not rise to compensate, so the loss tracks the overall drop in precipitation rather than snow turning into rain.

Absolute rainfall. ERA5 values describe a grid cell that includes the surrounding mountains, not the valley floor. ERA5 gives Gilgit about 1,430 mm of precipitation a year, while the Gilgit rain gauge records about 130 mm. Use precipitation for relative questions (trends, anomalies, percentiles), not as the amount that fell in town.

## Pending Work

- Re-run `fetch_gb_weather.py` to download Astore, Gupis, and Bunji, which were rate-limited on the first run.
- Re-run `bias_correct.py` after the remaining 3 stations are downloaded.
- Validate against PMD station records for Gilgit, Skardu and Chilas.
- These stations cover the eastern valleys and Ghizer district, with precipitation patterns different from the Karakoram corridor.

## Changelog

**October 2026**
- Moved the ERA5 break from 2016-01-01 to 2017-01-01. 2016 had been left uncorrected and read 4 to 5 C too cold at most stations.
- Regenerated all corrected CSVs, `bias_correction_report.json`, the combined gzip and every chart. Relabelled `era5_period` to `pre_2017` / `post_2017`.
- Recomputed the findings. Warming 1990 to 2024 is +0.08 C per decade (was +0.09). Dropped the rainfall (down 2 to 6 percent) and snowfall (down 5 to 9 percent) figures, which compared periods across the break, and replaced them with comparisons inside 1990 to 2016. Removed the "rain replacing snow" claim, which the data does not support.
- Fixed oversized annotation boxes in the charts, cropped the report poster, and made all scripts use paths relative to the repository.

## Data Sources and License

- API: Open-Meteo Historical Weather API (free, no key required), endpoint `https://archive-api.open-meteo.com/v1/archive`
- Underlying data: ERA5 reanalysis, ECMWF and the Copernicus Climate Change Service (C3S)
- License: [CC BY 4.0](LICENSE) for the Open-Meteo data. ERA5 is copyright Copernicus Climate Change Service.

This repository contains modified Copernicus Climate Change Service information. Neither the European Commission nor ECMWF is responsible for any use of this information.
