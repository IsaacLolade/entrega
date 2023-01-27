print("Actividad 56")
while True:
    name = input("Escribe un nombre de usuario: ")
    pswd = input("Escribe una contraseña: ")
    cname = len(name)
    cpswd = len(pswd)
    
    if cname < 6 or cpswd < 8:
        if cname < 6:
            print("¡ERROR! Su nombre de usuario debe contener al menos 6 carácteres.")
        elif cpswd < 8:
            print("¡ER ROR! La contraseña tiene que contenter al menos 8 carácteres.")
        else:
            print("¡ERRO ! Tanto el nombre de usuario como la contraseña tienen menos carácteres de los requeridos")
    elif cname > 12:
        print("¡ERROR! Su n mbre de usuario no puede contener más de 12 carácteres.")
    elif name.isalnum()== False:
        print("¡ERROR! Su nombre de usuario  sólo puede  ser alfanumérico.")
    while True:
        s = 0
        my = 0
        mn = 0
        d = 1
        for i in pswd:
            if i.isspace()==True:
                s += 1
            if i.isupper()==True:
                my += 1
            if i.islower()==True:
                mn += 1
            if i.isdigit()==True:
                d += 1
        if s >= 1:
            print("¡ERROR! La contraseña no puede contener espacios.")
            break
        elif my < 1:
            print("¡ERROR! La contraseña debe contene r mayusculas.")
            break
        elif mn < 1:
            print("¡ERROR! La contraseña debe con tener minusculas.")
            break
        elif d < 1:
            print("¡ERROR! La contra seña debe contener números.")
            break
        else:
            print("Bienv enido ",name)
            print("Su c ontraseña es",pswd)
            break
    else:
        break
    break