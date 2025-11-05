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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00569', methods=['GET'])
	def BenchmarkTest00569_get():
		return BenchmarkTest00569_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00569', methods=['POST'])
	def BenchmarkTest00569_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00569")
		
		if headers:
			param = headers[0]

		map28566 = {}
		map28566['keyA-28566'] = 'a-Value'
		map28566['keyB-28566'] = param
		map28566['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map28566['keyB-28566']
		bar = map28566['keyA-28566']

		import os
		import helpers.utils

		fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
		if os.path.exists(fileName):
			RESPONSE += ( f"File \'{escape_for_html(fileName)}\' exists." )
		else:
			RESPONSE += ( f"File \'{escape_for_html(fileName)}\' does not exist." )

		return RESPONSE

