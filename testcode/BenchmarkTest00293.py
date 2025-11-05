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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00293', methods=['GET'])
	def BenchmarkTest00293_get():
		return BenchmarkTest00293_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00293', methods=['POST'])
	def BenchmarkTest00293_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00293")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf8735 = configparser.ConfigParser()
		conf8735.add_section('section8735')
		conf8735.set('section8735', 'keyA-8735', 'a-Value')
		conf8735.set('section8735', 'keyB-8735', param)
		bar = conf8735.get('section8735', 'keyB-8735')

		import helpers.utils

		if '../' in bar:
			RESPONSE += (
				'File name must not contain \'../\''
			)
			return RESPONSE

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			fd = open(fileName, 'wb')
			RESPONSE += (
				f'Now ready to write to file: {escape_for_html(fileName)}'
			)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{escape_for_html(fileName)}\': '
				f'{escape_for_html(e.strerror)}'
			)
		finally:
			try:
				if fd is not None:
					fd.close()
			except IOError:
				pass # "// we tried..."

		return RESPONSE

