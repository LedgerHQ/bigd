from conans import ConanFile, CMake, tools

class BigdConan(ConanFile):
    name = "bigd"
    version = "2.6.1"
    license = "MIT"
    author = "Alexis Le Provost <alexis.le-provost@ledger.fr>"
    url = "https://github.com/LedgerHQ/bigd.git"
    description = "A free library of multiple-precision arithmetic routines written in ANSI C"
    topics = ("conan", "c", "arithmetic")
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = {}
    generators = "cmake"
    exports_sources = ["include/*", "src/*", "CMakeLists.txt", "cmake/*"]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
    

