from cx_Freeze import *

includefiles = ['calci.ico']
base =None
if sys.platform == "win32":
    base = "win32GUI"


shortcut_table = [
    ("DesktopShortcut", # shortcut
     "DesktopFolder", #Directory_
     "Calculator", #Name
     "TARGETDIR", #Component _
     "[TARGETDIR]\smartcalculator.exe", # Taarget
     None,  # Arguements
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR", #WKDir
      )
]

msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Calculator",
    author="Anish Bhandarkar",
    name="Calculator",
    options={'build_exe': {'include_files': includefiles}, 'bdist_msi': bdist_msi_options, },
    executables=[
        Executable(
            script="smartcalculator.py",
            base=base,
            icon='calci.ico',
        )
    ]

)






























