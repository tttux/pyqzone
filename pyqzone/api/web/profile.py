from ..model import AbstractProfileAPIGroup
from .host import WebAPI

import json


CGI_GET_VISITOR_MORE = "https://h5.qzone.qq.com/proxy/domain/g.qzone.qq.com/cgi-bin/friendshow/cgi_get_visitor_more?uin={}&mask=7&g_tk={}&page=1&fupdate=1&clear=1"
CGI_GET_VISITOR_SIMPLE = "https://user.qzone.qq.com/proxy/domain/g.qzone.qq.com/cgi-bin/friendshow/cgi_get_visitor_simple?uin={}&mask=1&g_tk={}"



class WebProfileAPI(WebAPI, AbstractProfileAPIGroup):

    def get_visitor_count(self) -> tuple[int, int]:

        resp = self.client.get(
            url=CGI_GET_VISITOR_SIMPLE.format(
                self.client.uin,
                self.client.gtk
            )
        )

        jsonp = resp.text

        # 删掉开头的_Callback(和结尾的);
        jsonp = jsonp[jsonp.find("(") + 1: jsonp.rfind(")")]

        data = json.loads(jsonp)['data']

        group = data['modvisitcount'][0]

        return group['todaycount'], group['totalcount']