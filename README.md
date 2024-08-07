# py-sas-studio-custom-steps: A Python package for SAS Studio Custom Steps

This repository provides a Python class and associated methods to facilitate access to the content of SAS Studio Custom Steps.  [SAS Studio Custom Steps](https://go.documentation.sas.com/doc/en/sasstudiocdc/default/webeditorcdc/webeditorsteps/titlepage.htm) are low-code components designed for a variety of analytical and data engineering operations on the SAS Viya platform.  They help users create a user interface for parameters, that can then be used to execute an associated SAS program.  Custom Steps provide easy access to common operations, boost code reusability, and help establish best practices in programming.

As SAS Viya continues to welcome a diverse set of users with different preferences (e.g. programming, low-code / no-code), a Python-based framework for interacting with custom steps aids code reusability, rapid development and testing of SAS solutions. This package can be used to access and port custom step capabilities from non-SAS Studio applications, such as [SAS Viya Workbench](https://www.sas.com/en_us/software/viya/workbench.html).

Note that SAS Viya, SAS Viya Workbench etc. refer to commercial software provided by SAS Institute.  The package in this repository is currently not officially provided or supported by SAS Institute. It only contains a convenient tool for manipulating a SAS Studio Custom Step, a serialized file.  It does not execute SAS algorithms or procedures.  SAS Programs and SAS Studio Custom Steps require a SAS / SAS Viya license to execute.


## Installation
1. Clone this repository
2. To install locally in editable mode, refer [here](https://github.com/SundareshSankaran/py-sas-studio-custom-steps/blob/main/scripts/local_install_quick_start.md)

Run the following command for a pip installation of the package from PyPi.

```shell

pip install --upgrade py-sas-studio-custom-steps

```

## Usage - quick example

To import the package inside a Python script:

```python

import py_sas_studio_custom_steps as py_sas_step

custom_step = py_sas_step.CustomStep()

```

or, as an alternative, import the object directly:

```python
from py_sas_studio_custom_steps import CustomStep

custom_step = CustomStep()
```

## Key Operations

This package will evolve and add more functionality in a gradual manner.  Important operations that are currently available include:

- *extract_sas_program:* Extract the SAS program from a given custom step
- *create_custom_step:* Write a custom step (CustomStep) object to a SAS Studio Custom Step (.step) file
- *list_keys:* List out all the attributes of a current custom step.

## Documentation
Refer this [page](https://github.com/SundareshSankaran/py-sas-studio-custom-steps/tree/main/docs/DOCUMENTATION.md) for a list of all available methods and attributes.

## Change Log
* Version: 0.1.2 (02AUG2024)
  - Initial version plus teething bug / doc fixes

## Contact
* [Sundaresh Sankaran](mailto:sundaresh.sankaran@sas.com)
