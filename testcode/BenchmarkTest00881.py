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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00881', methods=['GET'])
	def BenchmarkTest00881_get():
		return BenchmarkTest00881_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00881', methods=['POST'])
	def BenchmarkTest00881_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00881")
		if not param:
			param = ""

		possible = "ABC"
		guess = possible[0]
		
		match guess:
			case 'A':
				bar = param
			case 'B':
				bar = 'bob'
			case 'C' | 'D':
				bar = param
			case _:
				bar = 'bob\'s your uncle'

		import codecs
		import helpers.utils

		try:
			fileTarget = codecs.open(f'{helpers.utils.TESTFILES_DIR}/{bar}','r','utf-8')

			RESPONSE += (
				f"Access to file: \'{escape_for_html(fileTarget.name)}\' created."
			)

			RESPONSE += (
				" And file already exists."
			)

		except FileNotFoundError:
			RESPONSE += (
				" But file doesn't exist yet."
			)

		return RESPONSE

