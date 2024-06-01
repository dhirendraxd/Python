def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        
print_kwargs(name="dhiren", power="laser")
print_kwargs(name="dhiren")
print_kwargs(name="dhiren", power="laser", enemy="ramiro")