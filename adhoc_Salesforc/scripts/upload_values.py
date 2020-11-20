# import csv
# from adhoc_portal.models import Cus_sel

# def run():
#     fhand = open(r"C:\Users\Himanshu\Downloads\csel_csv.csv")
#     reader = csv.reader(fhand)
#     Cus_sel.objects.all().delete()
    
#     for row in reader:
#         print(row)
#         p,created = Cus_sel.objects.get_or_created(salesorg=row[0])
#         p,created = Cus_sel.objects.get_or_created(importzone=row[1])
#         p,created = Cus_sel.objects.get_or_created(soldto=row[2])
#         p,created = Cus_sel.objects.get_or_created(shipto=row[3])
#         p,created = Cus_sel.objects.get_or_created(shiptoname=row[4])
#         p,created = Cus_sel.objects.get_or_created(shiptocountry=row[5])
#         p,created = Cus_sel.objects.get_or_created(shipcond=row[6])
#         p,created = Cus_sel.objects.get_or_created(payer=row[0])
#         p,created = Cus_sel.objects.get_or_created(payername=row[0])
#         p,created = Cus_sel.objects.get_or_created(profitcen=row[0])
#         p,created = Cus_sel.objects.get_or_created(incoterm=row[0])
#         p,created = Cus_sel.objects.get_or_created(currency=row[0])
#         p,created = Cus_sel.objects.get_or_created(attri=row[0])
        