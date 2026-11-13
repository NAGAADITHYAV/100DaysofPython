CREATE_DRINKS_TABLE = '''
CREATE TABLE IF NOT EXISTS Drinks(
id NUM PRIMARY KEY,
name TEXT,
milk NUM,
water NUM,
coffee NUM,
cacoa NUM,
vanilla NUM,
cost REAL
);
'''

INSERT_DRINKS = '''
INSERT INTO Drinks(id, name, milk, water, coffee, cacoa, vanilla, cost)
VALUES
(1, 'Espresso', 0, 140, 30, 0, 0, 250),
(2, 'French Vanilla', 100, 40, 8, 5, 17, 375),
(3, 'Milk', 100, 40, 0, 0, 0, 200),
(4, 'Hot Chocolate', 80, 60, 0, 30, 0, 350),
(5, 'Mocha', 90, 50, 20, 10, 0, 425),
(6, 'Cappuccino', 90, 50, 20, 10, 0, 400),
(7, 'Americano', 0, 140, 15, 0, 0, 300),
(8, 'Latte', 110, 30, 20, 10, 0, 425),
(9, 'Flat White', 20, 120, 40, 0, 0, 375),
(10, 'Macchiato', 10, 130, 30, 0, 0, 325),
(11, 'French Vanilla Latte', 80, 60, 5, 5, 20, 475),
(12, 'Vanilla Choco', 90, 50, 0, 10, 20, 400),
(13, 'Vanilla Choco coffee', 90, 50, 15, 5, 10, 450);
'''


CREATE_COINS_TABLE = '''
CREATE TABLE IF NOT EXISTS Coins(
  id NUM PRIMARY KEY,
  name TEXT,
  value REAL,
  count NUM
);
'''

INSERT_COINS = '''
INSERT INTO Coins(id, name, value, count)
VALUES
(1, 'Penny', 1, 100),
(2, 'Nickel', 5, 20),
(3, 'Dime', 10, 10),
(4, 'Qarter', 25, 0);
'''


CREATE_INGREDIENTS_TABLE = '''
CREATE TABLE IF NOT EXISTS Ingredients(
  id NUM PRIMARY KEY,
  name TEXT,
  quantity NUM
);
'''

INSERT_INGREDIENTS = '''
INSERT INTO Ingredients(id, name, quantity)
VALUES
(1, 'Milk', 2000),
(2, 'Coffee', 600),
(3, 'Cocoa', 400),
(4, 'Vanilla', 300);
'''

CREATE_TRANSACTIONS_TABLE = '''
CREATE TABLE IF NOT EXISTS Transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink_id INTEGER,
    inserted_pennies INTEGER DEFAULT 0,
    inserted_nickels INTEGER DEFAULT 0,
    inserted_dimes INTEGER DEFAULT 0,
    inserted_quarters INTEGER DEFAULT 0,
    change_returned INTEGER, -- Total cents returned
    status TEXT CHECK(status IN ('SUCCESS', 'FAILED')), 
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (drink_id) REFERENCES Drinks(id)
);
'''
