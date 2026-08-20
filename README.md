# Blue Ice Forward Modeling
Code to implement forward modeling of proxies in Antarctic blue ice from the Allan Hills. Results are described in the following paper:

Tierney, J.E. and Ibarra, D. E. (submitted). A reassessment of proxy signal preservation in Antarctic blue ice: Implications for Plio-Pleistocene CO<sub>2</sub>. *Geophysical Research Letters*

## Contents
This repository contains code and small data files required to simulate blue ice proxies in Allan Hills core ALHIC 1901.

The contents of the repository are as follows:

* [blueIceData.xlsx](#blueIceData.xlsx)
* [externalData](#externalData)
* [respirationCorrection.ipynb](#respirationCorrection.ipynb)
* [iterateMixingDepth.ipynb](iterateMixingDepth.ipynb)
* [iceModelCO2.ipynb](#iceModelCO2.ipynb)
* [iceModelIsotopesMOT.ipynb](#iceModelIsotopesMOT.ipynb)
* [timeAvgFunction.py](#timeAvgFunction.py)
* [mixFunction.py](#mixFunction.py)
* [outputFigures](#outputFigures)

Details on each item are provided below.

### blueIceData.xlsx
This Excel spreadsheet contains the compiled proxy data from the Allan Hills blue ice core ALHIC 1901, including sample depth, Ar ages and uncertainties, greenhouse gas concentrations, noble gas ratios, and stable isotope ratios. Please cite the original source papers for these data when using them:

Chronology and isotopes of ice: 
Shackleton, S., Hishamunda, V., Davidge, L., Brook, E., Peterson, J.M., Carter, A., Aarons, S., Kurbatov, A., Introne, D., Yan, Y. and Nesbitt, I.M., 2025. Miocene and Pliocene ice and air from the Allan Hills blue ice area, East Antarctica. *Proceedings of the National Academy of Sciences*, 122(44), e2502681122. [link](https://doi.org/10.1073/pnas.2502681122)

Noble gas data:
Shackleton, S., Hishamunda, V., Yan, Y., Carter, A., Morgan, J., Severinghaus, J., Aarons, S., Marks-Peterson, J., Epifanio, J., Buizert, C. and Brook, E., 2026. Global ocean heat content over the past 3 million years. *Nature*, 651(8106), 653-657. [link](https://www.nature.com/articles/s41586-026-10116-3)

Greenhouse gas data and isotopes of CO<sub>2</sub>:
Marks-Peterson, J., Shackleton, S., Higgins, J., Severinghaus, J., Yan, Y., Buizert, C., Kalk, M., Beaudette, R., Hishamunda, V., Eves, D. and Carter, A., 2026. Broadly stable atmospheric CO<sub>2</sub> and CH<sub>4</sub> levels over the past 3 million years. *Nature*, 651(8106), 647-652. [link](https://www.nature.com/articles/s41586-025-10032-y)

### externalData
This folder contains data files needed for forward modeling, including:

* alkenone_co2.csv: Vetted alkenone proxy CO<sub>2</sub> data, from the [CenoCO<sub>2</sub>PIP Consortium](https://www.paleo-co2.org/)
* boron_co2.csv: Vetted boron proxy CO<sub>2</sub> data, from the [CenoCO<sub>2</sub>PIP Consortium](https://www.paleo-co2.org/)
* paleosol_co2.csv: Vetted paleosol proxy CO<sub>2</sub> data, from the [CenoCO<sub>2</sub>PIP Consortium](https://www.paleo-co2.org/)
* antarctica2015co2composite-noaa.txt: Composite CO<sub>2</sub> record from traditional Antarctic ice cores ([Bereiter et al. 2015](https://doi.org/10.1002/2014GL061957))
* Clark2024Temp.xlsx: the global SST and surface mean temperature reconstruction from [Clark et al., 2024](https://doi.org/10.1126/science.adi1908)
* edc3deuttemp2007-noaa.xlsx: stable hydrogen isotopic composition of ice (d2H) measured in the EPICA Dome C ice core ([Jouzel et al., 2007](https://doi.org/10.1126/science.1141038))
* edc2021noblegastemp.xlsx: reconstructed mean ocean temperature (MOT) from noble gas ratios measured in the EPICA Dome C ice core ([Haeberli et al., 2021](https://doi.org/10.1126/science.1141038))
* lisiecki2005-d18o-stack-noaa.xlsx: The LR04 benthic d18O stack ([Lisiecki and Raymo, 2005](https://doi.org/10.1029/2004PA001071))

### respirationCorrection.ipynb
This Jupyter Notebook contains code to compute the respired/microbial metabolic end-member for the d13C of CO<sub>2</sub> via a regression approach, apply the regression correction to non-pristine CO2 datapoints, and produce Figure 1 of the paper.

### iterateMixingDepth.ipynb
This Jupyter Notebook contains code to iteratively determine the optimal mixing depths for the three ice proxies that are simulated, and produce Figure S1 of the paper.

### iceModelCO2.ipynb
This Jupyter Notebook contains code to forward model time-averaging and mixing of a primary (atmospheric)  CO<sub>2</sub> signal in blue ice, and produce Figure 2 of the paper.

### iceModelIsotopesMOT.ipynb
This Jupyter Notebook contains code to forward model time-averaging and mixing of stable hydrogen isotopes of ice (d2H) and noble gas-derived mean ocean temperature (MOT) in blue ice, and produce Figure 3 of the paper.

### timeAvgFunction.py
Python script to model time-averaging in blue ice. Needed to run the Jupyter Notebooks.

### mixFunction.py
Python script to model diffusive-style mixing in blue ice. Needed to run the Jupyter Notebooks.

### outputFigures
Folder holding output figures printed in .pdf format.