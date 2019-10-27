# Fullstack Assessment - Stock portfolio

## What this project is about
Creating a full stack website where we let users log in and they are able to buy assets (for this project, an asset can be bought or sold like a house) with fluctuating prices throughout the day.

- The goal for this project is to allow users to buy numbers of shares if they have enough cash. 
- Asset prices are incidated via red, green, or grey color. Red indicates "Current price is less than day's opening price". 
  Green indicates "Current price si greater than the days' opening price.
  Gray indicated "Current price is equal to day's open price."
 
## NOTE: The api function call CURRENTLY DOES NOT WORK. ** Only the Login, Register, and database for those two works!

Deployable Link: https://fullstack-stockportfolio.herokuapp.com/

## Resourced Used for this project
 * Python version 3.6.8
 * Flask (Python Framework)
 * Sqlite3 
 * HTML, CSS, Bootstrap
 * API (Alpha Vantage API)- Link: https://www.alphavantage.co/documentation/
 * Modules and how to install them using PiPy: 
    * SQLite3  
        -Linux : python3 -m pip install sqlite3 (sqlite3 should come pre-installed with Python)\
        -Windows: pip install sqlite3
    * Flask\
        -Linux: python3 -m pip install flask\
        -Windows: pip install flask
    * alpha_vantage (API)\
        -Linux: python3 -m pip install alpha_vantage\
        -Windows: pip install alpha_vantage
        
        -Linux: python3 -m pip install pandas\
        -Windows: pip install pandas
        
        -Linux: python3 -m pip install matplotlib\
        -Windows: pip install matplotlib
    * SQLAlchemy\
        -Linux: python3 -m pip install sqlalchemy\
        -Windows: pip install sqlachemy
    * Bcrypt (For password hashing)\
        -Linux: python3 -m pip install flask-bcrypt\
        -Windows: pip install flask-bcrypt 
        
 ## Images of current progress
 ![LogIn](https://raw.githubusercontent.com/KevinLu19/stockPortfolio/master/screenshots/login.png)
 ![Register](https://raw.githubusercontent.com/KevinLu19/stockPortfolio/master/screenshots/register.png)
 ![Profile](https://raw.githubusercontent.com/KevinLu19/stockPortfolio/master/screenshots/profile.png)
 ![Transaction](https://raw.githubusercontent.com/KevinLu19/stockPortfolio/master/screenshots/transactions.png)
