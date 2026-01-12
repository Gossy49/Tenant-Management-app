#add a dict with building and adress
buildings = [
    {   "name": "Buiding 1",
        "address": "Kujawska 10 "
    },
    {   "name": "Buiding 2",
        "address": "Zamenhofa 13"
    }, 
]


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

# updated the payment section for mary to perfomr the completed.
    {"name" :'Mary Jay',
    "apartment_number": 2,
    "apartment_type": "1 Bedroom flat",
    "rent_amount": 350000,
    "payments": [{
        "amount": 300000,
        "date": "2027-03-23" 
    }, {
         "amount": 50000,
        "date": "2027-03-28"       
    }],   
    "due_date" : "20th June 2026",},

#assumed all have the same due date and we asssume Glory overpaid
    {"name" :"Glory flares",
    "apartment_number": 3,
    "apartment_type": "1 Bedroom flat",
    "rent_amount": 350000,
    "payments": [{
        "amount": 350000,
        "date": "2027-03-23" 
    }, {
         "amount": 35000,
        "date": "2027-03-28"       
    }],   
    "due_date" : "20th June 2026",}
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
        user_input = int(input("\nInput a tenant index number: ") ) - 1

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
            
                 
            

            #print out all info of selected teanant. 
            print(
                f"\nName: {tenant_name}\n"
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

#goal a function to send house contract to selected tenant
def send_contract():
    pass
#goal: a function to view Tenant Reports concerning issues faced in the house
def tenant_report():
    pass
#goal:a function to send receipts to tenants after payments of rent
def send_receipts():
    pass

#goal:function give details about tenant stautus: eg Rent expired and here we have the grace periods 
def tenant_status():
    pass
#goal: display the buildings list and user could choose which building info they wish to see
print ("             Welcome Mrs Abby   ")

#loop through building list 
for i,all_buildings in enumerate(buildings,1):
    all_buildings_name = all_buildings["name"]
    all_buildings_address = all_buildings["address"]
    print (f"{i}. {all_buildings_name}\n   Address:{all_buildings_address}")

app_welcome = int(input("\nEnter a building number to view more: "))-1


#print out of all options for both Building 1 and building 2 
if app_welcome == 0 or  app_welcome == 1:
        print("\n")
        print(f"       Welcome to 'Building {app_welcome + 1}'")
        print(f"{1}. View Tenants Info ")
        print (f"{2}. Add Tenant")
        print (f"{3}. Send House Contract")
        print (f"{4}. Tenant Reports")
        print(f"{5}. Send Receipts")
        print(f"{6}. View Tenant status")
        print(f"{7}. Send General info to all Tenants in 'Building {app_welcome + 1}' ")


#goal to ask user to enter an index number to choose an option above
app_options = int(input("\nEnter a number from 1-7 to selcet and view more from options: "))      
if app_options == 1:
    view_tenants(tenants)




# view_tenants(tenants)

