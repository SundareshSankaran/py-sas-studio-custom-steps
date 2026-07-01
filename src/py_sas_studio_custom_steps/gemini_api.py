

def generate_sas_code(user_prompt: str, current_ui_config: dict = None, current_sas_code: str = None) -> str:
    """This function generates a SAS program based on a given user prompt using the Gemini API."""
    import os
    import json
    from google import genai
    from dotenv import load_dotenv
    load_dotenv()  # Load environment variables from .env file

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    system_prompt = """
        Generate a SAS program (meant for execution in a SAS Studio custom step) based on user input, the 
        current UI configuration and current SAS code where provided. Follow a parameterised approach where input parameters, output datasets
        and reports are represented as macro variables rather than hard coded.
        Return only the SAS code without background explanation or markdown.  
        If current SAS code is provided, treat it as a code improvement opportunity keeping the objective in mind.
        If current UI configuration is provided, ensure alignment of UI controls with macro variables in the SAS code.
        The SAS code should be commented and indented for usability.
        The SAS Code always starts with a docstring comment block which explains the purpose of the code, input parameters and output. Should also include Author name and version in Version X.X.X (DDMONYYYY) format.
        An example response for a hypothetical user prompt is as follows.
        Example prompt: I want to create a summary dataset which aggregates an input table by one or more groupby variables. Aggregation metrics are sum and max.
        Example response:

        /************************************************************************
        Aggregate Input Table

        Purpose: This SAS program aggregates an input dataset by specified groupby variables and computes specified aggregation metrics.
        Input Parameters:
        - input_table: Name of the input dataset (macro variable)
        - groupby_vars: List of groupby variables, separated by spaces (macro variable)
        - aggregation_metrics: List of aggregation metrics (e.g. sum, max), separated by spaces (macro variable)
        Output:
        - output_table: Name of the output summary dataset (macro variable)

        Created: [Author Name]
        Version: 1.0.0 (12MAR2026)
        ************************************************************************/;
        /* Define macro variables for input parameters */
        %let input_table=; /* Name of the input dataset */
        %let groupby_vars=; /* List of groupby variables, separated by spaces */
        %let aggregation_metrics=; /* List of aggregation metrics (e.g. sum, max), separated by spaces */
        %let output_table=; /* Name of the output summary dataset */

        /************************************************************************
        EXECUTION CODE
        ************************************************************************/;

        /* Create summary dataset with dynamic groupby and aggregation */
        proc sql;
            create table &output_table. as
            select 
                &groupby_vars,
                %if %index(&aggregation_metrics., sum) > 0 %then sum(var) as sum_var,
                %if %index(&aggregation_metrics., max) > 0 %then max(var) as max_var,
                count(*) as count
            from &input_table.
            group by &groupby_vars.;
        quit;


        """


    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=system_prompt + "\n\n" + user_prompt + "\n\n current UI configuration:\n\n" + json.dumps(current_ui_config) + "\n\n current SAS Code:\n\n" + current_sas_code
    )
    sas_code = response.text
    return sas_code

def modify_sas_code(user_prompt: str) -> str:
    """This function modifies a given SAS program based on a user prompt using the Gemini API."""
    import os
    from google import genai
    from dotenv import load_dotenv
    load_dotenv()  # Load environment variables from .env file

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    system_prompt = """
        A SAS program (meant for execution in a SAS Studio custom step) along with some user instructions shall be provided. 
        Improve or modify the SAS program based on user instructions.
        Instructions may or may not include the current UI configuration. Use it if available to better understand 
        the context of code and modifications. Ensure alignment of UI controls with macro variables.
        Return only the SAS code without background explanation or markdown.  
        The SAS code should be commented and indented for usability.
        """


    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=system_prompt + "\n\n" + user_prompt
    )
    sas_code = response.text
    return sas_code

def generate_ui(user_prompt: str) -> str:
    """This function generates a UI configuration based on a given user prompt using the Gemini API."""
    import os
    from google import genai
    from .create_starter_page import starter_page, starter_page_code
    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    system_prompt = f"""
        Using the given step ui configuration as an example, generate a SAS Studio Custom step UI definition which addresses provided user specifications.  
        The main values you should look to modify are the ID (id) values which correspond to macro variables used in the 
        corresponding SAS code, and the type of controls (of which the ones provided in the step are only examples. 
        The other aspect is that of how closely they align with the SAS code, for example, if a macro variable points to a dataset in the 
        SAS code, the control is best suited as an input table. 
        The context might or might not contain current SAS code, but if it does, please use it to guide the design of the UI.
        Return only the UI configuration (in a json structure) without background explanation or markdown.  The structure of the json is sacrosanct. 
        
        The following example UI configuration and corresponding SAS program are meant to be used as a guide.

        Example UI configuration (in pseudo-json for readability):
         {{ showPageContentOnly : true,  pages : [  {starter_page}],  syntaxversion :  1.3.0 ,  values :  input_table :  {{      library :   , table :    }} ,     input_table_columns : [],   text_field :   ,  text_area :   ,   file_selector :   ,   drop_down_list : null,  list_box : [],  radio_button_group :  {{  value :  choice 1 , label :  choice 1 }},  promptHierarchies : [] }}

        Example SAS code:
        {starter_page_code}

        """


    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=system_prompt + "\n\nUser prompt: \n\n" + user_prompt
    )
    ui_config = response.text
    return ui_config

def generate_readme(ui_config: dict, sas_program: str,user_prompt: str) -> str:
    """This function generates a markdown README.md file based on a given user prompt using the Gemini API."""
    import os
    from google import genai
    from dotenv import load_dotenv
    load_dotenv()  # Load environment variables from .env file

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    system_prompt = f"""
        Using the provided SAS studio custom step attributes containing the UI configuration, SAS code and additional user instructions, generate a README.md file in markdown format.  An example README.md file format is provided for reference.
        Example README.md:

        # DuckDB - Extract Parquet Metadata

        ## Description
        This custom step extracts and outputs metadata from input parquet files. It also gives you an option to load this output to a SAS Cloud Analytics Services (CAS) table for visualisation. Visualising this output in applications like SAS Visual Analytics helps us understand if the parquet metadata and rowgroup structure need adjustment to yield faster query performance.  Then, based on user-specified parameters, this step can write parquet files reflecting changed metadata, particularly sorting information and rowgroups. Users may also choose to partition the file by specifying partitioning columns.  The step uses the SAS/ACCESS Interface to DuckDB and DuckDB's functions to work with parquet files.
        Open file formats such as Parquet are popular due to benefits they offer in reduced data footprint and columnar structure.  Also, DuckDB is a popular and performant query processing engine that reduces data movement. Parquet functions in DuckDB are useful tools that assist better use of parquet file metadata.

        ---
        ## User Interface

        (Watch out for a more detailed walkthrough soon.)

        ![Feast Your Eyes](./img/parquet-extract-metadata-holding-screenshot_1.png)
        ---
        ## Requirements
        - SAS Viya environment with SAS Studio flows (step tested on monthly stable 2026.01)
        - SAS/ACCESS Interface to DuckDB configured on the compute server. Note that SAS supports DuckDB from monthly stable 2025.07 onwards.
        ---
        ## Usage
        Configure the parameters as needed in the Parameters tab and run the step.
        ---
        ## Parameters
        ### Source Parameters
        - Path to parquet file(file selector, required): select only files on the SAS server (i.e. the filesystem). Based on earlier selection, this could be a single parquet file or a folder comprising multiple files.
        ### Target Parameters 
        1. Output table (output port, required): connect an output table to the output port for holding schema results.  
        2. Load to CAS (checkbox, optional): if checked, the output table is loaded to Cloud Analytics Services (and promoted to global scope) for visualisation. The default table is PARQUET_METADATA in PUBLIC caslib (can be changed by user). 
        Visualising this output in applications like SAS Visual Analytics helps us understand if  parquet metadata or rowgroup structure needs adjustment to yield faster query performance. The Load-to-CAS option is provided as part of this custom step as a convenience (to remind you of this quick option for visualisation rather than scrolling through a long table in case of many rowgroups).  Even if you choose not to load to CAS at this stage, you can always load the output table later through the [Load to CAS](https://github.com/sassoftware/sas-studio-custom-steps/tree/main/CAS%20-%20Load%20to%20CAS) custom step also available in this repo.
        ---
        ## Installation & Notes
        This step is part of the `sas-studio-custom-steps` collection. Follow the repository instructions in the top-level README to make custom steps available in SAS Studio.
        ---
        ## Change Log
        Reflects most recent update.  For previous updates, refer detailed changelog [here](./extras/CHANGELOG.md).
        - Version: 1.0.0 (12MAR2026)
            - Added option to define partitioning variables for file copy
        Generative AI assistance: GPT-4.1 through GitHub Copilot for code structuring
        ---
        ## Contact
        - [Firstname Lastname](mailto:Firstname.Lastname@sas.com)

        """


    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"{system_prompt}\n\nUser prompt: \n\n{user_prompt}\nExample SAS code:\n {sas_program}\n  Example UI Configuration: \n{ui_config}"
    )
    ui_config = response.text
    return ui_config