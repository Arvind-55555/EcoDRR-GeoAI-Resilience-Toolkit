#  **EcoDRR GeoAI Pipeline**
### **Ecosystem-based Disaster Risk Reduction using Remote Sensing, Machine Learning, and Hydrological Modeling**

This repository implements a complete **Eco-DRR (Ecosystem-based Disaster Risk Reduction)** workflow combining:
- Google Earth Engine (GEE)
- Deep learning (U-Net)
- Hydrological modeling (DEM-based flood, CN runoff)
- NDVI time-series analysis
- Ecosystem service assessment
- DRR risk fusion modeling

The pipeline operationalizes methodologies recommended in the  
**UNEP Eco-DRR Source Book (2019)** — enabling spatial intelligence for resilience planning and Nature-based Solutions (NbS).

---

#  **Eco-DRR Objectives**
This workflow supports:

- Mapping ecosystem condition & degradation  
- Detecting hydrological hazards (flood susceptibility, runoff)  
- Identifying exposed + vulnerable built-up areas  
- Quantifying ecosystem services  
- Computing DRR risk through multi-criteria fusion  
- Prioritizing NbS interventions (wetland restoration, afforestation, urban green buffers, etc.)

---

#  **Workflow Architecture**

```
                    ┌─────────────────────────────────┐
                    │  Google Earth Engine (GEE)      │
                    │  • Sentinel-2 SR Harmonized     │
                    │  • CHIRPS Rainfall              │
                    │  • NASADEM DEM                  │
                    └──────────────┬──────────────────┘
                                   │
                                   ▼
                Preprocessed GeoTIFFs (RGB, NDVI, DEM, Rainfall)
                                   │
                                   ▼
            ┌────────────────────────────────────────────────────┐
            │        Local GeoAI Processing Pipeline             │
            │  • Patch extraction                                │
            │  • U-Net landcover segmentation                    │
            │  • DEM: slope, depression, flood proxy             │
            │  • Curve Number (CN) runoff modeling               │
            │  • NDVI change detection                           │
            │  • Habitat quality (NDVI-based proxy)              │
            └──────────────────────┬─────────────────────────────┘
                                   │
                                   ▼
                          DRR Risk Fusion Model
                                   │
                                   ▼
                            Eco-DRR Risk Map
                    (NbS / Restoration Priority Zones)
```

---

#  **Repository Structure**

```
├── notebooks/
│   ├── 3_EcoDRR_DRR_AdvancedModeling_v1.ipynb
│   ├── 4_EcoDRR_Integrated_GeoAI_RiskPipeline_v2.ipynb
│   └── 5_EcoDRR_Master_GeoAI_Resilience_Model_v1.ipynb
│
├── data/
│   ├── sent_rgb.tif
│   ├── sent_ndvi.tif
│   ├── dem.tif
│   ├── chirps.tif
│   ├── ndvi_recent.tif
│   ├── ndvi_hist.tif
│   └── landcover_unet.tif
│
├── models/
│   └── tiny_unet_trained.pth
│
├── src/
│   ├── dem_flood.py
│   ├── runoff_cn.py
│   ├── ndvi_change.py
│   ├── invest_habitat.py
│   ├── invest_coastal.py
│   └── risk_fusion.py
│
└── README.md
```

---

#  **Pipeline Components**

## 1) **Sentinel-2 Preprocessing (GEE)**
- QA60 cloud masking  
- NDVI & NDWI generation  
- Local TIFF export  
- Prepares 4-channel input for U-Net (RGB + NDVI)  

---

## 2) **U-Net Landcover Segmentation**
Predicts 3 major classes:
| Class | Meaning |
|-------|---------|
| **1** | Vegetation |
| **2** | Bare Soil |
| **3** | Built-up / Impervious |

Outputs used for:
- Exposure estimation  
- CN hydrological assignment  
- Habitat quality adjustment  
- Overall Eco-DRR risk  

---

## 3) **DEM-Based Flood Hazard (NASADEM)**
Computed using:
- Sobel slope  
- Depression index  
- Low-lying accumulation potential  
- Gaussian smoothing  

Produces a **flood susceptibility raster** (0–1).

---

## 4) **Curve Number (CN) Runoff Modeling**
Inputs:
- CHIRPS rainfall  
- Landcover segmentation  
- CN lookup table  

Outputs:
- Surface runoff (mm)
- Hydrological hazard map

---

## 5) **NDVI Change Detection (ΔNDVI)**
Difference between:
- Historical NDVI  
- Recent NDVI  

Detects:
- Degraded vegetation  
- Drought effects  
- Vulnerability hotspots  

---

## 6) **Habitat Quality Proxy**
A simple NDVI-based ecosystem services estimate:

```
HQ = Normalize(NDVI_recent)
```

Higher HQ → better ecological buffering capacity.

---

## 7) **DRR Risk Fusion Model**

### Formula Implemented

```
Risk = Hazard × Exposure × (1 + Vulnerability) × (1 − Ecosystem Services)
```

**Where:**

| Component | Description |
|----------|-------------|
| **Hazard** | (Flood proxy + Runoff) / 2 |
| **Exposure** | Built-up from U-Net |
| **Vulnerability** | NDVI loss (ΔNDVI < −0.05) |
| **Ecosystem Services** | Habitat Quality (NDVI proxy) |

### Output:
- High-risk areas  
- NbS priority zones  
- Restoration targets  
- Urban resilience planning layers  

---

#  **Final Output: Eco-DRR Risk Map**
The risk map integrates:
- Topography  
- Hydrology  
- Landcover  
- Vegetation loss  
- Ecosystem services  

And provides **decision-ready spatial intelligence** for:
- City planning  
- Flood mitigation  
- Ecosystem restoration  
- Climate adaptation strategies  

---

#  **Requirements**
```
Python 3.9+
torch
numpy
rasterio
matplotlib
earthengine-api
geemap
scipy
```

---

# **Usage**

### 1. Run all steps in the Master Notebook:
```
notebooks/5_EcoDRR_Master_GeoAI_Resilience_Model_v1.ipynb
```

### 2. OR run individual modules:
- Landcover segmentation  
- Hydrology  
- ΔNDVI  
- Habitat quality  
- Risk fusion  

### 3. Outputs appear under `/content/data/`.

---

#  License
MIT License

---
