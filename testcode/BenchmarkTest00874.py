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

	@app.route('/benchmark/ldapi-00/BenchmarkTest00874', methods=['GET'])
	def BenchmarkTest00874_get():
		return BenchmarkTest00874_post()

	@app.route('/benchmark/ldapi-00/BenchmarkTest00874', methods=['POST'])
	def BenchmarkTest00874_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00874")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf19250 = configparser.ConfigParser()
		conf19250.add_section('section19250')
		conf19250.set('section19250', 'keyA-19250', 'a-Value')
		conf19250.set('section19250', 'keyB-19250', param)
		bar = conf19250.get('section19250', 'keyB-19250')

		import helpers.ldap
		import ldap3

		base = 'ou=users,ou=system'
		filter = f'(&(objectclass=person)(uid={bar}))'
		try:
			conn = helpers.ldap.get_connection()
			conn.search(base, filter, attributes=ldap3.ALL_ATTRIBUTES)
			found = False
			for e in conn.entries:
				RESPONSE += (
					f'LDAP query results:<br>'
					f'Record found with name {e['uid']}<br>'
					f'Address: {e['street']}<br>'
				)
				found = True
			conn.unbind()

			if not found:
				RESPONSE += (
					f'LDAP query results: nothing found for query: {helpers.utils.escape_for_html(filter)}'
				)
		except IOError:
			RESPONSE += (
				"Error processing LDAP query."
			)

		return RESPONSE

