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

PyScaffold is not a mature framrework to date. It's limitations are as follows:
* The `--help` option is not yet reliable. Options don't have descriptions in it.
* Generating of CMake project for C is not yet available.
* The directory structure of generated project is fixed. The user do not have the power to modify it via a configuration file (at least).
* This tool was developed on a Windows machine and is not yet tested on Linux.
* The `--location` option is not yet handled properly. Specifying a Windows path will cause some errors, caused specifically by the backslash not being handled as an escape character. Yet, you can use relative path names like `.` and `..`.