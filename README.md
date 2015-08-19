# Tapioca disqus

## Instalation
```
pip install tapioca-disqus
```

## Documentation
``` python
from tapioca_disqus import Disqus

disqus = Disqus(api_secret='your-disqus-api-secret')

thread = disqus.threads_details().get(params={'thread': '42'})

thread().data()
```

## More

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/latest/quickstart/)
- Explore this package using ipython
- Have fun!
