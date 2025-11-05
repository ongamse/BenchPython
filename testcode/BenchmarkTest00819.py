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

	@app.route('/benchmark/sqli-00/BenchmarkTest00819', methods=['GET'])
	def BenchmarkTest00819_get():
		return BenchmarkTest00819_post()

	@app.route('/benchmark/sqli-00/BenchmarkTest00819', methods=['POST'])
	def BenchmarkTest00819_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00819")
		param = ""
		if values:
			param = values[0]

		map42157 = {}
		map42157['keyA-42157'] = 'a-Value'
		map42157['keyB-42157'] = param
		map42157['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map42157['keyB-42157']
		bar = map42157['keyA-42157']

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

