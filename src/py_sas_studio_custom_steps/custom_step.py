class CustomStep:
    """This class helps you perform operations on a SAS Studio Custom Step programmatically"""
    def __init__(self, name=None,creationTimeStamp=None, modifiedTimeStamp=None, createdBy=None, modifiedBy=None, displayName=None, localDisplayName=None, properties=None, links=None, metadataVersion=None, version=None, type=None, flowMetadata=None, ui=None, templates=None) -> None:
        import uuid
        self.name=name if name else f"Auto_Generated_{uuid.uuid4()}"
        self.creationTimeStamp=creationTimeStamp
        self.modifiedTimeStamp=modifiedTimeStamp
        self.createdBy=createdBy
        self.modifiedBy=modifiedBy
        self.displayName=displayName
        self.localDisplayName=localDisplayName
        self.properties=properties
        self.links=links
        self.metadataVersion=metadataVersion
        self.version=version
        self.type=type
        self.flowMetadata=flowMetadata
        self.ui=ui
        self.templates=templates

    def __setitem__(self, key, value):
        setattr(self, key, value)
   
    def extract_sas_program(self,custom_step_file):
        """This function extracts and returns the SAS program portion of a custom step file.  Provide the full path to the custom step as an argument."""
        import json
        with open(custom_step_file) as step_file:
            step_data = json.load(step_file)
        self.name = step_data["name"]
        for key in step_data:
            self[key]=step_data[key]
        return step_data["templates"]["SAS"]
    
    def list_keys(self):
        """This function lists all keys forming part of a CustomStep object."""
        for key in self.__dict__:
            print(key)