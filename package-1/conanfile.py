
from conans import ConanFile, CMake, tools, python_requires
import os

class Package1Conan(ConanFile):
    name = "package-1"
    settings = "os", "arch", "compiler", "build_type", "toolchain"
    requires = (
        "libcurl/[=7.66.0]"
    )
    options = {
        "shared": [True, False],
         "fPIC": [True, False],
    }
    default_options = {
        "shared": False, 
        "fPIC": True
    }

    def package_id(self):
        self.info.requires['libcurl'].full_version_mode()
