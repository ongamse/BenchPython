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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00541', methods=['GET'])
	def BenchmarkTest00541_get():
		return BenchmarkTest00541_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00541', methods=['POST'])
	def BenchmarkTest00541_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00541")
		if not param:
		    param = ""

		map20464 = {}
		map20464['keyA-20464'] = 'a-Value'
		map20464['keyB-20464'] = param
		map20464['keyC'] = 'another-Value'
		bar = map20464['keyB-20464']

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

