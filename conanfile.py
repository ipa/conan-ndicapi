from conans import ConanFile, CMake, tools

class NDICAPIConan(ConanFile):
    name = "NDICAPI"
    version = "1.6"
    description = "NDI C API"
    url = "https://github.com/PlusToolkit/ndicapi.git"
    license = "CMAKE_INSTALL_PREFIX"
    exports = ["LICENSE.txt"]
    source_subfolder = "source_subfolder"
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = ""
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/PlusToolkit/ndicapi.git")
        self.run("cd ndicapi")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "install"
        cmake.configure(source_folder="ndicapi")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include/ndicapi", src="install/include")
        self.copy("*ndicapiExport.h", dst="include/ndicapi", src="../source/ndicapi")
        #self.copy("*.pdb", dst="bin", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ndicapi"]
