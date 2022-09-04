DATA = [
 {
    'name': 'Facundo',
    'age': 72,
    'organization': 'Platzi',
    'position': 'Technical coach',
    'language': 'python'
 },
 {
    'name': 'Luisana',
    'age': 33,
    'organization': 'Goblant',
    'position': 'UK Designer',
    'language': 'Javascript'
 },
 {
    'name': 'Hector',
    'age': 19,
    'organization': 'Platzi',
    'position': 'Associate',
    'language': 'ruby'
 },
 {
    'name': 'Isabella',
    'age': 30,
    'organization': 'Platzi',
    'position': 'QA Manager',
    'language': 'Java'
 }
]
def run ():
    all_python_devs = [worker["name"]for worker in DATA if worker ["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18 , DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    #old_people =list(map(lambda worker: worker / {"old": worker["age"] > 70}, DATA ))
    #for worker in all_python_devs:
    for worker in adults:
        print(worker)

if __name__ == '__main__':
    run()
       
    
