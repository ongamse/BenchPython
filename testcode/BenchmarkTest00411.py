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

	@app.route('/benchmark/xpathi-00/BenchmarkTest00411', methods=['GET'])
	def BenchmarkTest00411_get():
		return BenchmarkTest00411_post()

	@app.route('/benchmark/xpathi-00/BenchmarkTest00411', methods=['POST'])
	def BenchmarkTest00411_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00411" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf30700 = configparser.ConfigParser()
		conf30700.add_section('section30700')
		conf30700.set('section30700', 'keyA-30700', 'a-Value')
		conf30700.set('section30700', 'keyB-30700', param)
		bar = conf30700.get('section30700', 'keyB-30700')

		import lxml.etree
		import helpers.utils

		try:
			fd = open(f'{helpers.utils.RES_DIR}/employees.xml', 'rb')
			root = lxml.etree.parse(fd)
			query = f'/Employees/Employee[@emplid=$name]'
			nodes = root.xpath(query, name=bar)
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

