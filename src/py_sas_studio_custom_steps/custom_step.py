class CustomStep:
    """This class helps you perform operations on a SAS Studio Custom Step programmatically"""
    def __init__(self, custom_step_file = None, name=None,creationTimeStamp=None, modifiedTimeStamp=None, createdBy=None, modifiedBy=None, displayName=None, localDisplayName=None, properties=None, links=None, metadataVersion=None, version=None, type=None, flowMetadata=None, ui=None, templates={"SAS":""}) -> None:

        # Initialisation of attributes
        self.name=None 
        self.creationTimeStamp=None 
        self.modifiedTimeStamp=None 
        self.createdBy=None
        self.modifiedBy=None
        self.displayName=None
        self.localDisplayName=None
        self.properties=None
        self.links=None
        self.metadataVersion=None
        self.version=None
        self.type="code"
        self.flowMetadata=None
        self.ui=None
        self.templates={"SAS":""}

        # Load atttributes present in a custom step file
        if custom_step_file:
            #Load file
            import json
            with open(custom_step_file) as step_file:
                step_data = json.load(step_file)
            for key in step_data:
                self[key]=step_data[key]

        # Assign attributes which have been provided
        import uuid
        self.name=name if name else f"Auto_Generated_{uuid.uuid4()}"
        self.creationTimeStamp=creationTimeStamp if creationTimeStamp else self.creationTimeStamp 
        self.modifiedTimeStamp=modifiedTimeStamp if modifiedTimeStamp else self.modifiedTimeStamp
        self.createdBy=createdBy  if createdBy else self.createdBy
        self.modifiedBy=modifiedBy if modifiedBy else self.modifiedBy
        self.displayName=displayName if displayName else self.displayName
        self.localDisplayName=localDisplayName if localDisplayName else self.localDisplayName
        self.properties=properties if properties else self.properties
        self.links=links if links else self.links
        self.metadataVersion=metadataVersion if metadataVersion else self.metadataVersion
        self.version=version if version else self.version
        self.type=type if type else self.type
        self.flowMetadata=flowMetadata if flowMetadata else self.flowMetadata
        self.ui=ui if ui else self.ui
        self.templates=templates if templates else self.templates

    def __setitem__(self, key, value):
        setattr(self, key, value)
   
    def create_custom_step(self, custom_step_path):
        """This function writes a CustomStep object to a SAS Studio Custom Step file at a desired path."""
        import json
        with open(custom_step_path,"w") as f:
            json.dump(self.__dict__, f)
        print(f"Custom Step created at {custom_step_path}")

    def extract_sas_program(self,custom_step_file):
        """This function extracts and returns the SAS program portion of a custom step file.  Provide the full path to the custom step as an argument."""
        step_data = self.load_step_file(custom_step_file)
        return step_data["templates"]["SAS"]
    
    def attach_sas_program(self,sas_file):
        """This function extracts the contents of a given SAS program and attaches it to the SAS program template key of a custom step object.  Provide the full path to the SAS program as an argument."""
        with open(sas_file,"r") as sas_f:
            self["templates"]={"SAS":sas_f.read()}
        return self
    
    def attach_ui(self,ui_json_file):
        """This function attaches a given UI configuration to the UI key of a custom step object.  Provide the full path to a JSON file with components as an argument."""
        import json
        with open(ui_json_file,"r") as f:
             js = json.load(f)
        jsd = json.dumps(js)
        self["ui"]=jsd
        return self
        
    def get_pages(self):
        """This function returns all pages provided in a CustomStep object. Introduced v0.3.3"""
        import json
        pages = []
        ui = json.loads(self.__dict__["ui"])
        for page in ui["pages"]:
            pages.append(page)
        return pages

    def list_keys(self):
        """This function lists and returns all keys forming part of a CustomStep object."""
        keys = []
        for key in self.__dict__:
            print(key)
            keys.append(key)
        return keys

    def load_step_file(self, custom_step_file):
        "This functions loads a custom step object with attributes contained in a custom step file"
        import json
        with open(custom_step_file) as step_file:
            step_data = json.load(step_file)
        for key in step_data:
            self[key]=step_data[key]
        return step_data
    
    def generate_readme(self, readme_file, description, trigger_name=""):
        """This function generates a README file for a custom step object. Provide the full path to the README file as an argument."""
        readme_template = (f"# {self.displayName}\n"
                           f"{description}\n"
                           "## A general idea\n\n"
                           "----\n"
                           "## Table of Contents\n\n"
                           "----\n"
                           "## Requirements\n\n"
                           "-----\n"
                           "## Parameters\n\n"
                           "-----\n"
                           "## Run-time Control\n"
                           "Note: Run-time control is optional.  You may choose whether to execute the main code of this step or not, based on upstream conditions set by earlier SAS programs.  This includes nodes run prior to this custom step earlier in a SAS Studio Flow, or a previous program in the same session.\n\n"
                           "Refer this blog (https://communities.sas.com/t5/SAS-Communities-Library/Switch-on-switch-off-run-time-control-of-SAS-Studio-Custom-Steps/ta-p/885526) for more details on the concept.\n"
                           "The following macro variable,\n"
                           "```sas\n"
                           f"{trigger_name}_run_trigger\n"
                           "```\n"
                           "will initialize with a value of 1 by default, indicating an 'enabled' status and allowing the custom step to run.\n"
                           "If you wish to control execution of this custom step, include code in an upstream SAS program to set this variable to 0.  This 'disables' execution of the custom step.\n"
                           "To 'disable' this step, run the following code upstream:\n"
                           "```sas\n"
                           f"%global {trigger_name}_run_trigger;\n"
                           f"%let {trigger_name}_run_trigger = 0;\n"
                           "```\n"
                           "To 'enable' this step again, run the following (it's assumed that this has already been set as a global variable):\n"
                           "```sas\n"
                           f"%let {trigger_name}_run_trigger = 1;\n"
                           "```\n"
                           "IMPORTANT: Be aware that disabling this step means that none of its main execution code will run, and any  downstream code which was dependent on this code may fail.  Change this setting only if it aligns with the objective of your SAS Studio program.\n"                           
                           "-----\n"
                           "## Documentation\n\n"
                           "-----\n"
                           "## SAS Program\n\n"
                           "Refer [here]() for the SAS program used by the step.  You'd find this useful for situations where you wish to execute this step through non-SAS Studio Custom Step interfaces such as the [SAS Extension for Visual Studio Code](https://github.com/sassoftware/vscode-sas-extension), with minor modifications.\n"
                           "-----\n"
                           "## Installation & Usage\n\n"
                           "- Refer to the [steps listed here](https://github.com/sassoftware/sas-studio-custom-steps#getting-started---making-a-custom-step-from-this-repository-available-in-sas-studio).\n"
                           "----\n"
                           "## Created/contact:\n\n"
                           f"- Created by {self.createdBy}\n"
                           "----\n"
                           "## Change Log\n"
                           f"* Version {self.version}({self.modifiedTimeStamp})\n    - <Enter changes here>"
                           )
            
        with open(readme_file,"w") as f:
            f.write(readme_template)
        print(f"README file generated at {readme_file}")

    