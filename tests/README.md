# Print CARS Data

## Description
This custom step allows users to print a subset of observations and selected columns from an input dataset (such as `SASHELP.CARS`) directly into the SAS Studio results. It serves as an easy-to-use utility for quick data inspection and reporting.

---
## User Interface

![Print CARS Data Screenshot](./img/print-cars-data-screenshot.png)

---
## Requirements
- SAS Viya environment with SAS Studio flows.
- SAS Studio monthly stable 2023.x or later.

---
## Usage
1. Add the "Print CARS Data" step to your flow.
2. Select the input table and choose the specific columns you want to display.
3. Define the number of observations you want to print.
4. Run the step to view the output.

---
## Parameters

### Input Parameters
1. **Select input table** (input table, optional): The SAS table you want to print (e.g., `SASHELP.CARS`).
2. **Select columns** (column selector, optional): Select the specific columns from the input table to be printed.
3. **Example of a text field** (number, optional): Enter the number of observations to display in the report.

---
## Installation & Notes
This step is part of the `sas-studio-custom-steps` collection. Follow the repository instructions in the top-level README to make custom steps available in SAS Studio.

---
## Change Log
- Version: 0.1.0 (24OCT2023)
    - Initial release of the Print CARS Data custom step.

---
## Contact
- [Sundaresh Sankaran](mailto:sundaresh.sankaran@sas.com)