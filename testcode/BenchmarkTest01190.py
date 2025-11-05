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

	@app.route('/benchmark/sqli-00/BenchmarkTest01190', methods=['GET'])
	def BenchmarkTest01190_get():
		return BenchmarkTest01190_post()

	@app.route('/benchmark/sqli-00/BenchmarkTest01190', methods=['POST'])
	def BenchmarkTest01190_post():
		RESPONSE = ""

		import helpers.separate_request
		scr = helpers.separate_request.request_wrapper(request)
		param = scr.get_safe_value("BenchmarkTest01190")

		import configparser
		
		bar = 'safe!'
		conf51715 = configparser.ConfigParser()
		conf51715.add_section('section51715')
		conf51715.set('section51715', 'keyA-51715', 'a_Value')
		conf51715.set('section51715', 'keyB-51715', param)
		bar = conf51715.get('section51715', 'keyA-51715')

		import helpers.db_sqlite

		sql = f'SELECT username from USERS where password = \'{bar}\''
		con = helpers.db_sqlite.get_connection()
		cur = con.cursor()
		cur.execute(sql)
		RESPONSE += (
			helpers.db_sqlite.results(cur, sql)
		)
		con.close()

		return RESPONSE

