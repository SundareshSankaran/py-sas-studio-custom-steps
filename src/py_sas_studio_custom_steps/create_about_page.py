about_page = {
			"id": "about",
			"type": "page",
			"label": "About",
			"children": [
				{
					"id": "section_about_intro",
					"type": "section",
					"label": "Provide Title of your custom step here",
					"open": True,
					"visible": "",
					"children": [
						{
							"id": "section_about_intro_text",
							"type": "text",
							"text": "Provide a brief description of your custom step here. This custom step ...",
							"visible": ""
						},
						{
							"id": "section_about_parameters",
							"type": "section",
							"label": "Parameters",
							"open": False,
							"visible": "",
							"children": [
								{
									"id": "section_about_parameters_input",
									"type": "section",
									"label": "Input Parameters",
									"open": True,
									"children": [
										{
											"id": "section_about_parameters_input_text",
											"type": "text",
											"text": "List your input parameters here as a numeric or bulleted list, separated by line breaks. For example: \n 1. input parameter 1 (input port, required): description\n 2. input parameter 2...",
											"visible": ""
										}
									]
								},
								{
									"id": "section_about_parameters_output",
									"type": "section",
									"label": "Output specification",
									"open": True,
									"visible": "",
									"children": [
										{
											"id": "section_about_parameters_output_text",
											"type": "text",
											"text": "List your input parameters here as a numeric or bulleted list, separated by line breaks. For example: \n 1. input parameter 1 (input port, required): description\n 2. input parameter 2... ",
											"visible": ""
										}
									]
								}
							]
						},
                        {
							"id": "section_references",
							"type": "section",
							"label": "References",
							"open": False,
							"children": [
								{
									"id": "references_text",
									"type": "text",
									"text": "Insert a bulleted or number list of references here."
								}
							]
						},
						{
							"id": "section_about_version",
							"type": "section",
							"label": "About this step",
							"open": True,
							"children": [
								{
									"id": "version_text",
									"type": "text",
									"text": "Version: 0.1.0 (DDMONYYYY)\nContact: Firstname Lastname (Firstname.Lastname@company.com)"
								}
							]
						}
					]
				}
			]
		}