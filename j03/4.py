import pandas as pd

# student1 = ["alireza", "mohammadi", 14, "0987654321", 18.5]
# student2 = ["saeed", "ahmadi", 15, 18, "1234567890"]

students = {
    "student1" : {
        "name" : {
            "firstname" : "alireza",
            "lastname" : "mohammadi"
        },
        "age" : 14,
        "personalID" : "0987654321",
        "avg" : 18.5,
        "phone" : {
            "mobile" : "09123456789",
            "tel" : "021771633338"
        },
        "sessions" : ["math", "phisics", "chemistry"]
    }
}


# for key, value in students["student1"].items():
#     print(key, "->",  value)

df = pd.DataFrame(students)

print(df)