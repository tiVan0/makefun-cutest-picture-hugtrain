import os, shutil
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(here, "art.jpg"), "/output/entry.png")
