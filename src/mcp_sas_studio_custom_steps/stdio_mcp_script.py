import os
import json
import sys
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Add the source directory to the path to import CustomStep
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'py_sas_studio_custom_steps'))

from py_sas_studio_custom_steps import CustomStep

load_dotenv()

mcp = FastMCP("py-sas-studio-custom-steps", json_response=True)

# Global CustomStep instance - shared across all tool calls
_custom_step_instance = None

def get_custom_step():
    """Get or create the global CustomStep instance."""
    global _custom_step_instance
    if _custom_step_instance is None:
        _custom_step_instance = CustomStep()
    return _custom_step_instance


# =============================================================================
# MCP TOOLS - Generated from CustomStep public methods
# =============================================================================

@mcp.tool()
def add_about_page() -> str:
    """
    Add a templated About page to the UI of a custom step object.
    
    This function adds a templated About page to the UI of a custom step object.
    """
    try:
        step = get_custom_step()
        result = step.add_about_page()
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def add_starter_page() -> str:
    """
    Add a starter page to the UI of a custom step object.
    
    This function adds a starter page to the UI of a custom step object.
    """
    try:
        step = get_custom_step()
        result = step.add_starter_page()
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def attach_sas_program(sas_file: str) -> str:
    """
    Extract and attach a SAS program from a file to the custom step object.
    
    This function extracts the contents of a given SAS program and attaches it 
    to the SAS program template key of a custom step object. Provide the full 
    path to the SAS program as an argument.
    
    Args:
        sas_file: Full path to the SAS program file
    """
    try:
        step = get_custom_step()
        result = step.attach_sas_program(sas_file)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def attach_ui(ui_json_file: str) -> str:
    """
    Attach a UI configuration to the custom step object.
    
    This function attaches a given UI configuration to the UI key of a custom 
    step object. Provide the full path to a JSON file with components as an argument.
    
    Args:
        ui_json_file: Full path to a JSON file with UI components
    """
    try:
        step = get_custom_step()
        result = step.attach_ui(ui_json_file)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def create_custom_step(custom_step_path: str) -> str:
    """
    Write the CustomStep object to a SAS Studio Custom Step file.
    
    This function writes a CustomStep object to a SAS Studio Custom Step file 
    at a desired path.
    
    Args:
        custom_step_path: Desired file path for the custom step
    """
    try:
        step = get_custom_step()
        result = step.create_custom_step(custom_step_path)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def create_sas_program(prompt: str) -> str:
    """
    Create a SAS program based on a prompt using Gemini API.
    
    This function creates a SAS program based on a given prompt using Gemini API, 
    and attaches it to the SAS program template key of a custom step object.
    
    Args:
        prompt: The prompt describing the SAS program to create
    """
    try:
        step = get_custom_step()
        result = step.create_sas_program(prompt)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def create_ui(prompt: str) -> str:
    """
    Create a UI configuration based on a prompt using Gemini API.
    
    This function creates a UI configuration based on a given prompt using 
    Gemini API, and attaches it to the UI key of a custom step object.
    
    Args:
        prompt: The prompt describing the UI configuration to create
    """
    try:
        step = get_custom_step()
        result = step.create_ui(prompt)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def extract_sas_program(custom_step_file: str = None) -> str:
    """
    Extract and return the SAS program portion of a custom step.
    
    This function extracts and returns either its own SAS program portion or 
    that of a custom step file. Provide the full path or URL to the custom step 
    as an argument.
    
    Args:
        custom_step_file: Full path or URL to the custom step file (optional)
    """
    try:
        step = get_custom_step()
        result = step.extract_sas_program(custom_step_file)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def extract_ui(custom_step_file: str = None) -> str:
    """
    Extract and return the UI configuration of a custom step.
    
    This function extracts and returns the UI configuration of a custom step file. 
    Provide the full path or URL to the custom step as an argument.
    
    Args:
        custom_step_file: Full path or URL to the custom step file (optional)
    """
    try:
        step = get_custom_step()
        result = step.extract_ui(custom_step_file)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def generate_readme(prompt: str, readme_file: str) -> str:
    """
    Generate a README file for the custom step using a Large Language Model.
    
    This function generates a README file for a custom step object using a Large 
    Language Model. Provide the prompt and the full path to the README file as arguments.
    
    Args:
        prompt: The prompt describing the custom step
        readme_file: Full path to the README file to generate
    """
    try:
        step = get_custom_step()
        result = step.generate_readme(prompt, readme_file)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def get_pages() -> list:
    """
    Get all pages in the CustomStep object.
    
    This function returns all pages in a CustomStep object. 
    Introduced in v0.3.3.
    """
    try:
        step = get_custom_step()
        result = step.get_pages()
        return result if result else []
    except Exception as e:
        return [f"Error: {str(e)}"]


@mcp.tool()
def list_keys() -> list:
    """
    List all keys forming part of the CustomStep object.
    
    This function lists and returns all keys that are part of the CustomStep object.
    """
    try:
        step = get_custom_step()
        result = step.list_keys()
        return result if result else []
    except Exception as e:
        return [f"Error: {str(e)}"]


@mcp.tool()
def load_step_file(custom_step_file: str) -> str:
    """
    Load a custom step object from a file.
    
    This function loads a custom step object with attributes contained in a 
    custom step file, either local or from a URL.
    
    Args:
        custom_step_file: Full path or URL to the custom step file
    """
    try:
        step = get_custom_step()
        result = step.load_step_file(custom_step_file)
        return str(result) if result else "Step file loaded successfully"
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def modify_sas_program(prompt: str) -> str:
    """
    Modify the SAS program based on a prompt using Gemini API.
    
    This function modifies a SAS program based on a given prompt using Gemini API, 
    and attaches it to the SAS program template key of a custom step object.
    
    Args:
        prompt: The prompt describing modifications to make to the SAS program
    """
    try:
        step = get_custom_step()
        result = step.modify_sas_program(prompt)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()