# py-sas-studio-custom-steps: A Python package for SAS Studio Custom Steps

This repository provides a Python class and associated methods to facilitate operations on SAS Studio Custom Steps.  [SAS Studio Custom Steps](https://go.documentation.sas.com/doc/en/sasstudiocdc/default/webeditorcdc/webeditorsteps/titlepage.htm) are low-code components designed for a variety of analytical and data engineering operations on the SAS Viya platform.  They help users create a user interface for easy provision of parameters, that can then be used to execute an associated SAS program.  Custom Steps provide easy access to common operations, boost code reusability, and help establish best practices in programming.

As SAS Viya continues to welcome a diverse set of users with different preferences (e.g. programming vs. low-code / no-code), a Python-based framework for interacting with custom steps will aid code reusability, rapid development and testing of SAS solutions. This package can also be used to access and port custom step capabilities from non-SAS Studio applications, such as [SAS Viya Workbench](https://www.sas.com/en_us/software/viya/workbench.html).

## Installation
1. Clone this repository
2. Run the following command for a  pip installation of the package from a local path in editable mode.

```shell

pip install -e .

```

**Future:** We plan to make this package available through PyPi in future, which would facilitate a direct pip install without having to clone this repository.

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


## Change Log
* Version: 0.1.0 (31JUL2024)

## Contact
* [Sundaresh Sankaran](sundaresh.sankaran@sas.com)
