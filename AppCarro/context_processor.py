def importe_total_carro(request):
    total = 0
    try:
        #if request.user.is_authenticated:
        for key, value in request.session['carro'].items():
            total += float(value['precio'])
    except:
        pass
    return {'importe_total_carro':total}