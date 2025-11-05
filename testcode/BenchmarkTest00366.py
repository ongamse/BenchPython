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

	@app.route('/benchmark/ldapi-00/BenchmarkTest00366', methods=['GET'])
	def BenchmarkTest00366_get():
		return BenchmarkTest00366_post()

	@app.route('/benchmark/ldapi-00/BenchmarkTest00366', methods=['POST'])
	def BenchmarkTest00366_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00366")
		if not param:
			param = ""

		map99262 = {}
		map99262['keyA-99262'] = 'a-Value'
		map99262['keyB-99262'] = param
		map99262['keyC'] = 'another-Value'
		bar = map99262['keyB-99262']

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

