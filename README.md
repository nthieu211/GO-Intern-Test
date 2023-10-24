# GO-Intern-Test

Mini-project apply for Python developer intern

# Description

**Link website demo** [http://gotest.nth.id.vn](http://gotest.nth.id.vn)

# Tech stack

- BE & FE: Django
- Database: MySQL
- Deploy:
  - Droplet Ubuntu 20.04 on Digital Ocean
  - NGINX + gunicorn

# Run project locally

1. Download MySQL and MySQL Workbench from https://dev.mysql.com/downloads/workbench/

   - Enter password for `root`: 123456789
   - Create database `gsneaker` by run this query:

   ```bash
   CREATE DATABASE IF NOT EXISTS gsneaker
   ```

2. Clone my project

   ```bash
   git clone https://github.com/nthieu211/GO-Intern-Test.git
   cd GO-Intern-Test

   ```

3. Install requirements by run

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Migrate data

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. Load data from json

   ```bash
   python3 manage.py loaddata ./data/product.json
   ```

6. Run localhost server

   ```bash
   python3 manage.py runserver 0.0.0.0:8000
   ```

7. Open browser and open address `0.0.0.0:8000/localhost:8000`

# Deploy on Ubuntu 20.04 - DigitalOcean

1. Login and create a Droplet-Ubuntu20.04 on DigitalOcean

2. Open `Console` on tab droplet or add SSH Key to remote.

3. Using each line to install package:

```bash
sudo apt update
sudo apt install nginx
sudo ufw enable
sudo ufw allow 'Nginx HTTP'
sudo ufw allow 22
sudo apt install mysql-server
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456789';
CREATE DATABASE IF NOT EXISTS gsneaker;
exit
git clone https://github.com/nthieu211/GO-Intern-Test.git
cd GO-Intern-Test
python3 -m pip install -r requirements.txt
python3 -m pip install gunicorn
```

4. Config Gunicorn and Nginx

# Checklist

### Must have:

- [x] Display all products in Our Products section (for products data please check from Technical Requirements):
  - [x] Single product should have name, description, price, image and Add To Cart button.
  - [x] User able to click on Add To Cart to add target product to their cart.
  - [x] Added product doesn't have Add To Cart button anymore, it should have Check Mark Icon (✓) instead.
- [x] Display all added products in Your Cart section:

  - [x] Each product in cart should have name, price, image, increase/decrease amount button and remove button.
  - [x] User able to increase/decrease amount of a product in cart. When product's amount is decreased to zero, that product will be removed from cart naturally.
  - [x] User able to remove product from cart.
  - [x] Show total price of all products in car. When user increase/decrease product's amount or remove product, total price should be re-calculate correctly.
  - [x] When there are no products in cart, we should show Your cart is empty message.
  - [x] Products in cart should be persistent: When user visit the application, products are added before should be showed, user don't need to add products again.

- [x] UI must follow correctly design from [live demo](https://gshoes.vercel.app/).

### Nice to have:

- [x] Responsive design (look good on all devices: desktops, tablets & mobile phones).
- [ ] Smooth animations (don't really need to be same as the demo, just do what you think is good).
- [x] Deploy the application to ~~heroku~~ [DigitalOcean](digitalocean.com).
