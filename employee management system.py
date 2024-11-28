emp={121:{'name':'raj','address':'pune','mobile_number':9123485756,'salary':20000}}
def dashboard():
    print("""
            1.Add
            2.display
            3.update
            4.delete
            5.filter 
         
           """)
    
def add():
    id=int(input('enter id number:'))
    na=input('enter emp name:')
    add=input('enter emp address:')
    mono=int(input('enter emp mobile number:'))
    sal=int(input('enter emp salary:'))
    emp[id]={'name':na,'address':add,'mobile_number':mono,'salary':sal}

def disply():
    print('-'*106)
    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('id','name','address','mobile_number','salary'))
    print('-'*106)
    for id,val in emp.items():
         print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(id,val['name'],val['address'],val['mobile_number'],val['salary']))
         print('-'*106)
         
def update(roll):
    print("""
           1.name
           2.address
           3.mobilenumber
           4.salary
          
         """)
    ch=int(input('enter your ch:'))
    if ch==1:
        emp[roll]['name']=input('enter name:')
    elif ch==2:    
        emp[roll]['address']=input('enter address:')
    elif ch==3:     
        emp[roll]['mobile_number']=int(input('enter mobile number:'))
    elif ch==4:  
        emp[roll]['salary']=int(input('enter salary:'))
    else:
        print('invalid input') 
    return 'updated successfully....'          


def delete(roll):
    del emp[roll]
    return 'deleted successfully...'
    
def filtr():
    print("""
             1.name
             2.address
             3.mobile number
             4.salary
            
          """)   
    ch=int(input('enter your choise:')) 
    if ch==1:
        na=input('enter name:')
        filter = lambda val: val['name']==na
    elif ch==2:
        add=input('enter address:')
        filter = lambda val: val['address']==add
    elif ch==3:
        mn=int(input('enter mobile number:'))
        filter = lambda val: val['mobile_number']==mn
    elif ch==4:
        sal=eval(input('enter salary:'))
        filter = lambda val: val['salary']==sal
    # elif ch==5:
    #     idd=int(input('enter id number:'))    
    #     filter=lambda id: id[val]==idd
    else:
        print('invalid input.')
       
    print('-'*106)
    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('id','name','address','mobile_number','salary'))
    print('-'*106)
    Found=False
    for id,val in emp.items():
         if filter(val):
            print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(id,val['name'],val['address'],val['mobile_number'],val['salary']))
            print('-'*106)
            Found=True
         if not Found: 
          print('invalid data..') 
    return 'sort successfully..'              
              
while True:
    print(dashboard())
    ch=int(input('enter choise:'))
    if ch==1:
        print (add())
    elif ch==2:
        print(disply())    
    elif ch==3:
        inp=int(input('enter id number'))
        print(update(inp))   
    elif ch==4:
        i=int(input('enter id number'))
        print(delete(i))
    elif ch==5:
        print(filtr())    
