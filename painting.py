import random
height = 5  * random.random()
width = 5  * random.random()
canCov = 5
def painting(height,width,canCov):
    return int(round((height*width) / canCov,0))

result = painting(height,width,canCov)
print(result)