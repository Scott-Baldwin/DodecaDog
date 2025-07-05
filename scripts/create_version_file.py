# %% imports
import os.path, sys
from pyinstaller_versionfile import create_versionfile

sys.path.append("./dodecadog")
from core import VERSION, NAME

BUILD = ".2"

# %% build path for version info file output
folder = os.path.dirname(os.path.abspath(__file__))
filename = "app_version_info.txt"
filepath = os.path.join(folder, filename)


# %% generate file
create_versionfile(
    output_file=filepath,
    version=VERSION + BUILD,
    # company_name="ACME Inc.",
    file_description=NAME,
    product_name=NAME,
    # internal_name="Simple App",
    legal_copyright="© Scott-Baldwin 2025. All rights reserved.",
    # original_filename="SimpleApp.exe",
)
print(f"version file created/updated: {filepath}")
