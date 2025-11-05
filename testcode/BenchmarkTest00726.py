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

	@app.route('/benchmark/xpathi-00/BenchmarkTest00726', methods=['GET'])
	def BenchmarkTest00726_get():
		return BenchmarkTest00726_post()

	@app.route('/benchmark/xpathi-00/BenchmarkTest00726', methods=['POST'])
	def BenchmarkTest00726_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00726")
		if not param:
			param = ""

		map20491 = {}
		map20491['keyA-20491'] = 'a-Value'
		map20491['keyB-20491'] = param
		map20491['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map20491['keyB-20491']
		bar = map20491['keyA-20491']

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

