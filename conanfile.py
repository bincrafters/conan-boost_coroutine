from conans import ConanFile, tools, os

class BoostCoroutineConan(ConanFile):
    name = "Boost.Coroutine"
    version = "1.64.0"
    generators = "boost" 
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-boost-coroutine"
    source_url = "https://github.com/boostorg/coroutine"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["coroutine"]
    build_requires = "Boost.Generator/0.0.1@bincrafters/testing"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Context/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Exception/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Range/1.64.0@bincrafters/testing", \
                      "Boost.System/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing"

                      #assert1 config0 context12 core2 exception5 move3 range7 system3 throw_exception2 type_traits3 utility5
                      
    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def build(self):
        boost_build = self.deps_cpp_info["Boost.Build"]
        b2_bin_name = "b2.exe" if self.settings.os == "Windows" else "b2"
        b2_bin_dir_name = boost_build.bindirs[0]
        b2_full_path = os.path.join(boost_build.rootpath, b2_bin_dir_name, b2_bin_name)
        
        self.run(b2_full_path + " -j4 -a --hash=yes")

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

        self.copy(pattern="*", dst="lib", src="stage/lib")

    def package_info(self):
        self.user_info.lib_short_names = (",").join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
