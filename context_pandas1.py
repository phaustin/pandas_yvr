import site
import sys
from pathlib import Path
#
# Since __file__ gives the full path to this file, we
# can use Path().parent to find the folder this file is in
# and from there, locate both the processed and raw data
# folders.  We can also use sys.path.insert to p[ace this
# folder on the python sys path, which means that folders
# below this that contain library modules can be imported into
# our python scripts/notebooks.
#
curr_dir = Path(__file__).parent  #notebooks/pandas
root_dir = curr_dir
data_dir = root_dir / "data"
print((f"in context_pandas1.py, setting root_dir to \n{root_dir}\n"
       f"setting data_dir to \n{data_dir}\n"))
