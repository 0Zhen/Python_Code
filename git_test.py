import subprocess

proc = subprocess.Popen(['git','log'], stdout = subprocess.PIPE)
output = proc.stdout.read()
output = output.decode("utf-8")
print(output)

output = output.replace("\t","")
output = output.replace(" ","")
output = output.split("\n")


print(':::::::::::::::::::::::::::::')
print(output)
#print(output)
#print(output[0:2])