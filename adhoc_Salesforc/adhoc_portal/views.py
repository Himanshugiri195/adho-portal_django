from django.shortcuts import render
from django import forms

# Create your views here.

from django.http import HttpResponse
import requests
import base64
import json
import requests

# salesforce module 

from simple_salesforce import Salesforce 
from simple_salesforce.exceptions import SalesforceResourceNotFound
from simple_salesforce.exceptions import SalesforceAuthenticationFailed

from .models import Cussel as cs
from .models import Skusel 

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
    
    


def handle_uploaded_file(f):
        body = base64.b64encode(f.read()).decode('utf-8')
        # for chunk in f.chunks():
        #     body = base64.b64encode(chunk.read()).decode('utf-8')
        return body
    
    
    

def home(request):
    db_data = cs.objects.all()
    print(db_data)
    return render(request,'new_ticket_form.html',{'name':'Form'})



def blog(request):
    return render(request,'blog.html',{'name':'Blog One'})


def createtick(request):
    db_data = cs.objects.all()
    skusel = Skusel.objects.all()
    print(skusel)
    return render(request,'new_ticket_form.html',{'name':'New Ticket',"db_data":db_data,"sku_db":skusel})


def checkreq(request):
    return render(request,'checkstat_init.html',{})


def search(request):
    val1 = request.POST['ticketnumber']
    usrname = "bot_mdm_cmd-eur@ab-inbev.com.crm.ssfdoc"
    passwrd = "Welcome@123"
    instance = "https://abinbev-ei-crm--ssfdoc.my.salesforce.com/?"
    sf_domain = "test"
    desc = "this is test six"
    status = "created"
    Case_Origin = "Email"
    Subject = "ABY300619"
    Contact_ID = "0032400000eQHmeAAG"
    Account_ID = "0012400000dGVNdAAO"
    Case_Type = "MDM_Test"
    Record_Type_ID = "01224000000E1phAAC"
    ABI_DTT_Subtype__c = "its a test"
    Owner_ID = "0051q000003n4xmAAA"
    
    try:
        sf = Salesforce(username=usrname, password=passwrd, instance_url = instance, security_token = '', domain=sf_domain)
    
    except SalesforceAuthenticationFailed as a:
        print(a.message)
        return render(request,'result.html',{'result':a.message})
    
    
    
    # contact = sf.Case.get_by_custom_id('CaseNumber', val1)
    try:
        contact = sf.Case.get_by_custom_id('CaseNumber', val1)
        # print(contact['Status'])
        # print(contact['Priority'])
        return render(request,'checkinit_result_succ.html',{'result':contact['Status'],'casenumber':val1,'type':contact['Type'],'subject':contact['Subject'],'priority':contact['Priority'],'credate':contact['CreatedDate']})
    
    
    
    
    
    except SalesforceResourceNotFound as e:
        print(e.content)
        return render(request,'result.html',{'result':'Result not found'})
    
        

    
    

def add(request):
    
    val1 = request.POST['reqcat']
    val2 = request.POST['retype']
    val3 = request.POST['expflow']
    val5 = request.POST['testarea']
    # val7 = request.POST['sku_one']
    # val8 = request.POST['sku_two']
    # val9 = request.POST['sku_three']
    # val6 =request.FILES['myfile'].name
    # body = handle_uploaded_file(request.FILES['myfile'])
    valsold = request.POST['sold_to']
    valshipto = request.POST['ship_to']
    valsku = request.POST['sku_sel']
    form_class = FileFieldForm
    files = request.FILES.getlist('myfile')




    usrname = "bot_mdm_cmd-eur@ab-inbev.com.crm.ssfdoc"
    passwrd = "Welcome@123"
    instance = "https://abinbev-ei-crm--ssfdoc.my.salesforce.com/?"
    sf_domain = "test"
    desc = "Request Category : " + val1 + " \nRequest Type : "+val2+ "\nExporting Flow : "+val3 + "\nSold To : " + valsold + "\nShip to : "+valshipto + "\nSKU Selected : " + valsku + "\nEntered Text : " + val5
    status = "New Request"
    Case_Origin = "Email"
    Subject = "Adhoc Test"
    Contact_ID = "0032400000eQHmeAAG"
    Account_ID = "0012400000dGVNdAAO"
    Case_Type = "ADHOC Request_new_cat"
    Record_Type_ID = "01224000000E1phAAC"
    ABI_DTT_Subtype__c = val1
    Owner_ID = "0051q000003n4xmAAA"
    sf = Salesforce(username=usrname, password=passwrd, instance_url = instance, security_token = '', domain=sf_domain)
    case = sf.Case.create({'Description' : desc, 'Status' : status, 'Origin' : Case_Origin, 'Subject' : Subject, 'ContactId' : Contact_ID, 'AccountId' : Account_ID, 'Type' : Case_Type, 'RecordTypeId' :  Record_Type_ID, 'ABI_DTT_Subtype__c' : ABI_DTT_Subtype__c,'OwnerId' : Owner_ID},headers={'Sforce-Auto-Assign': 'FALSE'})
    sessionId = sf.session_id
    a = sf.Case.get(case['id'])
    # print("Case Number:", a['CaseNumber'], ";Case ID:", case['id'])
    # casenum = a['CaseNumber']
    #
    # body = ""
    # with open(r"C:\Users\Himanshu\Downloads\test_file_three.txt", "rb") as f:
    #     body = base64.b64encode(f.read()).decode('utf-8')
    #
    # filename, file_extension = os.path.splitext(r"C:\Users\Himanshu\Downloads\test_file_three.txt")
    #
    # filenew = val1
    # filenew_name = filenew + file_extension
    #

    #


    #
    # base64_bytes = base64.b64encode(message_bytes)
    # base64_message = base64_bytes.decode('ascii')

    # fields = {'title': val6, 'PathOnClient': 'somepathdoesntmatterthatmuchtome', 'VersionData':body,'Description': desc}
    #
    # contentv3 = sf.ContentVersion.create(fields)['id']
    
    for f in files:
        val6 = f.name
        body = handle_uploaded_file(f)
        response = requests.post(
        'https://abinbev-ei-crm--ssfdoc.my.salesforce.com/services/data/v29.0/sobjects/Attachment/',
        headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % sessionId},
        data=json.dumps({
            'ParentId': case['id'],
            'Name': val6,
            'body': body
        })
        )
    
    
    
    

    

    return render(request,'new_ticket_result.html',{'TicketNumber':val1,'TicketType':val2,'Export':val3,'title':a['CaseNumber']})

    
    
    
    
    