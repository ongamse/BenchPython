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

	@app.route('/benchmark/pathtraver-02/BenchmarkTest01099', methods=['GET'])
	def BenchmarkTest01099_get():
		return BenchmarkTest01099_post()

	@app.route('/benchmark/pathtraver-02/BenchmarkTest01099', methods=['POST'])
	def BenchmarkTest01099_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf28092 = configparser.ConfigParser()
		conf28092.add_section('section28092')
		conf28092.set('section28092', 'keyA-28092', 'a-Value')
		conf28092.set('section28092', 'keyB-28092', param)
		bar = conf28092.get('section28092', 'keyB-28092')

		import pathlib
		import helpers.utils

		testfiles = pathlib.Path(helpers.utils.TESTFILES_DIR)
		p = (testfiles / bar).resolve()

		if not str(p).startswith(str(testfiles)):
			RESPONSE += (
				"Invalid Path."
			)
			return RESPONSE
		
		if p.exists():
			RESPONSE += ( f"File \'{escape_for_html(str(p))}\' exists." )
		else:
			RESPONSE += ( f"File \'{escape_for_html(str(p))}\' does not exist." )

		return RESPONSE

