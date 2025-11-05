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

	@app.route('/benchmark/xss-00/BenchmarkTest00704', methods=['GET'])
	def BenchmarkTest00704_get():
		return BenchmarkTest00704_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00704', methods=['POST'])
	def BenchmarkTest00704_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00704")
		if not param:
			param = ""

		map24073 = {}
		map24073['keyA-24073'] = 'a-Value'
		map24073['keyB-24073'] = param
		map24073['keyC'] = 'another-Value'
		bar = map24073['keyB-24073']


		RESPONSE += (
			f'Parameter value: {bar}'
		)

		return RESPONSE

