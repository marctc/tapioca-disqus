# tapioca-disqus

Disqus API wrapper implemented with tapioca. 

## Installation
```
pip install tapioca-disqus
```

## Documentation

This wrapper can execute any Disqus Web API method listed in [Disqus API docs](https://disqus.com/api/docs/). 

For example, if we want to call __threads/details/__ method we can do the following:

``` python
from tapioca_disqus import Disqus

disqus = Disqus(api_secret='your-disqus-api-secret')
thread = disqus.threads_details().get(params={'thread': '42'})
print(thread.response.id().data())  # prints '42'
```

All methods should be called with snake_case naming in order to fit Python convention. If we want to execute __forums/listFollowers__
API method we should use `disqus.forums_list_followers()` method.

## More

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/latest/quickstart/)
- Explore this package using ipython
- Have fun!
