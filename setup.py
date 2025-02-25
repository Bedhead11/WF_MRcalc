from distutils.core import setup
import py2exe

setup(
    windows=[{'script': 'warframe_mr_calc.py'}],
    options={
        "py2exe": {
            "bundle_files": 1,  # Bundle everything into a single executable (optional)
            "compressed": True,
        }
    },
    zipfile=None,
)
