#!/usr/bin/env python3

from flask import Flask, request, render_template, \
                  redirect

from model_sqlite import *

from datetime import datetime

app = Flask(__name__)

# ipExterne = urllib.urlopen("http://www.whatismyip.org").readline()

@app.route('/')
def index():
    #d = { 'last_added':[ { 'uid':'testuid', 'code':'testcode' } ] }
    d = { 'last_added':get_last_code_db() }
    return render_template('index.html',**d)

@app.route('/create')
def create():
    ip = request.remote_addr
    user_agent = str(request.user_agent)
    date_modif = datetime.now()
    uid = save_db(ip, user_agent, date_modif)
    return redirect("{}edit/{}".format(request.host_url,uid))
    
@app.route('/edit/<string:uid>/')
def edit(uid):
    code = get_code(uid)
    langage = get_langage(uid)
    print(code)
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code, langage=langage,
              url="{}view/{}".format(request.host_url,uid))
    return render_template('edit.html', **d) 

@app.route('/publish',methods=['POST'])
def publish():
    code = request.form['code']
    uid  = request.form['uid']
    langage = request.form['langage']
    #print(code)
    update_code(uid,code,langage)
    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     uid))

@app.route('/view/<string:uid>/')
def view(uid):
    code = get_code(uid)
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code,
              url="{}view/{}".format(request.host_url,uid))
    return render_template('view.html', **d)

@app.route('/admin/<string:uid>/')
def admin(uid):
    #d = { 'last_added':get_all_users() }
    d = { 'last_added':get_ip_from_uid(uid) }
    return render_template('admin.html', **d)

if __name__ == '__main__':
    app.run()

