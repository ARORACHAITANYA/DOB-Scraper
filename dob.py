import sys
import datetime
import time


try :
    import mechanize
    import cookielib
except:
    print "Mechanize library not installed!"
    exit()

print '\n'
#Define your variables here for the search
start_dob = datetime.datetime(1997, 01, 01, 00, 00, 00)      #date in (yyyy, mm, dd, hh, mm, ss)
end_dob = datetime.datetime(2000, 01, 01, 00, 00, 00)        #date in (yyyy, mm, dd, hh, mm, ss)
roll_no = int(raw_input('Input Roll. No.: '))
website_url = 'http://cbseresults.nic.in/jee_main_zxc/jee_cbse_2017.htm'



roll_no = str(roll_no)      
        
dob = start_dob

found = 0

print '\n'
print 'Checking for: '
    
#DOB loop
while dob < end_dob:

        # Browser
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]  

    # Try to open web page
    try:
        r = br.open(website_url)
    except:
        print 'Error in reading page, please check internet connection!'
        print 'Retrying in 5 seconds ...'
        time.sleep(5)
        continue
                    

    dob_string = dob.strftime('%d/%m/%Y')
        
    # Prepare form
    html = r.read()    
    br.select_form(nr = 0)
   
    br.form['regno'] = roll_no
    br.form['dob'] = dob_string
        
    # Try to submit form
    try:
        br.submit()
    except:
        print 'Error in submitting form, please check internet connection!'
        print 'Retrying in 5 seconds ...'
        time.sleep(5)
        continue
                    
	
        
    dob += datetime.timedelta(days = 1)
    page_source = br.response().read()
	
    print("DOB..... {}".format(dob_string))

    ##Check if result not found
    found_index = 0
    found_index = page_source.find('Not Found')
    if found_index != -1:
        continue

    print '\n'
	
    print 'Found !!!'	
	
    print("DOB = {}".format(dob_string))       
	
    # Break DOB loop since a match was found
    break

    #DOB loop ends
 
if found == 0:
    print '\n'
    print 'Not Found...'
    print 'Check Roll no. provided....'   

print '\n'
print "Finished!"
