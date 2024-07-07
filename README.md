# ITC-X-EAopt
We demonstrate the optimization of ITC across nanostructures by developing an X+EA hybrid optimization method based on evolutionary algorithms (EAs) combined with the atomistic Green's function.

## Description
With the widespread application of nanomaterials in micro-nano devices, interfacial thermal conductance (ITC) has become an indispensable parameter in thermal management. We demonstrate the optimization of ITC across nanostructures by developing an X+EA hybrid optimization method based on evolutionary algorithms (EAs) combined with the atomistic Green's function. Due to the inconvenient hyperparameters tuning associated with EAs, we conduct thousands of grid searches on the hyperparameter configurations of three typical EAs: genetic algorithm (GA), particle swarm optimization (PSO), and simulated annealing (SA), resulting in more suitable parameter ranges. Compared to previous nanostructure design work using Bayesian optimization (BO) and Monte Carlo tree search (MCTS), we find that EAs exhibit robust structural design capabilities and extremely low optimization costs, particularly the GA with the fewest hyperparameters. Furthermore, we propose a highly compatible X+EA hybrid optimization strategy, where X can be substituted with the optimization results of any algorithm and used as the initial structures in the subsequent running of EAs. Among various hybrid optimizations with non-strict hyperparameter settings, the global search capability of BO+GA even rivals that of BO, while reducing optimization time by over 95%. And MCTS+GA effectively resolves the issue of MCTS alone yielding only a few local optima. The proposed X+EA framework can adapt to the nanostructure design with high degrees of freedom or large candidates.

## Installation

### Files loading:
To download, clone this repository:<br>
````
git clone https://github.com/SJTU-MI/ITC-X-EAopt.git
````

### Package requirements:
Some packages need to be installed on demand, such as [Pymatgen](https://pymatgen.org/), [Xenonpy](https://github.com/yoshida-lab/XenonPy), [scikit-learn](https://scikit-learn.org/stable/), [BayesianOptimization](https://github.com/bayesian-optimization/BayesianOptimization).

## Try the desired parts of the project:

### Code in the HTPS4HTTEMOs folder
**1_data4PF**: Power factor (PF) data collection and initial descriptor creation.
- 1_MP_api_features: Descriptors retrieved from the MP database
- 2_Xenonpy_features: Descriptors retrieved from Xenonpy
- 3_data4PF: The PF data and initial descriptor.

**2_featurefiltering**: Feature down-selection process.
- 1_lowvar: Screening features through variance.
- 2_corfilter: Screening features through correlation coefficient.

**3_featurecreation_bySR**: Feature creation process by symbolic regression (SR).
- 1_PC: Feature creation based on Pearson correlation (PC).
- 2_SC: Feature creation based on Spearman correlation (SC).
- 3_DC: Feature creation based on Distance correlation (DC).

**4_PFmodel**: PF prediction model training.
- 1_RF: Random Forest model training.
- 2_XG: XGBoost model training.
- 3_MLP: Multi-Layer Perceptron model training.

**5_SHAPanalysis**: SHAP analysis for the PF prediction model.
- 1_featureimportance: Feature importance calculation.
- 2_beeswarm_plot: Beeswarm plot on SHAP.
- 3_dependence_plot: Dependence plot on SHAP.

**6_meltingpointAPI**: API for the [melting point prediction model](https://www.pnas.org/doi/10.1073/pnas.2209630119).
- 1_prepare4API: Prepare the API json file from MP database for melting point prediction.
- 2_meltingpoint_predict: Melting point prediction.
- 3_meltingpoint_result: Melting point prediction results.

**7_HTP_virtualscreening**: Virtual screening for High-Temperature Thermoelectric Metal Oxides.
- 1_MPscreening: High-Throughput Screening based on MP database.
- 2_MLprediction: PF prediction of three ML models.

**8_PF_calresults**: The PF results by High-Throughput (HTP) DFT calculations.

## Authors

| **AUTHORS** |Shengluo Ma, Shenghong Ju            |
|:-------------:|--------------------------------------------------|
| **VERSION** | V1.0 / November,2023                               |
| **EMAILS**  | shenghong.ju@sjtu.edu.cn                         |
| **GROUP HOME**  | https://ju.sjtu.edu.cn/en/                         |

## Attribution
This work is under BSD-2-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.
