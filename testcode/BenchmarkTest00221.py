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

	@app.route('/benchmark/xxe-00/BenchmarkTest00221', methods=['GET'])
	def BenchmarkTest00221_get():
		return BenchmarkTest00221_post()

	@app.route('/benchmark/xxe-00/BenchmarkTest00221', methods=['POST'])
	def BenchmarkTest00221_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00221")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf69991 = configparser.ConfigParser()
		conf69991.add_section('section69991')
		conf69991.set('section69991', 'keyA-69991', 'a-Value')
		conf69991.set('section69991', 'keyB-69991', param)
		bar = conf69991.get('section69991', 'keyB-69991')

		import xml.dom.minidom
		import xml.sax.handler

		try:
			parser = xml.sax.make_parser()
			# all features are disabled by default

			doc = xml.dom.minidom.parseString(bar, parser)

			out = ''
			processing = [doc.documentElement]
			while processing:
				e = processing.pop(0)
				if e.nodeType == xml.dom.Node.TEXT_NODE:
					out += e.data
				else:
					processing[:0] = e.childNodes

			RESPONSE += (
				f'Your XML doc results are: <br>{escape_for_html(out)}'
			)
		except:
			RESPONSE += (
				f'There was an error reading your XML doc:<br>{escape_for_html(bar)}'
			)

		return RESPONSE

