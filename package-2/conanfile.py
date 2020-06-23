
from conans import ConanFile, CMake, tools, python_requires
import os

class Package2Conan(ConanFile):
    name = "package-2"
    settings = "os", "compiler", "build_type", "arch", "toolchain"
    options = {"shared": [True, False]}
    default_options = ("shared=False")
    generators = "cmake"

    requires = (
        "package-1/[=1.0]@error/test"
    )

    def imports(self):
        self.copy(pattern="*.dylib*", dst="bin", src="lib")
        self.copy(pattern="*.so*", dst="bin", src="lib")
