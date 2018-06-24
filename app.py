# -*- coding: utf-8 -*-
import logging
import json
import urllib

from flask import Flask, request
from flask import render_template, render_template_string

from properties import LogisticsType, LogisticsSubType, IsCollection


app = Flask(__name__, static_url_path='')
app.config.from_pyfile("config.py")

##############################
formatter = logging.Formatter(app.config["LOGGER_FORMAT"])

handler = logging.StreamHandler()
handler.setLevel(app.config["LOGGER_LEVEL"])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

app.logger.setLevel(app.config["LOGGER_LEVEL"])

##############################


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map')
def map():
    payload = dict(
        MerchantID=app.config["ECPAY_MERCHANTID"],
        LogisticsType=LogisticsType.CVS,

        ### staging ###
        LogisticsSubType=LogisticsSubType.FAMI,

        ### production ###
        # LogisticsSubType=LogisticsSubType.FAMIC2C,
        # LogisticsSubType=LogisticsSubType.UNIMARTC2C,

        IsCollection=IsCollection.N,
        ServerReplyURL=app.config["ECPAY_SERVER_REPLY"],
        MerchantTradeNo='',
        ExtraData='',
        Device='',
    )

    return render_template(
        "map.html",
        url="{}/Express/map".format(app.config["ECPAY_URL"]),
        payload=payload,
    )


@app.route('/reply', methods=['GET', 'POST'])
def reply():

    if request.method == 'POST':
        req_form = dict(request.form)
        app.logger.info("[POST] reply form: %s", json.dumps(req_form))
        return render_template("reply.html", store_info=urllib.urlencode(req_form))

    app.logger.info("[POST] reply args: %s", json.dumps(request.args))
    return render_template_string("<h2>This is reply Page</h2>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=True)
