#from pprint import pprint
from flask import Flask, request, render_template, redirect, url_for, json,jsonify
import sys,getopt
import json

from datetime import datetime
from BaseData.ConnectBDG import *
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
import os


BASE_DIR=os.path.abspath(os.path.dirname(__file__))
datos = []


app=Flask(__name__)

global base_grant_url
base_grant_url=""
global user_continue_url
user_continue_url=""
global success_url
success_url=""
global host
global IP_CLIENT,MAC_CLIENT, MAC
IP_CLIENT=""
MAC_CLIENT=""
MAC=""


""""
def mac_for_ip(ip):
    for iface in nif.interfaces():
        addresses = nif.ifaddresses(iface)
        try:
            if_mac = addresses[AF_LINK][0]['addr']
            if_ip = addresses[AF_INET][0]['addr']
            #print(if_ip)
        except KeyError:
            if_mac=if_ip=None
        if if_ip==ip:
            return if_mac
        #print(addresses)
    return  None
"""
@app.route("/inicio", methods=["GET"])
def click():
    global base_grant_url
    #base_grant_url = "https://n34.network-auth.com/splash/grant"
    #print(base_grant_url)
    global user_continue_url
    user_continue_url = "https://www.google.com"
    global success_url
    global host,IP_CLIENT,MAC_CLIENT,MAC

    host=request.host_url
    print(host)
    base_grant_url=request.args.get(base_grant_url)
    user_continue_url=request.args.get(user_continue_url)
    MAC = request.args.get('node_mac')

    #IP_CLIENT="10.57.30.200"
    #IP_CLIENT=socket.gethostbyname(socket.gethostname())
    #print(IP_CLIENT)
    IP_CLIENT=request.args.get('client_ip')

    #mac = mac_for_ip(IP_CLIENT)
    #print(mac)
    MAC_CLIENT=request.args.get('client_mac')
    #MAC_CLIENT = mac
    splashClick = datetime.now()
    splashClick=request.args.get('splashclick_time')
    #Success=Success()
    #success_url=host
    #success_url=host+"https://www.facebook.com/CafamFloresta.CC"
    success_url=host+"Success"
    
    return render_template("Inicio.html", success_url=success_url)

@app.route("/login", methods=["POST"])
def logging():
    global host,IP_CLIENT,MAC_CLIENT,MAC
    global base_grant_url
    base_grant_url = "https://n356.network-auth.com/splash/grant"
    global user_continue_url
    user_continue_url = "https://www.google.com"
    global success_url

    user=request.form["Usuario"]
    user_email=request.form["Email"]
    celular = request.form["Celular"]
    genero = request.form["Genero"]
    motivo = request.form["selector_motivo"]

    #print(user,user_email,celular,genero,motivo,IP_CLIENT,MAC_CLIENT)
    datos.append(user)
    datos.append(user_email)
    datos.append(celular)
    datos.append(genero)
    datos.append(motivo)
    datos.append(IP_CLIENT)
    datos.append(MAC_CLIENT)
    print(datos)

    #print(base_grant_url)
    #print(base_grant_url +"?continue_url=" + success_url)
    #host=request.host_url
    #host_n=host+"login"

    print(base_grant_url +"?continue_url=" + success_url)
    print(success_url)
	
    DataCaptive(datos)

    #frame_dict = {"id": frame.id, "name": frame.name, "email": frame.email}
    #return redirect(base_grant_url + "?continue_url=" + success_url + "&duration=3600", code=302)
    return redirect(base_grant_url +"?continue_url=" + success_url, code=302)
    #return redirect(host_n +"?base_grant_url="+ base_grant_url + "?continue_url=" + success_url, code=302)

@app.route("/Success", methods=["GET"])
def Success():
    global user_continue_url
    print(user_continue_url)
    #return redirect(base_grant_url + "?continue_url=" + success_url + "&duration=3600", code=302)
    return redirect("https://www.google.com")
    #return render_template("Success.html",user_continue_url=user_continue_url)


#if __name__ == "__main__":
    #db.create_all()
    #app.run(debug=False)


