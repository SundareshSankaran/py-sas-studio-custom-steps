starter_page = {
			"id": "page1",
			"label": "Page Template",
			"type": "page",
			"children": [
				{
					"id": "input_table",
					"type": "inputtable",
					"label": "Example of an input table:",
					"required": False,
					"placeholder": "",
					"visible": "",
					"filter": False
				},
				{
					"id": "input_table_columns",
					"type": "columnselector",
					"label": "Columns associated with the input table:",
					"include": None,
					"order": False,
					"columntype": "a",
					"max": None,
					"min": None,
					"visible": "",
					"table": "input_table"
				},
				{
					"id": "sample_text",
					"type": "text",
					"text": "This is informational text.",
					"visible": ""
				},
				{
					"id": "text_field",
					"type": "textfield",
					"label": "Example of a text field:",
					"placeholder": "",
					"required": False,
					"visible": ""
				},
				{
					"id": "text_area",
					"type": "textarea",
					"label": "Example of a text area for larger text:",
					"placeholder": "",
					"required": False,
					"visible": ""
				},
				{
					"id": "file_selector",
					"type": "path",
					"label": "Example of file or folder selector:",
					"pathtype": "file",
					"placeholder": "",
					"required": False,
					"visible": ""
				},
				{
					"id": "drop_down_list",
					"type": "dropdown",
					"label": "Example of a drop-down list:",
					"items": [
						{
							"value": "Item 1",
							"label": "Item 1"
						},
						{
							"value": "Item 2",
							"label": "Item 2"
						}
					],
					"required": False,
					"placeholder": "",
					"visible": ""
				},
				{
					"id": "list_box",
					"type": "list",
					"items": [
						{
							"value": "list box item 1",
							"label": "list box item 1"
						},
						{
							"value": "list box item 2",
							"label": "list box item 2"
						},
						{
							"value": "list box item 3",
							"label": "list box item 3"
						}
					],
					"label": "Example of a list box:",
					"max": None,
					"min": None,
					"visible": ""
				},
				{
					"id": "radio_button_group",
					"type": "radiogroup",
					"label": "Example of a radio button group for making a choice",
					"items": [
						{
							"value": "choice 1",
							"label": "choice 1"
						},
						{
							"value": "choice 2",
							"label": "choice 2"
						}
					],
					"visible": ""
				}
			]
		}

starter_page_code = """
/* SAS templated code goes here */

/* This program merely lists out all macro variables associated with the custom step's UI controls */

/* Input table control */
%put &input_table.;

/* Input table libname (automatically inferred)*/
%put &input_table_lib.;

/* Input table name (automatically inferred) */
%put &input_table_name.;

/* Columns selected by input table in space delimited format*/
%put &input_table_columns.;

/* Total number of columns selected by the column selector*/

%put &input_table_columns_count.;

/* List out all columns individually. */
%macro list_column_selector_columns;
    %do i= 1 %to &input_table_columns_count.;
        %put &&input_table_columns_&i._name.;
    %end;
%mend list_column_selector_columns;

%list_column_selector_columns;

/* The below variable will not be resolves since it only refers to the UI and not code gen */
/* %put &sample_text.; */

/* print the value of the text field */
%put &text_field.;

/* Prints out the contents of a text area which holds larger text */

%put &text_area.;

/* This macro variable holds value of the file or folder selector */
%put &file_selector.;

/* This macro variable holds values of the drop-down list box */
%put &drop_down_list.;

/* This macro refer macro variables holdng choices from a list box */

%macro list_list_box;
    %do i = 1 %to &list_box_count.;
        %put &&list_box_&i.;
    %end;
%mend list_list_box;

%list_list_box;


/* Prints out the choice of radio button group */
%put &radio_button_group.;

"""