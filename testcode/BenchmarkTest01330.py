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

	@app.route('/benchmark/codeinj-00/BenchmarkTest01330', methods=['GET'])
	def BenchmarkTest01330_get():
		return BenchmarkTest01330_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest01330', methods=['POST'])
	def BenchmarkTest01330_post():
		RESPONSE = ""

		import helpers.separate_request
		scr = helpers.separate_request.request_wrapper(request)
		param = scr.get_safe_value("BenchmarkTest01330")


		if not param.startswith('\'') or not param.endswith('\'') or '\'' in param[1:-1]:
			RESPONSE += (
				"Eval argument must be a plain string literal."
			)
			return RESPONSE		

		try:
			RESPONSE += (
				eval(param)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(param)}\''
			)

		return RESPONSE


