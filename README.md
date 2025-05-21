# ST-Imputer
This is the code for paper:
> ST-Imputer: Context-aware Spatiotemporal Imputation Diffusion Network with Physics Guidance

## Dependencies
Recent versions of the following packages for Python 3 are required:
* numpy==1.24.1
* PyYAML==6.0.1
* Requests==2.31.0
* scikit_learn==1.5.0
* scipy==1.13.1
* setuptools==69.5.1
* tensorboardX==2.6.2
* torch==1.13.1
* torch_cluster==1.6.0
* torch_geometric==2.5.3
* torch_sparse==0.6.15
* tqdm==4.66.4

## Datasets
All of the datasets we use are publicly available datasets.
### Link
The used datasets are available at:
* GLODAPv2 https://glodap.info/
* ECMWF https://cds.climate.copernicus.eu/
* CMEMS https://marine.copernicus.eu/
* AQI-36 http://research.microsoft.com/apps/pubs/?id=264768


## Usage
Use the following command to run the main script:

python train.py

If you want to modify the experimental configuration parameters, please refer to /config/base.yaml and config.py.
Specifically, key parameters such as the epochs, feature dimensions, and the number of dataset nodes can all be modified in the configuration file.

## Use your own dataset
Convert the data file into `.txt` format, place it in the `\data` directory, update the corresponding path in the `XX` file, and modify the `num_nodes` in `config.py`.
