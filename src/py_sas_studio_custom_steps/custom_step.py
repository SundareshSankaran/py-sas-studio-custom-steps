class CustomStep:
    """This class helps you perform operations on a SAS Studio Custom Step programmatically"""
    def __init__(self, custom_step_file = None, name=None,creationTimeStamp=None, modifiedTimeStamp=None, createdBy=None, modifiedBy=None, displayName=None, localDisplayName=None, properties=None, links=None, metadataVersion=None, version=None, type=None, flowMetadata=None, ui=None, templates=None) -> None:

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
        self.type=None
        self.flowMetadata=None
        self.ui=None
        self.templates=None

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
   
    def extract_sas_program(self,custom_step_file):
        """This function extracts and returns the SAS program portion of a custom step file.  Provide the full path to the custom step as an argument."""
        step_data = self.load_step_file(custom_step_file)
        return step_data["templates"]["SAS"]
    
    def load_step_file(self, custom_step_file):
        "This functions loads a custom step object with attributes contained in a custom step file"
        import json
        with open(custom_step_file) as step_file:
            step_data = json.load(step_file)
        for key in step_data:
            self[key]=step_data[key]
        return step_data
    
    def create_custom_step(self, custom_step_path):
        """This function writes a CustomStep object to a SAS Studio Custom Step file at a desired path."""
        import json
        with open(custom_step_path,"w") as f:
            json.dump(self.__dict__, f)
        print(f"Custom Step created at {custom_step_path}")
    
    def list_keys(self):
        """This function lists and returns all keys forming part of a CustomStep object."""
        keys = []
        for key in self.__dict__:
            print(key)
            keys.append(key)
        return keys
    