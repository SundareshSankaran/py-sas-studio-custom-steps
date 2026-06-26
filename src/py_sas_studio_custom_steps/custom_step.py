class CustomStep:
    """This class helps you perform operations on a SAS Studio Custom Step programmatically"""
    def __init__(self, custom_step_file = None, name=None,creationTimeStamp=None, modifiedTimeStamp=None, createdBy=None, modifiedBy=None, displayName=None, localDisplayName=None, properties=None, links=None, metadataVersion=None, version=None, type=None, flowMetadata=None, ui={"showPageContentOnly": True, "pages": []}, templates={"SAS":""}) -> object:
        import json
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
        self.ui=json.dumps({"showPageContentOnly": True, "pages": []})
        self.templates={"SAS":""}

        # Load atttributes present in a custom step file
        if custom_step_file:
            self.load_step_file(custom_step_file)
        else:
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
            self.ui=json.dumps(ui) if ui else self.ui
            self.templates=templates if templates else self.templates

    def __setitem__(self, key, value):
        setattr(self, key, value)
   
    def create_custom_step(self, custom_step_path) -> str:
        """This function writes a CustomStep object to a SAS Studio Custom Step file at a desired path."""
        import json
        try:
            with open(custom_step_path,"w", encoding="utf-8") as f:
                json.dump(self.__dict__, f)
            return f"Custom Step created at {custom_step_path}"
        except Exception as e:
            return f"Error occurred while creating custom step: {e}"
        

    def extract_sas_program(self,custom_step_file: str = None) -> str:
        """This function extracts and returns either its own SAS program portion or that of a custom step file.  Provide the full path or URLto the custom step as an argument."""
        if custom_step_file is None:
            step_data = self.__dict__
        else:
            step_data = self.load_step_file(custom_step_file)
        return step_data["templates"]["SAS"]
    
    def extract_ui(self,custom_step_file: str = None) -> str:
        """This function extracts and returns the UI configuration of a custom step file.  Provide the full path or URL to the custom step as an argument."""
        if not custom_step_file:
            step_data = self.__dict__
        else:
            step_data = self.load_step_file(custom_step_file)
        return step_data["ui"]
    
    def attach_sas_program(self,sas_file) -> str:
        """This function extracts the contents of a given SAS program and attaches it to the SAS program template key of a custom step object.  Provide the full path to the SAS program as an argument."""
        try:
            with open(sas_file,"r") as sas_f:
                self["templates"]={"SAS":sas_f.read()}
            return "Custom step object updated with SAS program template from "+sas_file
        except Exception as e:
            return f"Error occurred while attaching SAS program: {e}"

    def attach_ui(self,ui_json_file) ->str:
        """This function attaches a given UI configuration to the UI key of a custom step object.  Provide the full path to a JSON file with components as an argument."""
        import json
        try:
            with open(ui_json_file,"r") as f:
                js = json.load(f)
            jsd = json.dumps(js)
            self["ui"]=jsd
            return "Custom step object updated with UI configuration from "+ui_json_file
        except Exception as e:
            return f"Error occurred while attaching UI configuration: {e}"

    def get_pages(self) -> list:
        """This function returns all pages in a CustomStep object. Introduced v0.3.3"""
        import json
        pages = []
        ui = json.loads(self.__dict__["ui"])
        for page in ui["pages"]:
            pages.append(page)
        return pages

    def list_keys(self)->list:
        """This function lists and returns all keys forming part of a CustomStep object."""
        keys = []
        for key in self.__dict__:
            print(key)
            keys.append(key)
        return keys

    def load_step_file(self, custom_step_file)->object:
        "This functions loads a custom step object with attributes contained in a custom step file, either local or from a URL."
        import json
        from pathlib import Path
        from urllib.parse import urlparse
        import requests
        parsed = urlparse(custom_step_file)
        if parsed.scheme in ("http", "https"):
            url = custom_step_file
            if "github.com" in parsed.netloc and "/blob/" in parsed.path:
                url = custom_step_file.replace("github.com/", "raw.githubusercontent.com/").replace("/blob/", "/")
            response = requests.get(url)
            response.raise_for_status()
            step_data = response.json()
        else:
            with open(custom_step_file,"r", encoding="utf-8") as step_file:
                step_data = json.load(step_file)
        for key, value in step_data.items():
            self[key]=value
        return step_data
    
    def add_about_page(self) -> str:
        """This function adds a templated About page to the UI of a custom step object."""
        from .create_about_page import about_page
        import json
        ui = json.loads(self.__dict__["ui"])
        for pages in ui["pages"]:
            if pages.get("id") == about_page.get("id"):
                return "About page already exists in the UI."
        ui["pages"].append(about_page)
        self["ui"]=json.dumps(ui)
        return "About page added to the UI."
    
    def add_starter_page(self) -> str:
        """This function adds a starter page to the UI of a custom step object."""
        from .create_starter_page import starter_page
        import json
        ui = json.loads(self.__dict__["ui"])
        for pages in ui["pages"]:
            if pages.get("id") == starter_page.get("id"):
                return "Starter page already exists in the UI. "
        ui["pages"].append(starter_page)
        self["ui"]=json.dumps(ui)
        return "Starter page added to the UI."

    def create_sas_program(self, prompt: str) -> str:
        """This function creates a SAS program based on a given prompt using Gemini API, and attaches it to the SAS program template key of a custom step object.  Provide the prompt as an argument."""
        from .gemini_api import generate_sas_code
        try:
            sas_code = generate_sas_code(f"User prompt: {prompt}\n\n Current UI configuration:{self.__dict__['ui']}")
            self["templates"]={"SAS":sas_code}
            return "Program generated and attached to the custom step object successfully."
        except Exception as e:
            return f"Error occurred: {e}"   

    def create_ui(self, prompt: str) -> str:
        """This function creates a UI configuration based on a given prompt using Gemini API, and attaches it to the SAS program template key of a custom step object.  Provide the prompt as an argument."""
        from .gemini_api import generate_ui
        try:
            ui_config = generate_ui(f"User prompt: {prompt}\n\n Current SAS code:{self.__dict__['templates']['SAS']}")
            self["ui"]= ui_config
            return "UI configuration generated and attached to the custom step object successfully."
        except Exception as e:
            return f"Error occurred: {e}"

    def modify_sas_program(self, prompt: str) -> str:
        """This function modifies a SAS program based on a given prompt using Gemini API, and attaches it to the SAS program template key of a custom step object.  Provide the prompt as an argument."""
        from .gemini_api import modify_sas_code
        try:
            sas_code = modify_sas_code(f"User prompt: {prompt}\n\nCurrent SAS code:\n{self.__dict__['templates']['SAS']}\n\nCurrent UI config:\n{self.__dict__['ui']}")
            self["templates"]={"SAS":sas_code}
            return "SAS program modified"
        except Exception as e:
            return f"Error occurred: {e}"
    
    def generate_readme(self, prompt:str, readme_file:str)-> str:
        """This function generates a README file for a custom step object using a Large Language Model. . Provide the full path to the README file as an argument."""
        from .gemini_api import generate_readme
        try:
            readme_template = generate_readme(self.__dict__['ui'], self.__dict__['templates']['SAS'], prompt)
            with open(readme_file,"w", encoding="utf-8") as f:
                f.write(readme_template)
            return f"README file generated at {readme_file}"
        except Exception as e:
            return f"Error occurred: {e}"
        
    def change_name(self, new_name: str) -> str:
        """This function changes the name of a custom step object. Provide the new name as an argument."""
        try:
            self["name"] = new_name
            return f"Name changed to {new_name}"
        except Exception as e:
            return f"Error occurred: {e}"