# # change directory two levels up to project folder
$scriptpath = $MyInvocation.MyCommand.Path
$dir1 = Split-Path $scriptpath   # parent folder
$dir2 = Split-Path $dir1         # up second level
Set-Location $dir2

# Activate the virtual environment
$venvPath = ".venv"
& $venvPath\Scripts\activate.ps1

& uv sync --no-dev --group build

# update version info file
$versionScript = ".\scripts\create_version_file.py"
& $venvPath\Scripts\python.exe $versionScript

# Run the pyinstaller command
$launcherFile = ".\dodecadog\main.py"
$pyInstallerExecutable = "pyinstaller"
$appName = "template_app"
$versionFile = ".\scripts\app_version_info.txt"
$iconFile = ".\dodecadog\assets\icons\dog.ico"
# $addIcon = ".\src\data\icon.ico;.\data" # use this to add specific file
$addDataFolder = ".\dodecadog\assets;.\assets" # use this to add entire folder

# build command with settings args
& $pyInstallerExecutable $launcherFile --add-data $addDataFolder --version-file $versionFile -w -n $appName -i $iconFile --noconfirm --onefile

# # update requirements file
# & pip freeze > requirements.txt

# # update python version file
# & py --version > python_version.txt

# deactivate environment
& deactivate