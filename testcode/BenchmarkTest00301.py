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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00301', methods=['GET'])
	def BenchmarkTest00301_get():
		return BenchmarkTest00301_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00301', methods=['POST'])
	def BenchmarkTest00301_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00301")
		if not param:
			param = ""

		map13001 = {}
		map13001['keyA-13001'] = 'a-Value'
		map13001['keyB-13001'] = param
		map13001['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map13001['keyB-13001']
		bar = map13001['keyA-13001']

		import helpers.utils

		fileName = None
		fd = None

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			with open(fileName, 'rb') as fd:
				RESPONSE += (
					f'The beginning of file: \'{escape_for_html(fileName)}\' is:\n\n'
					f'{escape_for_html(fd.read(1000).decode('utf-8'))}'
				)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{fileName}\': '
				f'{escape_for_html(e.strerror)}'
			)

		return RESPONSE

