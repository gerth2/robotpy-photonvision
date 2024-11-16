import os
import sys
import pybind11_stubgen 
import photontargeting

script_path = os.path.dirname(os.path.realpath(__file__))

old_argv = sys.argv
sys.argv = [
    "foobart",
    "--exit-code",
    "--ignore-invalid-expressions=<.*>",
    "--root-suffix=",
    "-o",
    f"{script_path}",
    "photontargeting",
]

pybind11_stubgen.main()

sys.argv = old_argv
