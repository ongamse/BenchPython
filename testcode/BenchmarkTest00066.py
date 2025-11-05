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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00066', methods=['GET'])
	def BenchmarkTest00066_get():
		response = make_response(render_template('web/intoverflow-00/BenchmarkTest00066.html'))
		response.set_cookie('BenchmarkTest00066', 'x',
			max_age=60*3,
			secure=True,
			path=request.path,
			domain='localhost')
		return response
		return BenchmarkTest00066_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00066', methods=['POST'])
	def BenchmarkTest00066_post():
		RESPONSE = ""

		import urllib.parse
		param = urllib.parse.unquote_plus(request.cookies.get("BenchmarkTest00066", "noCookieValueSupplied"))

		bar = "This should never happen"
		if 'should' in bar:
			bar = param

		import re

		regex = re.compile(r'^(([a-z])+.)+')

		if regex.match(bar) is not None:
			RESPONSE += (
				'String matches!'
			)
		else:
			RESPONSE += (
				'String does not match.'
			)

		return RESPONSE

