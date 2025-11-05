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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00630', methods=['GET'])
	def BenchmarkTest00630_get():
		return BenchmarkTest00630_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00630', methods=['POST'])
	def BenchmarkTest00630_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00630")
		
		if headers:
			param = headers[0]

		map26888 = {}
		map26888['keyA-26888'] = 'a-Value'
		map26888['keyB-26888'] = param
		map26888['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map26888['keyB-26888']
		bar = map26888['keyA-26888']

		import re

		regex = r'(a+)+$'

		if re.match(regex, bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

