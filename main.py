def ipcalc():
    mask = input("Podaj maskę podsieci: ")
    mask = mask.split(".")
    hosts = 1
    bits = 0
    for octet in mask:
        byte = int(octet)
        hosts *= (256 - byte)
        print(bin(byte))
        if byte > 0:
            bits += len(bin(byte))-2
    print("Hostów w sieci: ", hosts - 2)
    print("Skrócony zapis: /", bits)

ipcalc()
