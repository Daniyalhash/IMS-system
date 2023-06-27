from django.shortcuts import render,redirect
from django.db import connections
import uuid
from django.views.decorators.csrf import csrf_exempt


from django.contrib import messages
import sqlite3,os,datetime,random,string
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse('ths is')
# dashboard
def dashboard(request):
     return render(request,'dashboard.html')
# product
def get_length(request):
    with sqlite3.connect(BASE_DIR/'data.db') as db:
        cursor=db.cursor()
        query = "SELECT * FROM o_product"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        product_count = len(rows)

    # Render the dashboard template with the product count
    return render(request, 'dashboard.html', {'product_count': product_count})
def product(request):
    with sqlite3.connect(BASE_DIR/'data.db') as db:
        cursor=db.cursor()
        query = "SELECT * FROM o_product"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        products = []
        for row in rows:
            product = dict(zip(column_names, row))
            products.append(product)
        print(products)
        
        return render(request,'product.html',{'product':products})
def delete_product(request,pro_id):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = "DELETE FROM o_product WHERE pro_id= ?"
        cursor.execute(query, (pro_id,))
        messages.success(request, 'Product deleted successfully.')
       
      
        return redirect('/product')
    
def save_product(request):
    if request.method == 'POST':
        pro_id =  random.randint(1, 100)
        ar_name = request.POST.get('ar_name')
        brand = request.POST.get('brand')
        color = request.POST.get('color')
        size = int(request.POST.get('size'))
        cate = request.POST.get('cate')
       
        unique_id = uuid.uuid4()
        with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()
            # query = 'INSERT INTO "axha"("ID","aname","brand","color","size","cate","price") VALUES (?,?,?,?,?,?,?)'
            query = 'INSERT INTO "o_product"("pro_id","ar_name","brand","color","size","cate") VALUES (?,?,?,?,?,?)'
            values = (pro_id,ar_name, brand, color, size, cate)
           
            cursor.execute(query, values)
       

    return redirect('/product')
def getproduct(request):
    
    with sqlite3.connect(BASE_DIR/'data.db') as db:
        cursor = db.cursor()
        query = "SELECT * FROM o_product"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        products = []
        for row in rows:
            product = dict(zip(column_names, row))
            products.append(product)
        
        # Count the total number of products
        total_products = len(products)
        
        return render(request, 'product.html', {'product': products, 'total_product': total_products})
def editproduct(request):
    if request.method == 'POST':
        pro_id = request.POST.get('pro_id')
        ar_name = request.POST.get('ar_name')
        brand = request.POST.get('brand')
        color = request.POST.get('color')
        size = request.POST.get('size')
        cate = request.POST.get('cate')
        
        with sqlite3.connect(BASE_DIR / 'data.db') as db:
            cursor = db.cursor()
            
            query = """
                UPDATE o_product
                SET ar_name = ?,
                    brand = ?,
                    color = ?,
                    size = ?,
                    cate = ?
                WHERE pro_id = ?
            """
            cursor.execute(query, (ar_name, brand, color, size, cate, pro_id))


    return redirect('/product')


def update_product(request, pro_id):
    # Process the form submission and update the product information in the database
        
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = """
            SELECT * FROM o_product
            WHERE pro_id = ?
        """
        cursor.execute(query, (pro_id,))
        rows = cursor.fetchone()
        
        # rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        # Prepare the data as a dictionary
        product = dict(zip(column_names, rows))
        
    return render(request, 'update_prod.html', {"product": product})

def product_count(request):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor =db.cursor()
        cursor.execute("SELECT COUNT(*) FROM o_product")
        product_count = cursor.fetchone()[0]
        
        count = len(product_count)
        
        query = 'INSERT INTO "c_product"("co_id","count") VALUES (?,?)'
        values = (co_id,count)
        
        cursor.execute(query, values)  
# suppliers function
def supplier(request):
     with sqlite3.connect(BASE_DIR/'data.db') as db:
        cursor=db.cursor()
        query = "SELECT * FROM o_supplier"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        suppliers = []
        for row in rows:
            supplier = dict(zip(column_names, row))
            suppliers.append(supplier)
        print(suppliers)
        return render(request,'supplier.html',{'supplier':suppliers})
        

def delete_supplier(request,sup_id):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = "DELETE FROM o_supplier WHERE sup_id= ?"
        cursor.execute(query, (sup_id,))
        messages.success(request, 'Supplier deleted successfully.')
       
      
        return redirect('/supplier')

def save_supplier(request):
    if request.method == 'POST':
        sup_id = random.randint(1, 100)
        sup_name = request.POST.get('sup_name')
        
        sup_ph=request.POST.get('sup_ph')
        unique_id = uuid.uuid4()
        with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()
            # query = 'INSERT INTO "axha"("ID","aname","brand","color","size","cate","price") VALUES (?,?,?,?,?,?,?)'
            query = 'INSERT INTO "o_supplier"("sup_id","sup_name","sup_ph") VALUES (?,?,?)'
            values = (sup_id, sup_name,sup_ph)
            cursor.execute(query, values)
       

    return redirect('/supplier')
def editsupplier(request):
    if request.method == 'POST':
        sup_id= request.POST.get("sup_id")
        sup_name = request.POST.get('sup_name')
        
        sup_ph=request.POST.get('sup_ph')
        
        with sqlite3.connect(BASE_DIR / 'data.db') as db:
            cursor = db.cursor()
            
            query = """
                UPDATE o_supplier
                SET sup_name = ?,
                    sup_ph = ?
                 
                WHERE sup_id = ?
            """
            cursor.execute(query, (sup_name, sup_ph,  sup_id))


    return redirect('/supplier')


def update_supplier(request, sup_id):
    # Process the form submission and update the product information in the database
        
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = """
            SELECT * FROM o_supplier
            WHERE sup_id = ?
        """
        cursor.execute(query, (sup_id,))
        rows = cursor.fetchone()
        
        # rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        # Prepare the data as a dictionary
        supplier = dict(zip(column_names, rows))
        
    return render(request, 'upd_supplier.html', {"supplier": supplier})
# purchase
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('pro_id')
        # Perform the desired logic with the product ID
        # For example, add the product to the user's cart
        request.session['pro_id'] = product_id
        # Redirect to the appropriate page
        return redirect('/purchase')
    else:
        # Handle the case when the request method is not POST
        # You can redirect to an error page or display an error message
        return redirect('Invalid request method')

def purchase(request):
    with sqlite3.connect(BASE_DIR/'data.db') as db:
   
        cursor=db.cursor()
        query = "SELECT * FROM o_purchase"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        # total amount

        # Prepare the data as a list of dictionaries
        purchases = []
        for row in rows:
            purchase = dict(zip(column_names, row))
            
            purchases.append(purchase)
        print(purchases)
    #    product
        query2 = "SELECT * FROM o_product"  
        cursor.execute(query2)
        rows2 = cursor.fetchall()
        column_names2 = [description[0] for description in cursor.description]
        # total amount
        # Prepare the data as a list of dictionaries
        products = []
        for row2 in rows2:
            product = dict(zip(column_names2, row2))
            products.append(product)

        print(products)     
     
        return render(request, 'purchase.html', {'product': products,'purchase': purchases})


def delete_purchase(request,pur_id):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = "DELETE FROM o_purchase WHERE pur_id= ?"
        cursor.execute(query, (pur_id,))
        messages.success(request, 'Purchase deleted successfully.')
       
      
        return redirect('/purchase')


def save_purchase(request):
     
    if request.method == 'POST':    
        pur_id = random.randint(1, 100)
        product_id = request.session.get('pro_id')
        sup_id = request.POST.get('sup_id')
        pur_quan = int(request.POST.get('pur_quan'))
        pur_price = float(request.POST.get('pur_price'))
        pur_total = pur_price* pur_quan
        #we  inventory
        in_id = random.randint(1, 100)
        sal_quan = None
        # inserting in purchase
        with sqlite3.connect(BASE_DIR / 'data.db') as db:
            cursor = db.cursor()

            # Check if the supplier ID exists
            query_check_supplier = 'SELECT * FROM o_supplier WHERE sup_id = ?;'
            cursor.execute(query_check_supplier, (sup_id,))
            result_supplier = cursor.fetchone()

            if result_supplier:
                # Supplier ID exists, proceed with saving the purchase
                query_insert_purchase = 'INSERT INTO o_purchase (pur_id, pro_id, sup_id, pur_quan, pur_price, pur_total) VALUES (?, ?, ?, ?, ?, ?);'
                values_insert_purchase = (pur_id, product_id, sup_id, pur_quan, pur_price, pur_total)
                cursor.execute(query_insert_purchase, values_insert_purchase)

                # Check if the product already exists in the inventory
                query_check_inventory = 'SELECT * FROM o_inventory WHERE pro_id = ?;'
                cursor.execute(query_check_inventory, (product_id,))
                result_inventory = cursor.fetchone()

                if result_inventory:
                    # If the product already exists, update the quantity
                    current_quantity = result_inventory[2]
                    new_quantity = int(current_quantity) + int(pur_quan)
                    query_update_inventory = 'UPDATE o_inventory SET pur_quan = ? WHERE pro_id = ?;'
                    cursor.execute(query_update_inventory, (new_quantity, product_id))
                else:
                    # If the product doesn't exist, insert a new record
                    query_insert_inventory = 'INSERT INTO o_inventory (in_id, pro_id, pur_quan, sal_quan) VALUES (?, ?, ?, ?);'
                    values_insert_inventory = (in_id, product_id, pur_quan, sal_quan)
                    cursor.execute(query_insert_inventory, values_insert_inventory)

                db.commit()
                return redirect('/purchase')
            else:
                # Supplier ID does not exist, generate an error
                error_message = 'Supplier ID does not match any existing suppliers.'
                return render(request, 'error.html', {'error_message': error_message})

    return redirect('/purchase')
    #     with sqlite3.connect(BASE_DIR/'data.db') as db:
          
    #         cursor=db.cursor()
    #         query = 'INSERT INTO "o_purchase"("pur_id","pro_id","sup_id","pur_quan","pur_price","pur_total") VALUES (?,?,?,?,?,?);'
    #         values = (pur_id,product_id,sup_id,pur_quan,pur_price,pur_total)
    #         cursor.execute(query, values)       
    #         db.commit() 
    #           # Insert into the purchase table using the foreign key
              
    #     with sqlite3.connect(BASE_DIR/'data.db') as db:
    #         cursor = db.cursor()

    #         # Check if the product already exists in the inventory
    #         query_check = 'SELECT * FROM o_inventory WHERE pro_id = ?;'
    #         cursor.execute(query_check, (product_id,))
    #         result = cursor.fetchone()

    #         if result:
    #             # If the product already exists, update the quantity
    #             current_quantity = result[2]
    #             new_quantity =int(current_quantity) + int(pur_quan)

    #             query_update = 'UPDATE o_inventory SET pur_quan = ? WHERE pro_id = ?;'
    #             cursor.execute(query_update, (new_quantity, product_id))
    #         else:
    #             # If the product doesn't exist, insert a new record
    #             in_id = random.randint(1, 100)
    #             query_insert = 'INSERT INTO o_inventory (in_id, pro_id, pur_quan, sal_quan) VALUES (?, ?, ?, ?);'
    #             values_insert = (in_id, product_id, pur_quan, sal_quan)
    #             cursor.execute(query_insert, values_insert)
            
    #  return redirect('/purchase')




        
        # Retrieve the patient and doctor objects using their IDs
        # with sqlite3.connect(BASE_DIR/'data.db') as db:
        #     cursor=db.cursor() 
        #     cursor.execute("SELECT * FROM Patient WHERE id_p=?", (patient_id,))
        #     patient_result = cursor.fetchone()
        #     cursor.execute("SELECT * FROM Doctor WHERE id_d=?", (doctor_id,))
        #     doctor_result = cursor.fetchone()
        #     appointment_id = "".join(random.choices(string.ascii_letters + string.digits, k=4))

        #     # Create a new Appointment object and save it to the database
        #     cursor.execute("INSERT INTO Appointment (id_a, patient, doctor,date) VALUES (?, ?, ?,?)", (appointment_id, patient_result[0], doctor_result[0],datetime.date.today()))
def editpurchase(request):
    if request.method == 'POST':
        in_id = request.POST.get('in_id')
        pur_id = request.POST.get('pur_id')
        product_id = request.session.get('pro_id')
        sup_id = request.POST.get('sup_id')
        pur_quan = int(request.POST.get('pur_quan'))
        pur_price = float(request.POST.get('pur_price'))
        pur_total = pur_price * pur_quan
        sal_quan = None
        
        with sqlite3.connect(BASE_DIR / 'data.db') as db:
            cursor = db.cursor()

            # Get the original purchase quantity
            query_original_purchase = """
                SELECT pur_quan
                FROM o_purchase
                WHERE pur_id = ?
            """
            cursor.execute(query_original_purchase, (pur_id,))
            original_purchase_quan = cursor.fetchone()[0]

            # Calculate the quantity difference
            purchase_quantity_diff = int(pur_quan) - int(original_purchase_quan)

            # Update the purchase
            query_purchase = """
                UPDATE o_purchase
                SET pro_id = ?,
                    sup_id = ?,
                    pur_quan = ?,
                    pur_price = ?,
                    pur_total = ?
                WHERE pur_id = ?
            """
            cursor.execute(query_purchase, (product_id, sup_id, pur_quan, pur_price, pur_total, pur_id))

            if int(pur_quan) > int(original_purchase_quan):
                # Update the inventory
                query_update_inventory = """
                    UPDATE o_inventory
                    SET pur_quan = pur_quan + ?
                    WHERE pro_id = ?
                """
                cursor.execute(query_update_inventory, (purchase_quantity_diff, product_id))

    return redirect('/purchase')



def update_purchase(request, pur_id):
    # Process the form submission and update the product information in the database
        
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = """
            SELECT * FROM o_purchase
            WHERE pur_id = ?
        """
        cursor.execute(query, (pur_id,))
        rows = cursor.fetchone()
        
        # rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        # Prepare the data as a dictionary
        purchase = dict(zip(column_names, rows))
        
    return render(request, 'upd_purchase.html', {"purchase": purchase})

# customer

def customer(request):
    with sqlite3.connect(BASE_DIR/'data.db') as db:
        cursor=db.cursor()
        query = "SELECT * FROM o_customer"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        # total amount

        # Prepare the data as a list of dictionaries
        customers = []
        for row in rows:
            customer = dict(zip(column_names, row))
            customers.append(customer)
        print(customers)
        
        return render(request, 'customer.html', {'customer': customers})
def delete_customer(request,cus_id):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = "DELETE FROM o_customer WHERE cus_id= ?"
        cursor.execute(query, (cus_id,))
        messages.success(request, 'Customer deleted successfully.')
       
      
        return redirect('/customer')
def save_customer(request):
     if request.method == 'POST':
        cus_id =random.randint(1, 100)
        c_name = request.POST.get('c_name')
        c_ph = int(request.POST.get('c_ph'))
       
        with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()

            # query = 'INSERT INTO "axha"("ID","aname","brand","color","size","cate","price") VALUES (?,?,?,?,?,?,?)'
            query = 'INSERT INTO "o_customer"("cus_id","c_name","c_ph") VALUES (?,?,?);'
            values = (cus_id,c_name,c_ph)
            cursor.execute(query, values)

    
     return redirect('/customer')
# sale
def add_to_cart_sale(request):
    if request.method == 'POST':
        product_id = request.POST.get('pro_id')
        # Perform the desired logic with the product ID
        # For example, add the product to the user's cart
        request.session['pro_id'] = product_id
        # Redirect to the appropriate page
        return redirect('/sale')
    else:
        # Handle the case when the request method is not POST
        # You can redirect to an error page or display an error message
        return redirect('Invalid request method')
def sale(request):
    
    with sqlite3.connect(BASE_DIR/'data.db') as db:
        cursor=db.cursor()
        query = "SELECT * FROM o_sale"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        # total amount

        # Prepare the data as a list of dictionaries
        sales = []
        for row in rows:
            sale = dict(zip(column_names, row))
            sales.append(sale)
        print(sales)
        # products
        query2 = "SELECT * FROM o_product"  
        cursor.execute(query2)
        rows2 = cursor.fetchall()
        column_names2 = [description[0] for description in cursor.description]
        # total amount
        # Prepare the data as a list of dictionaries
        products = []
        for row2 in rows2:
            product = dict(zip(column_names2, row2))
            products.append(product)

        print(products)     
        return render(request, 'sale.html', {'sale': sales,'product':products})
    

def delete_sale(request,sal_id):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = "DELETE FROM o_sale WHERE sal_id= ?"
        cursor.execute(query, (sal_id,))
        messages.success(request, 'sales deleted successfully.')
       
      
        return redirect('/sale')
def save_sale(request):
    if request.method == 'POST':
        sal_id = random.randint(1, 100)
        product_id = request.session.get('pro_id')
        sal_price = float(request.POST.get('sal_price'))
        sal_quan = int(request.POST.get('sal_quan'))
        t_amtt = sal_price * sal_quan

        with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor = db.cursor()

            # Check if the product exists in the inventory and has sufficient quantity
            query_check = 'SELECT * FROM o_inventory WHERE pro_id = ?;'
            cursor.execute(query_check, (product_id,))
            result = cursor.fetchone()

            if result:
                current_quantity = result[2]

                if int(current_quantity) >= sal_quan:
                    # Sufficient quantity available, proceed with the sale

                    # Insert sale record
                    query_insert_sale = 'INSERT INTO "o_sale"("sal_id","pro_id","sal_price","sal_quan","sal_total") VALUES (?,?,?,?,?);'
                    values_sale = (sal_id, product_id, sal_price, sal_quan, t_amtt)
                    cursor.execute(query_insert_sale, values_sale)

                    # Update inventory and sales quantity
                    new_quantity = int(current_quantity) - int(sal_quan)
                    query_update_inventory = 'UPDATE o_inventory SET pur_quan = ?, sal_quan = ? WHERE pro_id = ?;'
                    values_update_inventory = (new_quantity, sal_quan, product_id)
                    cursor.execute(query_update_inventory, values_update_inventory)
                else:
                    # Insufficient quantity, display error message or redirect
                    error_message = "Insufficient quantity available for sale."
                    return render(request, 'error.html', {'error_message': error_message})
                    # You can choose to render an error page or redirect with the error message
                    # Example: return render(request, 'error.html', {'message': error_message})
                    # Example: return redirect('/error/?message=' + error_message)

    return redirect('/sale')

# INVENTORY
def editsale(request):
    if request.method == 'POST':
        sal_id = request.POST.get('sal_id')
        product_id = request.session.get('pro_id')
        sal_quan = int(request.POST.get('sal_quan'))
        sal_price = float(request.POST.get('sal_price'))
        sal_total = sal_price * sal_quan
        
        with sqlite3.connect(BASE_DIR / 'data.db') as db:
            cursor = db.cursor()

            # Get the original sale details
            query_original_sale = """
                SELECT sal_quan
                FROM o_sale
                WHERE sal_id = ?
            """
            cursor.execute(query_original_sale, (sal_id,))
            original_sale_quan = cursor.fetchone()[0]

            # Update the sale
            query_update_sale = """
                UPDATE o_sale
                SET pro_id = ?,
                    sal_quan = ?,
                    sal_price = ?,
                    sal_total = ?
                WHERE sal_id = ?
            """
            cursor.execute(query_update_sale, (product_id, sal_quan, sal_price, sal_total, sal_id))
            
            # Check if the new quantity is less than the original quantity
            if int(sal_quan) < int(original_sale_quan):
                # Calculate the remaining quantity
                remaining_quan = int(original_sale_quan) - (sal_quan)
                remaining_sale = int(sal_quan) 
                # Update the inventory
                query_update_inventory = """
                    UPDATE o_inventory
                    SET pur_quan = pur_quan + ?,
                    sal_quan = sal_quan -?
                    WHERE pro_id = ?
                """
                cursor.execute(query_update_inventory, (remaining_quan,remaining_sale,product_id))
            else:
                remaining_quan = int(original_sale_quan) + (sal_quan)
                remaining_sale = int(sal_quan) 
                # Update the inventory
                query_update_inventory = """
                    UPDATE o_inventory
                    SET pur_quan = pur_quan - ?,
                    sal_quan = sal_quan +?
                    WHERE pro_id = ?
                """
                cursor.execute(query_update_inventory, (remaining_quan,remaining_sale,product_id))

    return redirect('/sale')




def update_sale(request, sal_id):
    # Process the form submission and update the product information in the database
        
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = """
            SELECT * FROM o_sale
            WHERE sal_id = ?
        """
        cursor.execute(query, (sal_id,))
        rows = cursor.fetchone()
        
        # rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        # Prepare the data as a dictionary
        sale = dict(zip(column_names, rows))
        
    return render(request, 'upd_sale.html', {"sale": sale})


        
def display_inventory(request):

    with sqlite3.connect(BASE_DIR/'data.db') as db:
   
        cursor=db.cursor()
        query = "SELECT * FROM o_inventory"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        # total amount

        # Prepare the data as a list of dictionaries
        invent = []
        for row in rows:
            inventory = dict(zip(column_names, row))
            invent.append(inventory)
        print(invent) 
        return render(request, 'inventory.html',{'inventory': invent})
def delete_inventory(request,in_id):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = "DELETE FROM o_inventory WHERE in_id= ?"
        cursor.execute(query, (in_id,))
        messages.success(request, 'Inventory deleted successfully.')
       
      
        return redirect('/inventory')