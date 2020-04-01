# bigd
![build](https://github.com/LedgerHQ/bigd/workflows/build/badge.svg)
![deploy](https://github.com/LedgerHQ/bigd/workflows/deploy/badge.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)

**_bigd_** is a free library of multiple-precision arithmetic routines written in ANSI C 
to carry out calculations with the large natural numbers used in cryptography computations.

The **_bigd_** library is designed to work with the set of natural numbers N; 
that is, the non-negative integers 0,1,2,... . 

## Dependencies
This library is based on **_cmake_** as a build system and **_conan_** as a package manager 
so you should install it before starting (at least version _3.10_ and _1.23_ respectively).

## Local build

You can build the library by running : 

### Unix user
```
cd build
cmake -DCMAKE_BUID_TYPE=<Debug|Release|RelWithDebInfo|MinSizeRel> ..
cmake --build . -j
```

### Windows user
```
cd build
cmake ..
cmake --build . --config <Debug|Release|RelWithDebInfo|MinSizeRel> -j
```

An additional **_cmake_** flag can be provided :
* `-DCMAKE_INSTALL_PREFIX=/path/to/install` prefixes the install path

After building the library you may install it by running : 
```
cmake --install .
```

## Create package

You can create a **_conan_** package by running :
```
conan create . <organization>/<stable|testing> -s compiler.libcxx=stdlibc++
```

This command will create a **_conan_** package by scanning your default environment; your platform and your compiler.
If you want to override some of these, you can provide additional **_conan_** command line arguments such as :
* `-s compiler=` to change the compiler. You should provide only the compiler name without the version
* `-s compiler.version=` to change the compiler version
* `-s buid_type=<Debug|Release>`
* `-e <CC|CXX>=` to change the compiler. This argument is for **_cmake_** so you must provide the complete compiler name; so the compiler name with its version.

## Upload package
### Bintray repository

First create a [bintray](https://bintray.com) account then create a **_bintray_** repository.
Second run the following commands once the **_conan_** package created properly :
```
conan remote add <name> <url>
conan user -p <token> -r <name> <account>
conan upload bigd/<version>@<organization>/<stable|testing> -r=<name> --all
```

* `<name>` is a user-defined remote name
* `<url>` is the **_bintray conan_** repository url; it looks like `https://api.bintray.com/conan/<organization>/<repository>`.
* `<token>` is the **_bintray_** token for your **_bintray_** repository.
* `<account>` is your **_bintray_** account name.

