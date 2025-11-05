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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00194', methods=['GET'])
	def BenchmarkTest00194_get():
		return BenchmarkTest00194_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00194', methods=['POST'])
	def BenchmarkTest00194_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00194")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf162 = configparser.ConfigParser()
		conf162.add_section('section162')
		conf162.set('section162', 'keyA-162', 'a_Value')
		conf162.set('section162', 'keyB-162', param)
		bar = conf162.get('section162', 'keyA-162')

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

