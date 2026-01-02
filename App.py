tenants = [

    {
    "name" :'Jack Brown',
    "apartment_number": 1,
    "apartment_type": "1 Bedroom flat",
    "rent_amount": 350000,
    "amount_paid": 20000,
    "due_date" : "20th June 2026",},

    {"name" :'Mary Jay',
    "apartment_number": 2,
    "apartment_type": "1 Bedroom flat",
    "rent_amount": 350000,
    "amount_paid": 25000,
    "due_date" : "20th June 2026",},

    {"name" :"Glory flares",
    "apartment_number": 3,
    "apartment_type": "1 Bedroom flat",
    "rent_amount": 350000,
    "amount_paid": 10000,
    "due_date" : "20th June 2026.",},

]

def view_tenants(tenants_list):
    print("\nAll Tenants")

    for i in range (len(tenants_list)):
        tenant_names = tenants_list[i]["name"]
        print(f"{i+1}){tenant_names}")

    

    try: 
        user_input = int(input("Input a tenant index number: ") ) - 1
        if user_input < 0 or user_input>= len(tenants_list):
            print (f"Invalid selection. Please choose a number between 1 and {len(tenants_list)}.")
            return       

        else:

            selected_tenant = tenants_list [user_input ]
            tenant_name      = selected_tenant["name"]
            tenant_ap_number = selected_tenant["apartment_number"]
            tenant_ap_type   = selected_tenant ["apartment_type"]
            tenant_ra        = selected_tenant["rent_amount"]
            tenant_dd        = selected_tenant["due_date"]
            print (f"Name: {tenant_name}\nApartment Number: {tenant_ap_number}\nApartment Type: {tenant_ap_type}\nRent AMount: {tenant_ra}\nDue Date: {tenant_dd}")
            


    except : 
        print (f"Error occured!! There are only {len(tenants_list)} Tenants in this Building, Please enter a number (e.g., 1, 2, 3).")
        
view_tenants(tenants)

