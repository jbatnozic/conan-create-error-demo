
from conans import ConanFile, CMake, tools
import os

class Package3Conan(ConanFile):
    name = "package-3"
    settings = "os", "compiler", "build_type", "arch", "toolchain"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = (
        "shared=False",
        "protobuf:shared=True",
        "framework-protobufcomms:shared=True",
        "mapdisplay-tile-model:shared=True",
        "fPIC=True"
    )
    
    generators = "cmake"

    requires = (
        "package-2/[=1.0]@error/test"
    )

    license = "commercial"

    def package_id(self):
        self.info.shared_library_package_id()
