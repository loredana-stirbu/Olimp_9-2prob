s=input("Introduceti prenumele si numele vostru: ")
s1=s.split()
if s1[0]==s1[0].title():
    print("Prenumele a fost introdus corect")
if s1[1]==s1[1].title():
    print("Numele a fost introdus corect")
else:
    print("Numele si Prenumele au fost introduse gresit")
