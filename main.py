import psycopg2
from colorama import Fore

conn = psycopg2.connect(dbname='n42 5-oy@localhost',
                        user='postgres',
                        password='0509',
                        host='localhost',
                        port='5432'
                        )
cur = conn.cursor()

#cur.execute('select * from products')

#products = cur.fetchall()

create_table_query = """
create table if not exists products (
id serial primary key,
name varchar(60),
email varchar(100),
address varchar(110),
age int,
author varchar(30)

);
"""


cur.execute(create_table_query)
conn.commit()

def print_response(message: str):
    print(Fore.YELLOW + message + Fore.RESET)


def isert_product():
    name = str(input('Enter product name: '))
    email = str(input('Enter product seller email : '))
    address = str(input('Enter product seller address: '))
    age = int(input('Enter product seller age: '))
    author = str(input('Enter product author: '))
    insert_into_query = "insert into products (name, email, address, age, author) values (%s, %s, %s, %s, %s);"
    insert_into_parms = (name, email, address, age, author)
    cur.execute(insert_into_query, insert_into_parms)
    conn.commit()
    print_response('Product inserted successfully! 0 1')


def select_all_products():
    select_query = 'select * from products;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print_response(str(row))


def select_one_product():
    _id = int(input('Enter product id: '))
    select_query = 'select * from products where id = %s'
    cur.execute(select_query, (_id,))
    product = cur.fetchall()
    if product:
        print_response('No such product found!')


def update_product():
    select_all_products()
    _id = int(input('Enter product id: '))
    name = str(input('Enter product name: '))
    email = str(input('Enter product seller email: '))
    address = str(input('Enter product seller address: '))
    age = int(input('Enter product seller age: '))
    author = str(input('Enter product author: '))
    update_query = 'update products set name = %s, email = %s, address = %s, age = %s, author = %s where id = %s;'
    update_query_parms = (name, email, address, age, author, _id)
    cur.execute(update_query, update_query_parms)
    conn.commit()
    print_response('Product updated successfully!')



def delete_product():
    select_all_products()
    _id = int(input('Enter product id: '))

    delete_query = 'delete from products where id = %s;'
    cur.execute(delete_query, (_id,))
    conn.commit()
    print_response('Product deleted successfully!')


def menu():
    try:
        print('Insert product => 1')
        print('Select all products => 2')
        print('Delete product => 3')
        print('Select one product => 4')
        print('Update product => 5')
        choice = int(input('Enter your choice: '))

    except ValueError as v:

        choice = -1

    return choice


def run():
    while True:
        choice = menu()
        match choice:
            case '1':
                isert_product()
            case '2':
                select_all_products()
            case '3':
                delete_product()
            case '4':
                select_one_product()
            case '5':
                update_product()
            case _:
                break



# if __name__ == '__main__':
#     run()