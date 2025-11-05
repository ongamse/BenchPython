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

	@app.route('/benchmark/xss-00/BenchmarkTest00576', methods=['GET'])
	def BenchmarkTest00576_get():
		return BenchmarkTest00576_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00576', methods=['POST'])
	def BenchmarkTest00576_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("Referer")
		
		if headers:
			param = headers[0]

		string24315 = ''
		data12 = ''
		copy = string24315
		string24315 = ''
		string24315 += param
		copy += 'SomeOKString'
		bar = copy


		otherarg = "static text"
		RESPONSE += (
			f'bar is \'{bar}\' and otherarg is \'{otherarg}\''
		)

		return RESPONSE

