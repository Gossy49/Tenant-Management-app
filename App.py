#importing Json
import json 

#add a dict with building and adress
buildings = [
    {   "name": "Buiding 1",
        "address": "Kujawska 10 "
    },
    {   "name": "Buiding 2",
        "address": "Zamenhofa 13"
    }, 
]

#A function to save the tenants details in a Json File
def save_tenants (t_list):
    with open('tenants.json', 'w') as json_file:
        json.dump(t_list,json_file,indent= 2)

# goal a function to load tenants from teh json file
def load_tenants():
    try :
        with open('tenants.json', 'r') as json_file:
            data = json.load(json_file)
            return data

    except FileNotFoundError:
        print ("File Not Found")
        return []
        

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
            tenant_email     = selected_tenant["email"]
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
                f"email: {tenant_email}\n"                
                f"Apartment number: {tenant_ap_number}\n"
                f"Apartment Type: {tenant_ap_type}\n"
                f"\nRent Amount: ₦{tenant_ra}\n"
                f"Total Amount Paid: ₦{total_paid}\n"
                f"Balance Amount: ₦{remaining_amount}\n"
                f"\nOverpaid Amount: ₦{overpaid}\n"
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



#function to catch error incase user input a text inplace of aparmnet number and rent amunt
def ask_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number")

#goal a function to add new tenants to the app
def add_tenant(tenants, building_selected):
    #ask users for details of the new tenant
    
    name = input ("Enter a name: ")
    email = input ("Enter a valid Email Adress: ")
    apartment_number = ask_int ("Enter an Apartment Number: ")
    apartment_type = input("Enter Apartment Type: ")
    rent_amount = ask_int("Enter Rent Amount: ")
    due_date = input("Enter Due Date: ")

    #new dict created with the new tenant info
    new_tenant = {"building": building_selected,
    "name" :name,
    "email": email,
    "apartment_number": apartment_number,
    "apartment_type": apartment_type,
    "rent_amount": rent_amount,
    "payments": [],   
    "due_date" : due_date,}

    #append details to the tenant list 
    tenants.append(new_tenant)
    print("New Tenant Added.")
    print("Saved under building:", new_tenant["building"])
    



    
#goal a function to send house contract to selected tenant
def send_contract():
    pass
#goal: a function to view Tenant Reports concerning issues faced in the house
def tenant_report():
    pass
#goal:a function to send receipt of latest payment to tenants after payments of rent
def record_payments(filtered_tenants_list,tenant_database):
        # printing all tenants name with index 
    print("\nTenants Available")

    # loop throught the list using the length of the list of tenant and use the index from the len to able get the name from the 
    # dict in the list
    for i in range (len(filtered_tenants_list)):
        tenant_names = filtered_tenants_list[i]["name"]
        print(f"{i+1}){tenant_names}")
    

#add a try and except to avoid the code from crashing, incase when user inputs a letter or symbols. 

    try: 
        # asking user to input an index to get the info of the tenant they wish to see
        # then since the index printed will be from 1 to lenght of tenant_list then we subtract -1 to match the index of the list:
        user_input = int(input("\nInput a tenant index number to choose a tenant : ") ) - 1

        # a condition to check the int value the user entered which should be among the len of the teanant_list
        #if not return an error and inform user to input number from 1 to the length of tenants_list
        if user_input < 0 or user_input>= len(filtered_tenants_list):
            print (f"Invalid selection. Please choose a number between 1 and {len(filtered_tenants_list)}.")
            return       
    except: 
        print (f"Error occured!!! There are only {len(filtered_tenants_list)} Tenants in this Building, Please enter a number (e.g., 1, 2, 3).")
        return

    # a selected_tenant which is a dict of the selected tenants user selects from the list displayed
    tenant_selected = filtered_tenants_list [user_input ]
    new_payment = int(input ("Enter amount: "))
    new_paymen_date = input("Enter Date (YYYY-MM-DD): ")

    new_amount_details  = {"amount": new_payment ,"date": new_paymen_date}
    
    tenant_selected["payments"].append(new_amount_details)

    #save the tenant new Payment record without formatting the whole database. 
    save_tenants(tenant_database)
    print ("Payment Details was Saved Successfully")

    send_process = input("Do you wish to generate Receipt Pdf and foward to email (y/n)? ").lower()

    # condition to check the what user inputed previously on send process
    if send_process == "y" :
 
        latest_amount = new_payment
        latest_date   = new_paymen_date
        filtered_tenants_name  = tenant_selected ["name"]
        filtered_tenants_email = tenant_selected["email"] 

        print(f"\nAmount Received:₦{latest_amount} from {filtered_tenants_name}on {latest_date}. ")
        print(f"Sending Receipt in Pdf to Email:{filtered_tenants_email}")

    else: 
        print("Email failed to Send")
            


#goal:function give details about tenant stautus: eg Rent expired and here we have the grace periods 
def tenant_status():
    pass
#goal: display the buildings list and user could choose which building info they wish to see


#function to get tenants in a certain building. 
def get_building_tenants(tenants, selected_building):
    
    building_tenants = []
    for items in tenants:
        if items["building"] == selected_building:
            building_tenants.append(items)
        
    return building_tenants


tenants = load_tenants()
print ("             Welcome Mrs Abby   ")


#loop through building list 
for i,all_buildings in enumerate(buildings,1):
    all_buildings_name = all_buildings["name"]
    all_buildings_address = all_buildings["address"]
    print (f"{i}. {all_buildings_name}\n   Address:{all_buildings_address}")


# load tenant info from the tenants.json file created.
tenants = load_tenants()
# here user selects a building
app_welcome = int(input("\nEnter a building number to view more: "))-1



#print out of all options for both Building 1 and building 2 
if app_welcome == 0 or  app_welcome == 1:
        print("\n")
        print(f"       Welcome to 'Building {app_welcome + 1}'")
        print(f"{1}. View Tenants Info ")
        print (f"{2}. Add Tenant")
        print (f"{3}. Send House Contract")
        print (f"{4}. Record Payments")
        print(f"{5}. View Tenant status")
        print(f"{6}. Tenant Reports")
        print(f"{7}. Send General info to all Tenants in 'Building {app_welcome + 1}' ")





#goal to ask user to enter an index number to choose an option above
app_options = int(input("\nEnter a number from 1-7 to selcet and view more from options: "))      
if app_options == 1:

    #goal: When user selects Building 1 or 2, “View Tenants Info” shows only tenants in that building.
    #function to get only tenants in that build is called here
    selected_building= app_welcome + 1


    building_tenants = get_building_tenants(tenants,selected_building)
    # if building tenants is an empty list we assume there are no tenants there yet. 
    if not building_tenants:
        print("No tenants found for this building yet.")
    else:
        view_tenants(building_tenants)


#goal to able to add the Tenant Manually from Landlady view
elif app_options == 2 :
    #calling the add tenant
    selected_building= app_welcome + 1
    add_tenant(tenants, selected_building)
    save_tenants(tenants)
    

# For sending Receipts options
elif app_options == 4 :
    # making sure we are in the selected building the user needed 
    selected_building = app_welcome + 1

    # get the tenants  in the selected building
    building_tenants = get_building_tenants(tenants,selected_building)

    #add to give info about there being a tenant in the 
    if not building_tenants:
        print("No tenants found for this building yet.")
    else:
        record_payments(building_tenants, tenants)

         
    

# save_tenants(tenants)
# print("Initial tenants saved to JSON.")


# view_tenants(tenants)

