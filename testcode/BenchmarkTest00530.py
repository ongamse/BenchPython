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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00530', methods=['GET'])
	def BenchmarkTest00530_get():
		return BenchmarkTest00530_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00530', methods=['POST'])
	def BenchmarkTest00530_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00530")
		if not param:
		    param = ""

		map80744 = {}
		map80744['keyA-80744'] = 'a-Value'
		map80744['keyB-80744'] = param
		map80744['keyC'] = 'another-Value'
		bar = map80744['keyB-80744']

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

