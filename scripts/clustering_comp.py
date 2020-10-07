#!/usr/bin/python

# NOTE: For this script it is required a file containing the results of the docking and the SMILES of the top20 compounds
# 
# An example of how to run this script is: python2.7 clustering_comp.py
#
# Any questions please write to: rodrigo.ochoa@udea.edu.co

import rdkit
from rdkit import Chem
from rdkit import DataStructs
from rdkit.ML.Cluster import Butina
from rdkit.Chem import AllChem
from rdkit.Chem import MCS

report=[x.strip() for x in open("final_report_top20.txt")]

compounds={}

for data in report:
    info=data.split()
    comp=info[1]
    smiles=info[3]
    if comp not in compounds:
        compounds[comp]=smiles
        
idComp=[]
comps=[]
smiles=[]

for comp in compounds:
    idComp.append(comp)
    smiles.append(compounds[comp])
    comps.append(Chem.MolFromSmiles(compounds[comp]))

def ClusterFps(fps,cutoff=0.2):
    # first generate the distance matrix:
    dists = []
    nfps = len(fps)
    for i in range(1,nfps):
        sims = DataStructs.BulkTanimotoSimilarity(fps[i],fps[:i])
        dists.extend([1-x for x in sims])

    # now cluster the data:
    cs = Butina.ClusterData(dists,nfps,cutoff,isDistData=True)
    return cs

#The return value is a tuple of clusters, where each cluster is a tuple of ids.

#Example usage:
fps = [AllChem.GetMorganFingerprintAsBitVect(x,3,1024) for x in comps]
clusters=ClusterFps(fps,cutoff=0.7)
#print clusters

for i,clus in enumerate(clusters):
    
    if len(clus)>3:
        print "Cluster: %d" %i
        #molCluster[i]=[]
        molClust=[]
        for element in clus:
            molClust.append(comps[element])
            print idComp[element]
        result=MCS.FindMCS(molClust)
        print result

