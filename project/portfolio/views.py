from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def portfolio(request):
    return render(request, "pages/portfolio.html")

def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "124512.03"},
    ]
    return render(request, "pages/dashboard.html", context={"data": data})