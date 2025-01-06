select e.name 
from employee e
join(
    select managerId , 
    count(managerId) as direct_reports from employee 
    group by managerId 
    having direct_reports >=5
) m on e.id = m.managerId;