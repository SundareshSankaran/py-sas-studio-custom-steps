# py-sas-studio-custom-steps: A Python package for SAS Studio Custom Steps

This repository provides a Python class and associated methods to create, access and manipulate SAS Studio Custom Steps.  [SAS Studio Custom Steps](https://go.documentation.sas.com/doc/en/sasstudiocdc/default/webeditorcdc/webeditorsteps/titlepage.htm) are low-code components designed for analytical and data engineering operations on the SAS Viya platform.  They provide a user interface for parameters which are then used to execute an associated SAS program.  Custom Steps provide easy access to common operations, boost code reusability, and help establish best practices in programming.

As SAS Viya continues to welcome a diverse set of users with different preferences (e.g. programming, low-code / no-code), a Python-based framework for interacting with custom steps accelerates code reusability and assists rapid development and testing of custom steps. This package can be used to access and port custom step capabilities from SAS Studio and non-SAS Studio applications, such as  [SAS Viya Workbench](https://www.sas.com/en_us/software/viya/workbench.html), Visual Studio Code, Claude Code and other Python IDEs.

Note that SAS Viya, SAS Viya Workbench etc. refer to commercial software provided by SAS Institute.  The open-source package in this repository is  not officially provided or supported by SAS Institute. It only contains a convenient tool for manipulating a SAS Studio Custom Step, a serialized file.  It does not execute SAS algorithms or procedures.  SAS programs and SAS Studio Custom Steps require a SAS / SAS Viya license to execute.

A wiki of this repo has been generated using DeepWiki and is available here: [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/SundareshSankaran/py-sas-studio-custom-steps)

## Installation
1. Clone this repository
2. To install locally in editable mode, refer [here](https://github.com/SundareshSankaran/py-sas-studio-custom-steps/blob/main/build/local_install_quick_start.md)

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

Refer this [notebook](https://github.com/SundareshSankaran/py-sas-studio-custom-steps/blob/main/scripts/example-notebook.ipynb) for a detailed example.

## Key Operations

This package will evolve and add more functionality in a gradual manner.  Important operations that are currently available include:

- *extract_sas_program:* Extract the SAS program from a given custom step
- *create_custom_step:* Write a custom step (CustomStep) object to a SAS Studio Custom Step (.step) file
- *add_starter_page* and *add_about_page*: Rapidly create a starter SAS Studio Custom Step and edit further
- *attach_sas_program:* Attaches content of a SAS program to a custom step object.
- *attach_ui:* Attaches UI component definitions to a custom step object.

and, as a bonus, some convenient generative AI functionality (note that this also requires a Gemini API Key from Google which is used to call a Gemini Flash 3.5 Large Language Model (LLM))

- *generate_readme:* Creates a README file as per user specification.
- *create_sas_program:* Creates a SAS program through an LLM's assistance based on a user prompt
- *modify_sas_program:* Modifies the SAS program component of a custom step through an LLM's assistance based on a user prompt
- *create_ui:* Creates a user interface through an LLM's assistance based on a user prompt

## Documentation
Refer this [page](https://github.com/SundareshSankaran/py-sas-studio-custom-steps/tree/main/docs/DOCUMENTATION.md) for a list of all available methods and attributes.

## Generative AI usage
Some functions (described in [Documentation](https://github.com/SundareshSankaran/py-sas-studio-custom-steps/tree/main/docs/DOCUMENTATION.md)) make use of a Large Language Model (LLM)(Gemini 3.5 Flash).  While you are free to modify the code to accommodate other LLMs, this is at present the only LLM supported.  Read this important note regarding functions that make use of Generative AI.

**IMPORTANT**: All outputs returned from Generative AI tools such as LLMs should be carefully reviewed prior to actual use.  Quality of Generative AI outputs are determined by the Large Language Model in use and may be incorrect. Always review the same.

## Convenience: tasks.json
This repository contains a tasks.json meant for use in Visual Studio Code which helps clean up temporary files and stands up a virtual environment for quick development and exploration.  Remove this file if you do not want to have Visual Studio Code run the tasks in `tasks.json`.

## Change Log
* Version: 1.0.0 (28MAY2025)
  - Major release
* Version: 0.9.9 (27MAY2025)
  - Prior to a major release
* Version: 0.5.1 (17JAN2025)
  - Method to create a README file 
* Version: 0.4.0 (09JAN2025)
  - Methods to add SAS program and UI components to a Custom Step
* Version: 0.3.3 (22SEP2024)
  - New method to return pages from a Custom Step object
* Version: 0.2.3 (07AUG2024)
  - New method to instantiate a class through a Custom Step file
* Version: 0.1.3 (07AUG2024)
  - Initial version plus teething issues / doc fixes

## Contact
* [Sundaresh Sankaran](mailto:sundaresh.sankaran@gmail.com)
