# Print CARS Data

## Description
This custom step allows users to select an input dataset, choose specific columns, and define the number of observations to display. It then prints the selected data using `PROC PRINT` in SAS Studio. 

---
## User Interface

*(Screen capture of the user interface will be available soon.)*

---
## Requirements
- SAS Viya environment with SAS Studio Flows.

---
## Usage
1. Add the step to a SAS Studio flow.
2. Configure the parameters on the **Print CARS data** tab.
3. Run the flow to display the printed data in the Results tab.

---
## Parameters

### Print CARS data
- **Select input table** (input table, optional): Choose the input table you want to print.
- **Select columns** (column selector, optional): Select the specific columns from the input table to be printed.
- **Example of a text field** (number, optional): Specify the number of observations to display.

---
## Installation & Notes
This step is part of the `sas-studio-custom-steps` collection. Follow the repository instructions in the top-level README to make custom steps available in SAS Studio.

---
## Change Log
- Version: 0.1.0 (24MAY2024)
    - Initial release.

---
## Contact
- [Sundaresh Sankaran](mailto:sundaresh.sankaran@sas.com)