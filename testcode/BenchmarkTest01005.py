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

	@app.route('/benchmark/sqli-00/BenchmarkTest01005', methods=['GET'])
	def BenchmarkTest01005_get():
		return BenchmarkTest01005_post()

	@app.route('/benchmark/sqli-00/BenchmarkTest01005', methods=['POST'])
	def BenchmarkTest01005_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest01005" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest01005"}\'."
		param = query_string[paramLoc + len("BenchmarkTest01005") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		map96560 = {}
		map96560['keyA-96560'] = 'a-Value'
		map96560['keyB-96560'] = param
		map96560['keyC'] = 'another-Value'
		bar = map96560['keyB-96560']

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

