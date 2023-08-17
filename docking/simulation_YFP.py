import os
os.system("./VP3-hiYFP-RLink-CotB")

for i in range (0,24):
     os.system("lightdock3.py setup.json 100 -c 1 -s fastdfire -l "+str(i))
     os.system("lgd_generate_conformations.py vp3hiYFPRLinkCotB_ASN773result.pdb lightdock_Vg.pdb swarm_"+str(i)+"/gso_100.out 200")
     os.system("lgd_cluster_bsas.py swarm_"+str(i)+"/gso_100.out")
