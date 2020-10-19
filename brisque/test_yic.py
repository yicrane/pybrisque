import os
import sys
sys.path.append('K:\\OneDrive\\CodeYic2020\\pybrisque')
sys.path.append('K:\\OneDrive\\CodeYic2020\\pybrisque\\brisque')
sys.path.append('C:/ProgramData/Anaconda3/Lib/site-packages/libsvm')
print(sys.path)


from brisque import BRISQUE
from utilities import root_path

reference_path = root_path('examples', 'I04.BMP')
brisq = BRISQUE()

brisq.get_score(reference_path)