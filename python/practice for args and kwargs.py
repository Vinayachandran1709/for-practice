def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("Mr","Vinaya", "Chandran",street="3/3, Govinda Singh Street",city="Chennai",state="Tamilnadu",country="India")