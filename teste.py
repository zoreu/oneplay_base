import six
estado = str(six.PY3)
from fasthttp import req
r = req.get('https://oneplayhd.com')
conteudo = r.text

