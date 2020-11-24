def calculate_tax(**xxx):
    if xxx["salary"] >= 10000 and xxx["salary"] <= 20000:
        print((5/100)*xxx["salary"])
    elif xxx["salary"] > 20000:
        print((10/100)*xxx["salary"])
    elif xxx["age"] < 18:
        print("0")
    elif xxx["current_job_designation"] == "president":
        print("0")
    elif xxx["salary"] < 10000:
        print("0")

calculate_tax(age = 16, salary = 20000, current_job_designation = "Student")

