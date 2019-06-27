from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm(request.GET)
    if form.is_valid():
        initial = int(request.GET.get('initial_fee'))
        rate = float(request.GET.get('rate'))
        months_count = int(request.GET.get('months_count'))
        result = round(initial + initial * rate, 2)
        monthly_payment = round(result / months_count)
        return render(request, template,
                      {'form': form, 'result': monthly_payment, 'common_result': result})
    else:
        return render(request, template, {'form': form})
