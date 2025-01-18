import pandas as pd

def department_highest_salary(dfe: pd.DataFrame, dfd: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(dfe , dfd , how='right' , left_on='departmentId' , right_on='id' , suffixes=('_employee', '_department'))
    max_salary_by_department = df.groupby('name_department')['salary'].transform(max)
    highest_salary_guys = df[df['salary'] == max_salary_by_department ]
    new_db = highest_salary_guys[['name_department' , 'name_employee' , 'salary']]
    new_db.columns = ['Department' , 'Employee' , 'Salary']
    return new_db

