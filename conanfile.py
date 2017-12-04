from conans import ConanFile, tools


class BoostCoroutineConan(ConanFile):
    name = "Boost.Coroutine"
    version = "1.65.1"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Context/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Exception/1.65.1@bincrafters/testing", \
        "Boost.Move/1.65.1@bincrafters/testing", \
        "Boost.Range/1.65.1@bincrafters/testing", \
        "Boost.System/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Utility/1.65.1@bincrafters/testing"
    lib_short_names = ["coroutine"]
    is_header_only = False

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-coroutine"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    generators = "boost"

    def package_id(self):
        if self.is_header_only:
            self.info.header_only()

    # pylint: disable=unused-import
    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
