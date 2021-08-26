# ShoppingCartAPI


# How to run on your local server
1. Clone this repo.
2. Download & Install python(if not install)
3. Activate virtual env.
5. Go to the clone repo directory & run these commands
   1)  python manage.py migrate
   2)  python manage.py runserver

Also you can Use these apis on our heroku server https://shopping-cart-intern.herokuapp.com

# Api Endpoints

Register User - http://127.0.0.1:8000/

Login User - http://127.0.0.1:8000/rest-auth/login/

Add Item on Cart - http://127.0.0.1:8000/cart/add-item/

Update/Delete/Retrive Cart - http://127.0.0.1:8000/cart/edit-cart/5/  (change cart id according to your cart eg. /5 or /6)

Note :- You can also send data in json format by clicking on Raw data(above the form)
