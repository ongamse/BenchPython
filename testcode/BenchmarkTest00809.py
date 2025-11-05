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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00809', methods=['GET'])
	def BenchmarkTest00809_get():
		return BenchmarkTest00809_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00809', methods=['POST'])
	def BenchmarkTest00809_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00809")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf19104 = configparser.ConfigParser()
		conf19104.add_section('section19104')
		conf19104.set('section19104', 'keyA-19104', 'a-Value')
		conf19104.set('section19104', 'keyB-19104', param)
		bar = conf19104.get('section19104', 'keyB-19104')

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

