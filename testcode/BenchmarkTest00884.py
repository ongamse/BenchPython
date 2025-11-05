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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00884', methods=['GET'])
	def BenchmarkTest00884_get():
		return BenchmarkTest00884_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00884', methods=['POST'])
	def BenchmarkTest00884_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00884")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf56887 = configparser.ConfigParser()
		conf56887.add_section('section56887')
		conf56887.set('section56887', 'keyA-56887', 'a_Value')
		conf56887.set('section56887', 'keyB-56887', param)
		bar = conf56887.get('section56887', 'keyA-56887')

		import helpers.utils

		fileName = None
		fd = None

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			fd = open(fileName, 'rb')
			RESPONSE += (
				f'The beginning of file: \'{escape_for_html(fileName)}\' is:\n\n'
				f'{escape_for_html(fd.read(1000).decode('utf-8'))}'
			)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{fileName}\': '
				f'{escape_for_html(e.strerror)}'
			)
		finally:
			try:
				if fd is not None:
					fd.close()
			except IOError:
				pass # "// we tried..."

		return RESPONSE

