import sys
import os

print ("hello " + sys.argv[1])

baseDir = os.path.dirname(os.path.realpath(__file__))
subDir = "/target/output/"
outputJson_rel = "release_notes_versions.txt"
outputFile_rel = baseDir + subDir + outputJson_rel
os.makedirs(os.path.dirname(outputFile_rel), exist_ok=True)
with open(outputFile_rel, "w") as f:
    f.write("hihihih")
