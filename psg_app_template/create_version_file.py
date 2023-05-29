# %% imports
import os.path
from pyinstaller_versionfile import create_versionfile
from app_package.pgk_module import APP_VERSION

# %% build path for version info file output
folder = os.path.dirname(os.path.abspath(__file__))
filename = "app_version_info.txt"
filepath = os.path.join(folder, filename)

# %% generate file
create_versionfile(
    output_file=filepath,
    version=APP_VERSION,
    company_name="ACME Inc.",
    file_description="Template App",
    product_name="Template App",
    # internal_name="Simple App",
    legal_copyright="© 2023. All rights reserved.",
    # original_filename="SimpleApp.exe",
)
print(f"version file created/updated: {filepath}")
