# supp-ISCB-LA-2020-ID3

Additional supplementary information:

*Virtual screening of potential kinase inhibitors within the PI3K/AKT pathway of Leishmania*

Authors: Rodrigo Ochoa, Amaya Ortega-Pajares, Florencia A. Castello, Federico Serral, Darío Fernández Do Porto, Carlos Muskus

*Content:*

This repository contains 3 folders with the following information:
- models: Folder with the predicted model of each Leishmania kinase in pdb and pdbqt format, and the configuration file to dock compounds within the identified druggable pocket. These files can be used as input for the server: https://drugdiscovery.tacc.utexas.edu/
- networks: Folder with the three Leishmania protein-protein interaction networks that can be analyized using Cytoscape (https://cytoscape.org/)
- script: Two scripts are provided. One (find-reciprocal-2.py) allows to run the best reciprocal hits protocol using as example two CSV files with the BLAST results between two set of proteins: human and Leishmania major. The second script (clustering_comp.py) allows the clustering of compounds using their SMILES formats, based on a file containing the top 20 compounds detected during the docking analysis (final_report_top20.txt).

The rest of the analysis can be done using the servers mentioned in the publication and the data from the Supplementary Information section of the manuscript.

Any questions please write us to the email: rodrigo.ochoa@udea.edu.co.
