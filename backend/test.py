import os
import json
#print(os.listdir("./dataset/speakers/"))
#print(os.listdir("E:\\github repos\\AspectWise\\backend\\datasets\\speakers"))
#for (root,dirs,files) in os.walk(os.path.abspath(f"./datasets/speakers/"), topdown=True):
#   break
#print(jsondirs)
print([ f.name for f in os.scandir(os.path.abspath(f"./datasets/speakers/")) if f.is_dir() ])