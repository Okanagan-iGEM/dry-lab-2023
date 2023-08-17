import os
os.system("./CotB-RigLink-VP3")

for i in range (0,22):
     os.system("lightdock3.py setup.json 100 -c 1 -s fastdfire -l "+str(i))
     os.system("lgd_generate_conformations.py result-working.pdb lightdock_Vg.pdb swarm_"+str(i)+"/gso_100.out 200")
     os.system("lgd_cluster_bsas.py swarm_"+str(i)+"/gso_100.out")
