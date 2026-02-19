def hitung_denda(haritelat):
    if haritelat > 0:
        return haritelat * 2000
    else:
        return 0
    
def hitung_saldo(kasmasuk, kaskeluar, denda):
    return kasmasuk - kaskeluar - denda
