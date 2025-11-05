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

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00444', methods=['GET'])
	def BenchmarkTest00444_get():
		return BenchmarkTest00444_post()

	@app.route('/benchmark/intoverflow-00/BenchmarkTest00444', methods=['POST'])
	def BenchmarkTest00444_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00444" in request.form.getlist(name):
				param = name
				break

		bar = ""
		if param:
			lst = []
			lst.append('safe')
			lst.append(param)
			lst.append('moresafe')
			lst.pop(0)
			bar = lst[0]

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

