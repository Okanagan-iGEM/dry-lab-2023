#PBS -N 2HDI-anal
#PBS -q medium
#PBS -l nodes=1:ppn=8
#PBS -S /bin/bash
#PBS -d ./
#PBS -e ./analysis.err
#PBS -o ./analysis.out

### Calculate the number of swarms ###

s=`ls -d ./swarm_* | wc -l`
swarms=$((s-1))

### Create files for Ant-Thony ###

### Generate LightDock models ###

ant_thony.py -c 8 generate_lightdock.list;

### Clustering BSAS (rmsd) within swarm ###

ant_thony.py -c 8 cluster_lightdock.list;

### Generate ranking files for filtering ###

lgd_rank.py $s 100;

### Copy structures for further analysis ###

lgd_copy_structures.py rank_by_scoring.list > /dev/null 2> /dev/null;