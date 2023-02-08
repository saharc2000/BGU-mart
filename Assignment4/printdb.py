from persistence import *
def print_table(table, sort_key):
    print(table._table_name.title())
    list_of_rows = table.find_all()
    list_of_rows.sort(key=sort_key)
    for row_val in list_of_rows:
        print(row_val)

def main():
    print_table(repo.activities, lambda x: x.date)
    print_table(repo.branches, lambda x: x.id)
    print_table(repo.employees, lambda x: x.id)
    print_table(repo.products, lambda x: x.id)
    print_table(repo.suppliers, lambda x: x.id)
    
    print("Employees report")
    EmployeesWithSales = repo.execute_command("SELECT employees.id,employees.name,employees.salary,branches.location,SUM(activities.quantity*products.price*-1) FROM activities JOIN employees ON activities.activator_id=employees.id JOIN branches ON employees.branche=branches.id JOIN products ON activities.product_id=products.id GROUP BY activities.activator_id")
    AllEmployees = repo.execute_command("SELECT employees.id,employees.name,employees.salary,branches.location,0 FROM employees JOIN branches ON employees.branche=branches.id")
    CombineEmployeesList = AllEmployees+EmployeesWithSales
    CombineEmployeesList.sort(key=lambda x: x[1])
    for i in range(len(CombineEmployeesList)):
        if i+1!=len(CombineEmployeesList):
            if CombineEmployeesList[i][0]==CombineEmployeesList[i+1][0]:
                if CombineEmployeesList[i][4]==0:
                    continue
        if i>0:
            if CombineEmployeesList[i][0]==CombineEmployeesList[i-1][0]:
                if CombineEmployeesList[i][4]==0:
                    continue
        print(('{} {} {} {}').format(CombineEmployeesList[i][1],str(CombineEmployeesList[i][2]),CombineEmployeesList[i][3],str(CombineEmployeesList[i][4])))
    
    print("\nActivities report")
    Buys = repo.execute_command("SELECT activities.date,products.description,activities.quantity,employees.name,suppliers.name FROM activities JOIN products ON activities.product_id=products.id JOIN suppliers ON activities.activator_id=suppliers.id LEFT JOIN employees ON activities.activator_id=employees.id")
    Sales =  repo.execute_command("SELECT activities.date,products.description,activities.quantity,employees.name,suppliers.name FROM activities JOIN products ON activities.product_id=products.id JOIN employees ON activities.activator_id=employees.id LEFT JOIN suppliers ON activities.activator_id=suppliers.id")
    ActiviesReport=Buys+Sales
    ActiviesReport.sort(key=lambda x: x[0])
    for activity in ActiviesReport:
        print(activity)

if __name__ == '__main__':
    main()