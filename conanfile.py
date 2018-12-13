#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostCoroutineConan(base.BoostBaseConan):
    name = "boost_coroutine"
    url = "https://github.com/bincrafters/conan-boost_coroutine"
    lib_short_names = ["coroutine"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    source_only_deps = ["thread"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_context",
        "boost_core",
        "boost_exception",
        "boost_move",
        "boost_range",
        "boost_system",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility"
    ]
