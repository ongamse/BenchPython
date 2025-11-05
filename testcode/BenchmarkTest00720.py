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

	@app.route('/benchmark/xss-00/BenchmarkTest00720', methods=['GET'])
	def BenchmarkTest00720_get():
		return BenchmarkTest00720_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00720', methods=['POST'])
	def BenchmarkTest00720_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00720")
		if not param:
			param = ""

		map34113 = {}
		map34113['keyA-34113'] = 'a-Value'
		map34113['keyB-34113'] = param
		map34113['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map34113['keyB-34113']
		bar = map34113['keyA-34113']


		dict = {}
		dict['bar'] = bar
		dict['otherarg'] = 'this is it'
		RESPONSE += (
			'bar is \'{0[bar]}\' and otherarg is \'{0[otherarg]}\''.format(dict)
		)

		return RESPONSE

