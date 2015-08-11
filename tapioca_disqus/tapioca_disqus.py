# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)


from resource_mapping import RESOURCE_MAPPING


class DisqusClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://disqus.com/api/3.0/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(DisqusClientAdapter, self).get_request_kwargs(api_params, *args, **kwargs)
        if 'params' in params:
            params['params'].update({'api_secret': api_params.get('api_secret')})
        else:
            params['params'] = {'api_secret': api_params.get('api_secret')}
        return params

    def get_iterator_list(self, response_data):
        return response_data['response']

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs, response_data, response):
        cursor = response_data.get('cursor')
        if not cursor or not cursor.get('hasNext'):
            return
        next_val = cursor.get('next')
        if next_val:
            return {'url': '{}&cursor='.format(response.url, next_val)}

Disqus = generate_wrapper_from_adapter(DisqusClientAdapter)

if __name__ == '__main__':
    d = Disqus(api_secret='GuTZDx1d0Tqs93OK85PmJhEvLX30X6V65DJJAVDCGFXuQeHx9TUJLDJd76fuQDw5')
    #f = d.threads_details().get(params={'forum': 'apsldev', 'thread': 'ident:20'})
    f = d.threads_list().get(params={'forum': 'apsldev'})
    for t in f().pages():
        print(t)
