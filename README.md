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
Some packages need to be installed on demand, such as [scikit-opt](https://scikit-opt.github.io/), [numpy](https://numpy.org/).

## Try the desired parts of the project:

### Code in the ITC-X-EAopt folder
**0-data_ITC**: interfacial thermal conductance (ITC) data collection
- SiSi_structure_ITC.txt: ITC data for the Si-Si interface
- SiGe_structure_ITC.txt: ITC data for the Si-Ge interface

**1-GA**
- GArunalone.py: the code for running genetic algorithm alone

**2-PSO**
- PSOrunalone.py: the code for running particle swarm optimization alone

**3-SA**
- SArunalone.py: the code for running simulated annealing alone

**4-X+EA**: the X+EA hybrid optimization method
- demo_run: a demo X result
- run_file: the code for running X+EA hybrid optimization
- sko_msl: the basic code of X+EA hybrid optimization

### running
To run the GA, PSO, and SA alone, try these commands:<br>
````
cd dir/1-GA (2-PSO, 3-SA)
cp -r dir/0-data_ITC ./data_ITC
python GArunalone.py (PSOrunalone.py, SArunalone.py)
````

To run the X+EA hybrid optimization, try these commands:<br>
````
cd dir/4-X+EA/demo_run
cp -r dir/0-data_ITC ./data_ITC
cp -r dir/sko_msl/* ./
cp -r dir/run_file/XGArun.py (XPSOrun.py, XSArun.py) ./
python XGArun.py (XPSOrun.py, XSArun.py)
````

### Data in the ITC-X-EAopt folder
**1-GA**: nanostructure design via genetic algorithm
- 1-populationsize: hyperparameter population size N in GA
- 2-probability: hyperparameter crossover probability Pc and mutation probability Pm in GA

**2-PSO**: nanostructure design via particle swarm optimization
- 1-populationsize: hyperparameter population size N in PSO
- 2-inertiaweight: hyperparameter inertia weight 𝜔 in PSO
- 3-c1c2coefficient: hyperparameter c1 and c2 in PSO

**3-SA**: nanostructure design via simulated annealing
- 1-struc_count_ITC: hyperparameter L and kmax in SA
- 2-chainlength: hyperparameter L in SA
- 3-tempcurve: hyperparameter m, n, and q in SA

**4-comparison**: comparisons among EAs and other algorithms
- 1-globalsearch: global search
- 2-localoptima: local optima
- 3-time: coretime

**5-X+EA**: nanostructure design via X+EA hybrid optimization
- 0-data: data
- 1-BOGA: BO+GA
- 2-MCGA: MCTS+GA

## Authors

| **AUTHORS** |Shengluo Ma, Shenghong Ju            |
|:-------------:|--------------------------------------------------|
| **VERSION** | V1.0 / May, 2024                               |
| **EMAILS**  | shenghong.ju@sjtu.edu.cn                         |
| **GROUP HOME**  | https://ju.sjtu.edu.cn/en/                         |

## Attribution
This work is under BSD-3-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.
