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

	@app.route('/benchmark/sqli-00/BenchmarkTest00217', methods=['GET'])
	def BenchmarkTest00217_get():
		return BenchmarkTest00217_post()

	@app.route('/benchmark/sqli-00/BenchmarkTest00217', methods=['POST'])
	def BenchmarkTest00217_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00217")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf72771 = configparser.ConfigParser()
		conf72771.add_section('section72771')
		conf72771.set('section72771', 'keyA-72771', 'a_Value')
		conf72771.set('section72771', 'keyB-72771', param)
		bar = conf72771.get('section72771', 'keyA-72771')

		import helpers.db_sqlite

		sql = f'SELECT username from USERS where password = ?'
		con = helpers.db_sqlite.get_connection()
		cur = con.cursor()
		cur.execute(sql, (bar,))
		RESPONSE += (
			helpers.db_sqlite.results(cur, sql)
		)
		con.close()

		return RESPONSE

