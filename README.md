# Blue Ice Forward Modeling
Code implement forward modeling of proxies in Antarctic blue ice from the Allan Hills. Results are described in the following paper:

Tierney, J.E. and Ibarra, D. E. (submitted). A reassessment of proxy signal preservation in Antarctic blue ice: Implications for Plio-Pleistocene CO<sub>2</sub> *Geophysical Research Letters*

## Contents
This repository contains code and small data files required to simulate blue ice proxies in Allan Hills core ALHIC 1901.

The contents of the repository are as follows:

* [blueIceData.xlsx](#BlueIceProxyData)
* [externalData](#otherinputdata)
* [respirationCorrection.ipynb](#RespirationCorrection)
* [iceModelCO2.ipynb](#ForwardModelCO2)
* [iceModelIsotopesMOT.ipynb](#ForwardModelIsotopesMOT)
* [timeAvgFunction.py](#TimeAvgFunction)
* [mixFunction.py](#MixFunction)
* [outputFigures](#Figures)

Details on each item are provided below.

### BlueIceProxyData
This Excel spreadsheet contains the compiled proxy data from the Allan Hills blue ice core ALHIC 1901, including sample depth, Ar ages and uncertainties, greenhouse gas concentrations, noble gas ratios, and stable isotope ratios. Please cite the original source papers for these data when using them:

Chronology and isotopes of ice: 
Shackleton, S., Hishamunda, V., Davidge, L., Brook, E., Peterson, J.M., Carter, A., Aarons, S., Kurbatov, A., Introne, D., Yan, Y. and Nesbitt, I.M., 2025. Miocene and Pliocene ice and air from the Allan Hills blue ice area, East Antarctica. *Proceedings of the National Academy of Sciences*, 122(44), e2502681122.

Noble gas data:
Shackleton, S., Hishamunda, V., Yan, Y., Carter, A., Morgan, J., Severinghaus, J., Aarons, S., Marks-Peterson, J., Epifanio, J., Buizert, C. and Brook, E., 2026. Global ocean heat content over the past 3 million years. *Nature*, 651(8106), 653-657.

Greenhouse gas data and isotopes of CO<sub>2</sub>:
Marks-Peterson, J., Shackleton, S., Higgins, J., Severinghaus, J., Yan, Y., Buizert, C., Kalk, M., Beaudette, R., Hishamunda, V., Eves, D. and Carter, A., 2026. Broadly stable atmospheric CO2 and CH4 levels over the past 3 million years. *Nature*, 651(8106), pp.647-652.

### otherinputdata
This folder contains data files needed for forward modeling, including:

* The spatial points used when regridding climate model output,
* The climate model runs used for various ensembles, and
* Global, conservative R values
* parameters for the function dGMST.

### RespirationCorrection
This Jupyter Notebook contains code to compute the respired/microbial metabolic end-member for the d13C of CO2 via a regression approach, apply the regression correction to non-pristine CO2 datapoints, and produce Figure 1 of the paper.

### ForwardModelCO2
This Jupyter Notebook contains code to forward model time-averaging and mixing of a primary (atmospheric) CO2 signal in blue ice, and produce Figure 2 of the paper.

### ForwardModelIsotopesMOT
This Jupyter Notebook contains code to forward model time-averaging and mixing of stable hydrogen isotopes of ice (d2H) and noble gas-derived mean ocean temperature (MOT) in blue ice, and produce Figure 3 of the paper.

### TimeAvgFunction
Python script to model time-averaging in blue ice.

### MixFunction
Python script to model diffusive-style mixing in blue ice.

### Figures
Folder holding output figures printed in .pdf format.