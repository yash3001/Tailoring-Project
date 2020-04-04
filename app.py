from flask import render_template, redirect, url_for, request
from myproject import db, app
from myproject.forms import BookingForm, SearchId, SearchName, ModifyCustomer, DeleteCustomer, SearhPhNumber, LoginForm
from myproject.models import Customer, User
from flask_login import login_required, login_user, logout_user

session = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/booking', methods = ['GET','POST'])
@login_required
def booking():
    form = BookingForm()
    if form.validate_on_submit():
        lis = form.name.data.split()
        form.name.data = ''
        for item in lis:
            form.name.data += item.capitalize() + " "
        customer = Customer(form.name.data, form.address.data, form.ph_number.data, form.length_shirt.data,
                     form.chest_shirt.data, form.waist_shirt.data, form.shoulder_shirt.data, form.hips_shirt.data, form.neck_shirt.data,
                     form.sleeves_shirt.data, form.flair_shirt.data, form.slit_shirt.data, form.armhole_shirt.data, form.biceps_shirt.data,
                     form.front_shirt.data, form.back_shirt.data, form.length_trouser.data, form.poncha_trouser.data, form.length_blouse.data,
                     form.chest_blouse.data, form.shoulder_blouse.data, form.neck_blouse.data, form.sleeves_blouse.data, form.armhole_blouse.data,
                      form.biceps_blouse.data, form.plate_blouse.data, form.extra_1.data, form.extra_2.data, form.extra_3.data, form.extra_4.data)
        db.session.add(customer)
        db.session.commit()
        session['ses'] = Customer.query.get(customer.id)
        return redirect(url_for('thanks'))
    return render_template('booking.html', form = form)


@app.route('/thanks')
@login_required
def thanks():
    return render_template('thanks.html', session = session)


@app.route('/search_id', methods = ['GET','POST'])
@login_required
def search_id():
    form = SearchId()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(id = form.id.data).all()
        session['customer'] = customer
        return redirect(url_for('show'))
    return render_template('search_id.html', form = form)


@app.route('/search_name', methods = ['GET','POST'])
@login_required
def search_name():
    form = SearchName()
    if form.validate_on_submit():
        lis = form.name.data.split()
        form.name.data = ''
        for item in lis:
            form.name.data += item.capitalize() + ' '
        customer = Customer.query.filter_by(name = form.name.data).all()
        session['customer'] = customer
        return redirect(url_for('show'))
    return render_template('search_name.html', form = form)


@app.route('/show')
@login_required
def show():
    return render_template('show.html', session = session)

@app.route('/modify', methods=['GET', 'POST'])
@login_required
def modify():
    form = ModifyCustomer()
    if form.validate_on_submit():
        customer = Customer.query.get(form.id.data)
        if form.name.data:
            lis = form.name.data.split()
            form.name.data = ''
            for item in lis:
                form.name.data += item.capitalize() + " "
            customer.name = form.name.data
        if form.address.data:
            customer.address = form.address.data
        if form.ph_number.data:
            customer.ph_number = form.ph_number.data
        if form.length_shirt.data:
            customer.length_shirt = form.length_shirt.data
        if form.chest_shirt.data:
            customer.chest_shirt = form.chest_shirt.data
        if form.waist_shirt.data:
            customer.waist_shirt = form.waist_shirt.data
        if form.shoulder_shirt.data:
            customer.shoulder_shirt = form.shoulder_shirt.data
        if form.hips_shirt.data:
            customer.hips_shirt = form.hips_shirt.data
        if form.neck_shirt.data:
            customer.neck_shirt = form.neck_shirt.data
        if form.sleeves_shirt.data:
            customer.sleeves_shirt = form.sleeves_shirt.data
        if form.flair_shirt.data:
            customer.flair_shirt = form.flair_shirt.data
        if form.slit_shirt.data:
            customer.slit_shirt = form.slit_shirt.data
        if form.biceps_shirt.data:
            customer.biceps_shirt = form.biceps_shirt.data
        if form.armhole_shirt.data:
            customer.armhole_shirt = form.armhole_shirt.data
        if form.front_shirt.data:
            customer.front_shirt = form.front_shirt.data
        if form.back_shirt.data:
            customer.back_shirt = form.back_shirt.data
        if form.length_trouser.data:
            customer.length_trouser = form.length_trouser.data
        if form.poncha_trouser.data:
            customer.poncha_trouser = form.poncha_trouser.data
        if form.length_blouse.data:
            customer.length_blouse = form.length_blouse.data
        if form.chest_blouse.data:
            customer.chest_blouse = form.chest_blouse.data
        if form.shoulder_blouse.data:
            customer.shoulder_blouse = form.shoulder_blouse.data
        if form.neck_blouse.data:
            customer.neck_blouse = form.neck_blouse.data
        if form.sleeves_blouse.data:
            customer.sleeves_blouse = form.sleeves_blouse.data
        if form.armhole_blouse.data:
            customer.armhole_blouse = form.armhole_blouse.data
        if form.biceps_blouse.data:
            customer.biceps_blouse = form.biceps_blouse.data
        if form.plate_blouse.data:
            customer.plate_blouse = form.plate_blouse.data
        if form.extra_1.data:
            customer.extra_1 = form.extra_1.data
        if form.extra_2.data:
            customer.extra_2 = form.extra_2.data
        if form.extra_3.data:
            customer.extra_3 = form.extra_3.data
        if form.extra_4.data:
            customer.extra_4 = form.extra_4.data

        db.session.commit()
        customer = Customer.query.get(form.id.data)
        session['ses'] = customer
        return redirect(url_for('thanks'))

    return render_template('modify.html', form = form)


@app.route('/delete', methods = ['GET', 'POST'])
@login_required
def delete():
    form = DeleteCustomer()
    if form.validate_on_submit():
        customer = Customer.query.get(form.id.data)
        session['ses'] = customer
        db.session.delete(customer)
        db.session.commit()
        return redirect(url_for('deleted'))
    return render_template('delete.html', form = form)

@app.route('/search_ph_number', methods=['GET', 'POST'])
@login_required
def search_ph_number():
    form = SearhPhNumber()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(ph_number = form.ph_number.data).all()
        session['customer'] = customer
        return redirect(url_for('show'))
    return render_template('search_ph_number.html', form=form)

@app.route('/deleted')
@login_required
def deleted():
    return render_template('deleted.html', session = session)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('home')

            return redirect(next)
    return render_template('login.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
