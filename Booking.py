#!/bin/usr/env python

#global declaration of booking as a list
book_list=[]

#function check availability if the facility at perticular date and time
def check_availability(facility,date,time_from,time_to):
    global book_list
    if len(book_list)==0:
        return 1
    else:
        for i in book_list:
            if i[0]==facility and i[1]==date and ((time_from>=i[2] or time_from<=i[2]) and (time_to<=i[3] or time_to>=i[3])):
                flag=0
            else:
                flag=1
        if flag==0:
            print "\tNote Available"

        if flag==1:
            return 1

#fnctiion books facility     
def book_facility(facility,date,time_from,time_to):
    book=[facility,date,time_from,time_to]
    rent=getrent(facility,time_from,time_to)
    book_time=time_to-time_from
    total=rent*book_time
    
    try:
        book_list.append(book)
        print "\t\tBooked"
        print "\t\tRate for 1 hour ",rent
        print "\t\tBooking Time ",book_time,
        print "hours"
        print "\t\tTotal payable amount is Rs.",total
    except:
        print "\tSome error ocurred while proccessing,please try agian..."


def getrent(facility,time_from,time_to):
    """this function gets rent of perticular 
        time slot"""

    if facility == "tennis court":
        if time_from>=10 and time_to<=16:
            rent=100
        if time_from>=16 and time_to<=24:
            rent=500
        if time_from>=1 and time_to<=10:
            rent=50

    if facility == "club house":
        if time_from>=10 and time_to<=16:
            rent=300
        if time_from>=16 and time_to<=24:
            rent=800
        if time_from>=1 and time_to<=10:
            rent=100

    return rent

#this convert function is responsible for getting time in floating
#point format e.g if time is 10:30 then function convert it to 10.3
def convert(time):
    time=time.split(':')
    time=time[0]+'.'+time[1]
    time_f=float(time)

    return time_f

#Simple authentication function 
#with username and password provided
def authenticate():

    username="vinay"
    password="password"

    print "\n\t\t\tFacility Booking System"
    print "\tLogin:\n"
    user=raw_input("\tEnter Username:  ")
    passwd=raw_input("\tEnter password:  ")
        
    if user == username and password == passwd:
        return 1

#Displaying Menu and input prompt
def start():
    print "\n\tWelcome ,"
    print "\n\tFor Booking available facility enter input in the following format:\
        \n\tif You want to book a Tennis Court the input should be as follows:\
    \n\t***NOTE-Time is in 24-hours format(i.e for 4 pm -> 16:00)\
    \n\n\te.g- 'Tennis Court,2012-10-27,10:00,16:00' without any quotes\n\n"
    print "\tAvailable Facilities\
        \n\t*Tennis Court\
        \n\t*Club house\n"

    while(1):
        facility=raw_input("Your input >>  ")
        facility=facility.split(',')

        facility_available=facility[0].lower()
        date=facility[1]    
        time_f=convert(facility[2])
        time_t=convert(facility[3])

        if check_availability(facility_available,date,time_f,time_t):
            book_facility(facility_available,date,time_f,time_t)

if __name__=="__main__":

    if authenticate():
        start()
