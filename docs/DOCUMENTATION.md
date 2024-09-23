# Package Documentation

## Methods

### extract_sas_program
*extract_sas_program(self, custom_step_file)*

This function extracts and returns the SAS program portion of a custom step file.  Provide the full path to the custom step as an argument.

**Inputs**
1. self:  CustomStep() object
2. custom_step_file:  Path to a SAS Studio Custom Step file

**Returns**
- String

----

### load_step_file
*load_step_file(self, custom_step_file)*

This functions loads a custom step object with attributes contained in a custom step file (.step).  Provide the full path to the custom step as an argument.

**Inputs**
1. self:  CustomStep object
2. custom_step_file:  Path to a SAS Studio Custom Step file

**Returns**
- CustomStep

----


### create_custom_step
*create_custom_step(self, custom_step_path)*

This function writes a CustomStep object to a SAS Studio Custom Step file at a desired path.

**Inputs**
1. self:  CustomStep object
2. custom_step_path:  Path to a SAS Studio Custom Step file that will get created.

----

### list_keys
*list_keys(self, custom_step_file)*

This function lists and returns all keys forming part of a CustomStep object.

**Input**
- self:  CustomStep object

**Returns**
- List

----

### get_pages
*get_pages(self)*

This function returns all pages provided in a CustomStep object. Introduced v0.3.3

**Input**
- self:  CustomStep object

**Returns**
- List

----

## Objects

### CustomStep

**Attributes of a CustomStep object**

*The current operations covered by this package do not require knowledge of all attributes of a SAS Studio Custom Step, and therefore only some of them are described here.  This should not be interpreted as official documentation of a SAS Studio Custom Step.*

1. name: name of the Custom Step
2. creationTimeStamp: date the custom step file was created.
3. modifiedTimeStamp: date the custom step file was last modified.
4. createdBy: ID of the creator of the custom step.
5. modifiedBy: ID of the user who last modified the custom step.
6. displayName: name shown on the title of the custom step.
7. localDisplayName
8. properties
9. links
10. metadataVersion
11. version
12. type
13. flowMetadata
14. ui: section containing the custom step prompt
15. templates: section containing the code generation for the custom step.  SAS Programs are identified by a further key called 'SAS'
16. custom_step_file: a path to a SAS Studio Custom Step provided at time of initialisation.  Passed with double quotes.