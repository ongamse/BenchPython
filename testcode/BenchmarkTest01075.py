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

	@app.route('/benchmark/redirect-00/BenchmarkTest01075', methods=['GET'])
	def BenchmarkTest01075_get():
		return BenchmarkTest01075_post()

	@app.route('/benchmark/redirect-00/BenchmarkTest01075', methods=['POST'])
	def BenchmarkTest01075_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest01075" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest01075"}\'."
		param = query_string[paramLoc + len("BenchmarkTest01075") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		string52153 = ''
		data12 = ''
		copy = string52153
		string52153 = ''
		string52153 += param
		copy += 'SomeOKString'
		bar = copy

		import flask

		return flask.redirect(bar)

		return RESPONSE

