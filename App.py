# make a tenant "list" with tenant info and inside list key payments should also be list of dicts containing history of  payments
#  which will have amout and date as the keys
tenants = [

    {
    "name" :'Jack Brown',
    "apartment_number": 1,
    "apartment_type": "1 Bedroom flat",
    "rent_amount": 350000, 
 # processing a logic instead of having a fixed amount paid the amount paid would be gotten from series of payments   
 # first we work with the payment history feature with Jack brown and leave others as fixed
    "payments": [{
        "amount": 20000,
        "date": "2027-03-23" 
    }, {
         "amount": 40000,
        "date": "2027-03-28"       
    }],   
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



#TODO: Function to display tenant info based on a user request by inputing index
def view_tenants(tenants_list):
    # printing all tenants name with index 
    print("\nAll Tenants")

    # loop throught the list using the length of the list of tenant and use the index from the len to able get the name from the 
    # dict in the list
    for i in range (len(tenants_list)):
        tenant_names = tenants_list[i]["name"]
        print(f"{i+1}){tenant_names}")

    
#add a try and except to avoid the code from crashing, incase when user inputs a letter or symbols. 

    try: 
        # asking user to input an index to get the info of the tenant they wish to see
        # then since the index printed will be from 1 to lenght of tenant_list then we subtract -1 to match the index of the list:
        user_input = int(input("Input a tenant index number: ") ) - 1

        # a condition to check the int value the user entered which should be among the len of the teanant_list
        #if not return an error and inform user to input number from 1 to the length of tenants_list
        if user_input < 0 or user_input>= len(tenants_list):
            print (f"Invalid selection. Please choose a number between 1 and {len(tenants_list)}.")
            return       

        else:

            # a selected_tenant which is a dict of the selected tenants user selects from the list displayed
            selected_tenant = tenants_list [user_input ]

           #save the tenant info in various variables
            tenant_name      = selected_tenant["name"]
            tenant_ap_number = selected_tenant["apartment_number"]
            tenant_ap_type   = selected_tenant ["apartment_type"]
            tenant_ra        = selected_tenant ["rent_amount"]
            tenant_dd        = selected_tenant["due_date"]

            #get the values of the amount in the payments list, add them to a list and then sum to get total amount paid
            amount =[]            
            for payment in selected_tenant["payments"]:
                amount.append(payment["amount"])
            total_paid = sum (amount)
            
            #goal: add remaining amount to pay from if tenant paid less
            #compare the rent amount and the total paid to get the remaining amount
            remaining_amount= tenant_ra - total_paid


            #goal: to check if the user made an overpayment of the rent:
            # substract the total paid amount from the rent amount and indicate this on the print below. 
            overpaid = 0
            overpaid_status = "No"
            if total_paid > tenant_ra:
                remaining_amount = 0
                overpaid += total_paid - tenant_ra
                overpaid_status = "Yes"
            pass
                 
            

            #print out all info of selected teanant. 
            print(
                f"Name: {tenant_name}\n"
                f"Apartment number: {tenant_ap_number}\n"
                f"Apartment Type: {tenant_ap_type}\n"
                f"Rent Amount: ₦{tenant_ra}\n"
                f"Total Amount Paid: ₦{total_paid}\n"
                f"Balance Amount: ₦{remaining_amount}\n"
                f"Overpaid Amount: ₦{overpaid}\n"
                f"Overpaid Status: {overpaid_status}\n"
                f"Due Date: {tenant_dd}\n"
                )
            

            # Here the Land lady or tenant will be able view history of payments for the rented apartment.
            payment_history = input ("Do you wish to view Payment History (yes/no): ").lower()
            
            #goal is the user inputs yes we print our the amount paid and the date when it was paid
            if payment_history == "yes":
                #goal extract the content of the payements list
                history = selected_tenant["payments"]
                # looping through all payments, dates and print then printing them out. using the enumerate 
                #function to for the numbering
                for i, all_payments in enumerate(history,1):
                    history_amount= all_payments["amount"]
                    history_date = all_payments["date"]
                    print(
                     f"{i}. Amount: ₦{history_amount}\n"
                     f"     Date: {history_date}\n"
                 )

            


    except : 
        print (f"Error occured!!! There are only {len(tenants_list)} Tenants in this Building, Please enter a number (e.g., 1, 2, 3).")
        
view_tenants(tenants)

