# São Paulo Flood Risk Analysis

This repository contains a Jupyter notebook that analyzes flood risk in São Paulo, Brazil, using Digital Elevation Model (DEM) data, river and waterbody data, and rainfall data. The analysis identifies flood-prone areas by combining low elevation, proximity to water sources, and heavy rainfall events.

## Table of Contents
- [Installation](#installation)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Results](#results)
- [Usage](#usage)
- [License](#license)

## Installation

To run the notebook, the following Python libraries are required:

```bash
pip install rasterio geopandas shapely matplotlib folium pandas scipy
```

## Data Sources

The analysis uses the following datasets:
- **Digital Elevation Model (DEM)**: `s24_w047_1arc_v3.tif`
- **Rivers and Waterbodies**: `sao_paulo_waterways.geojson` and `sao_paulo_water.geojson`
- **Rainfall Data**: `sao_paulo_rain_2021-2025.csv`

These datasets go in the `data` directory, but are not committed to this repo.  The DEM data is provided by [USGS Earth Explorer](https://earthexplorer.usgs.gov/) mission, and the river and waterbody data is obtained from [OpenStreetMap (Geofabrik)](https://www.geofabrik.de/geofabrik/) and clipped using `clip_water_files.py`. The rainfall data is obtained from the [National Centers for Environmental Information - CDO](https://www.ncei.noaa.gov/cdo-web/) website.  

## Methodology

1. **Load and Visualize DEM Data**:
   - The DEM data is loaded using `rasterio` and visualized using `matplotlib`.
   - Low-lying areas (below 50 meters) are identified as potential flood zones.

2. **Identify Flood-Prone Zones**:
   - Flood-prone zones are identified by combining low elevation and flat areas using a slope threshold.

3. **Load and Plot River & Waterbody Data**:
   - River and waterbody data are loaded using `geopandas` and plotted over the DEM.

4. **Load and Analyze Rainfall Data**:
   - Rainfall data is loaded using `pandas` and analyzed to identify days with heavy rainfall (above 50 mm).

5. **Combine Data for Flood Risk Analysis**:
   - Flood risk areas are identified by combining low elevation, proximity to water sources (using a 500-meter buffer), and heavy rainfall events.

## Results

The final output is a flood risk map that highlights areas in São Paulo that are at risk of flooding based on the combined analysis of elevation, proximity to water, and rainfall data.

## Usage

To run the analysis, gather appropriate files, open the Jupyter notebook `sao_paulo_flood_risk.ipynb` and execute the cells sequentially. Ensure that all required libraries are installed and that the data files are in the correct directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.