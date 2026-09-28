tours=[
    ["Goa",4,12000],
    ["Kashmir",6,22000],
    ["Rajasthan",5,16000],
    ["Delhi-Agra",3,9000]
]


def show_tours():
    print("\n====== TOUR PACAKAGES ======")

    for i in range(len(tours)):
       print(i+1,".",tours[i][0])
       print("Duration:",tours[i][1],"days")
       print("Price:Rs.",tours[i][2])
       
    

       