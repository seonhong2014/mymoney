from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    User,
    Item,
    LabelList,
    )


#@view_config(route_name='login', renderer='templates/login.pt')
def login(request):
    pass

#@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'),
                     headers=headers)

@view_config(route_name='itemview')
def item_view(request):
    #userid = request.matchdict['userid']
    userid = request.session['userid']
    item_list = DBSession.query(Item).filter_by(userid=userid).order_by(Item.datetime).all()

    return dict(list=item_list)

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    request.session['userid'] = '1'
    request.session['user_name'] = '박선홍'
    request.session['temp'] = 'seonhong'
    return HTTPFound(location=request.route_url('itemview'))


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_mymoney_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

