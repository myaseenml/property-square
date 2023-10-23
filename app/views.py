from django.shortcuts import render


def index(request):
    return render(request, 'src/Dashboard.html')


def telecalling(request):
    return render(request, 'src/telecalling.html')


def admin(request):
    return render(request, 'src/admin.html')


def agent(request):
    return render(request, 'src/agents.html')


def manager(request):
    return render(request, 'src/manager.html')


def sale_availability(request):
    return render(request, 'src/avalibilityForSale-Rent.html')


def invoice_generation(request):
    return render(request, 'src/invoiceGeneration.html')


def offer_letter(request):
    return render(request, 'src/offerLetter.html')
