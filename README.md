# PyScaffold #

**PyScaffold** is an automation script (a command line tool) written in Python 3 used for generating a C++ CMake project.

## Who should use this tool? ##

Are you experiencing the hassle of manually creating folders - build, include, lib, src, test - needed for a CMake project? Then this tool is for you.

## Features ##
  * A command-line interface that you can interact with
  * Basic set of options for creating a C++ CMake project:
    * `--project-name` lets you specify the name of the project and the directory name of the project to be created.
    * `--cmake-version` lets you specify the required minimum version of `cmake` for the compilation to be successful.
    * `--cpp-version` lets you specify the C++ standard to be used (e.g., `c++11`, `c++14`, `c++17`).
    * `--location` lets you specify the path where the project will be created.

## Limitations ##

PyScaffold is not a mature framework and is under active development. It's limitations are as follows:
* The `--help` option is not yet reliable. Options don't have descriptions in it.
* Generating of CMake project for C is not yet available.
* The directory structure of generated project is fixed. The user do not have the power to modify it via a configuration file (at least).
* This tool was developed on a Windows machine and is not yet tested on Linux.
* The `--location` option is not yet handled properly. Specifying a Windows path will cause some errors, caused specifically by the backslash not being handled as an escape character. Yet, you can use relative path names like `.` and `..`.

## References ##
* If you don't have an idea on what CMake is, you could refer to this [link](https://en.wikipedia.org/wiki/CMake). **TLDR:** It's a hassle for some C/C++ developers to use make. CMake lets you specify rules on compiling, linking and executing, and it will generate a Makefile for you.
* You could use this [tutorial](http://derekmolloy.ie/hello-world-introductions-to-cmake/) as a hands-on reference. It's presented in a straighforward manner.
* I would also like to recommend [this one](https://tuannguyen68.gitbooks.io/learning-cmake-a-beginner-s-guide/content/chap1/chap1.html) in case you're not interested in the previous tutorial link. Note that this is just a part of the tutorial series. You could proceed with the succeeding part of the series if you want to.

## Usage ##

Here is a brief example:

```bash
python pyscaffold.py --project-name cpp_tuts --cmake-version 3.4.3 --cpp-version c++17 --location ~/cpp_projects
```

* Not specifying the `--project-name` will default project name to *sample_cmake_project*.
* Not specifying the `--cmake-version` will default CMake version to *3.4.3*.
* Not specifying the `--cpp-version` will default C++ standard to *c++14*.
* Not specifying the `--location` will default project location to *current directory*. **NOTE:** The location should be a directory. Error handling is not yet implemented properly.