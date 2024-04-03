string = ("Extension modules: mkl._mklinit, mkl._py_mkl_service, numpy.core._multiarray_umath, "
          "numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, "
          "numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, "
          "numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, "
          "numpy.random._generator, matplotlib._c_internal_utils, PIL._imaging, matplotlib._path, kiwisolver._cext, "
          "psutil._psutil_osx, psutil._psutil_posix (total: 21)")

packages = string.split(':')[1].replace(" ","").split(",")

# The list of missing packages are in packages list, we'll us OS to install them
# We'll use subprocess to install the missing packages
import subprocess

for package in packages:
    subprocess.run(["pip", "install", package])
