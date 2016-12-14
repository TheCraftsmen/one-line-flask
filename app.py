from flask.views import MethodView as MV


get = lambda self: "devuelve todo"
post = lambda self: "crear"
put = lambda self: "actualizar"

map(lambda x: [x.add_url_rule('/', 'index', lambda: 'hola'), x.add_url_rule('/cust',view_func=type('Cust',(MV,),{row: eval('%s' % row) for row in ['get','post','put']}).as_view('cust')),x.run(debug=True)] , [__import__('flask').Flask(__name__)])