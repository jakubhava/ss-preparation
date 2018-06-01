import sys
import random
row = (str(bool(random.getrandbits(1))), str(random.randrange(1,100)), str(random.randrange(1,10)), str(random.randrange(1,10)), str(random.randrange(1,10)), str(random.randrange(1,10)), str(random.randrange(10000,10000000)), str(random.randrange(3,100)), str(random.randrange(1,10)), str(random.randrange(1,100)), str(random.randrange(1,10)), str(random.randrange(100000, 100000000)), str(random.randrange(1,5)))
row_str = ','.join(row)

thefile = open("spark-summit-demo-data/" + str(sys.argv[1]) + ".csv", 'w')
thefile.write(row_str)
thefile.close()
