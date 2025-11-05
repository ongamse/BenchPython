'''
OWASP Benchmark for Python v0.1

This file is part of the Open Web Application Security Project (OWASP) Benchmark Project.
For details, please see https://owasp.org/www-project-benchmark.

The OWASP Benchmark is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation, version 3.

The OWASP Benchmark is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

  Author: Theo Cartsonis
  Created: 2025
'''

from flask import redirect, url_for, request, make_response, render_template
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/xpathi-01/BenchmarkTest00823', methods=['GET'])
	def BenchmarkTest00823_get():
		return BenchmarkTest00823_post()

	@app.route('/benchmark/xpathi-01/BenchmarkTest00823', methods=['POST'])
	def BenchmarkTest00823_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00823")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf33668 = configparser.ConfigParser()
		conf33668.add_section('section33668')
		conf33668.set('section33668', 'keyA-33668', 'a-Value')
		conf33668.set('section33668', 'keyB-33668', param)
		bar = conf33668.get('section33668', 'keyB-33668')

		import elementpath
		import xml.etree.ElementTree as ET
		import helpers.utils

		try:
			root = ET.parse(f'{helpers.utils.RES_DIR}/employees.xml')
			nodes = elementpath.select(root, f"/Employees/Employee[@emplid=\'{bar.replace('\'', '&apos;')}\']")
			node_strings = []
			for node in nodes:
				node_strings.append(' '.join([e.text for e in node]))

			RESPONSE += (
				f'Your XPATH query results are: <br>[ {', '.join(node_strings)} ]'
			)
		except:
			RESPONSE += (
				f'Error parsing XPath Query: \'{escape_for_html(query)}\''
			)


		return RESPONSE

