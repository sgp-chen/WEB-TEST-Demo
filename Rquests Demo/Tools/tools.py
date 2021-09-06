import requests
import logging

class Requests_tools():
    def get_(self, url, **kwargs):

        try:
            r = requests.get(url=url, headers=kwargs, json=kwargs)
        except:
            r = requests.get(url=url, headers=kwargs, data=kwargs)
        return r.json(), r.status_code

    def post_(self, url, **kwargs):
        try:
            r = requests.post(url=url, headers=kwargs, json=kwargs)
        except:
            r = requests.post(url=url, headers=kwargs, data=kwargs)
        return r.json(), r.status_code

    def assert_get(self, code,log, url, **kwargs):
        try:
            r = self.get_(url, **kwargs)[1]
            log.info("status_code r={}".format(r))
            log.info("status_code code={}".format(code))
            assert r == code, "测试不通过"
        except Exception as e:
            log.error("测试异常，异常码为{}".format(e))

    def assert_post(self, code, log,url, **kwargs):
        try:
            r = self.post_(url, **kwargs)[1]
            log.info("status_code r={}".format(r))
            log.info("status_code code={}".format(code))
            assert r == code, "测试不通过"
        except Exception as e:
            log.error("测试异常，异常码为{}".format(e))