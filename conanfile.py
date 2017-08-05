from conans import ConanFile, tools, os

class BoostCoroutineConan(ConanFile):
    name = "Boost.Coroutine"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/coroutine"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "coroutine"
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
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()