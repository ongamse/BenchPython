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

	@app.route('/benchmark/xpathi-01/BenchmarkTest01007', methods=['GET'])
	def BenchmarkTest01007_get():
		return BenchmarkTest01007_post()

	@app.route('/benchmark/xpathi-01/BenchmarkTest01007', methods=['POST'])
	def BenchmarkTest01007_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest01007" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest01007"}\'."
		param = query_string[paramLoc + len("BenchmarkTest01007") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		map71326 = {}
		map71326['keyA-71326'] = 'a-Value'
		map71326['keyB-71326'] = param
		map71326['keyC'] = 'another-Value'
		bar = map71326['keyB-71326']

		import elementpath
		import xml.etree.ElementTree as ET
		import helpers.utils

		try:
			root = ET.parse(f'{helpers.utils.RES_DIR}/employees.xml')
			query = f"/Employees/Employee[@emplid=\'{bar}\']"
			nodes = elementpath.select(root, query)
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

