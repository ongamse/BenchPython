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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00090', methods=['GET'])
	def BenchmarkTest00090_get():
		return BenchmarkTest00090_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00090', methods=['POST'])
	def BenchmarkTest00090_post():
		RESPONSE = ""

		param = request.form.get("BenchmarkTest00090")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf28405 = configparser.ConfigParser()
		conf28405.add_section('section28405')
		conf28405.set('section28405', 'keyA-28405', 'a-Value')
		conf28405.set('section28405', 'keyB-28405', param)
		bar = conf28405.get('section28405', 'keyB-28405')

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

