from django.shortcuts import render, redirect
from .forms import PersonalInfoForm, TravelForm, WasteForm, EnergyForm, ExpenditureForm
from .calculations import calculate_carbon_footprint

def personal_info_view(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            request.session['personal_info'] = form.cleaned_data
            return redirect('travel')
    else:
        form = PersonalInfoForm()
    return render(request, 'forms/personal_info.html', {'form': form})

def travel_view(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            request.session['travel'] = form.cleaned_data
            return redirect('waste')
    else:
        form = TravelForm()
    return render(request, 'forms/travel.html', {'form': form})

def waste_view(request):
    if request.method == 'POST':
        form = WasteForm(request.POST)
        if form.is_valid():
            request.session['waste'] = form.cleaned_data
            return redirect('energy')
    else:
        form = WasteForm()
    return render(request, 'forms/waste.html', {'form': form})

def energy_view(request):
    if request.method == 'POST':
        form = EnergyForm(request.POST)
        if form.is_valid():
            request.session['energy'] = form.cleaned_data
            return redirect('expenditure')
    else:
        form = EnergyForm()
    return render(request, 'forms/energy.html', {'form': form})


def expenditure_view(request):
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            request.session['expenditure'] = form.cleaned_data
            return redirect('dashboard')  # ✅ Redirect to the dashboard after last step
    else:
        form = ExpenditureForm()
    return render(request, 'forms/expenditure.html', {'form': form})

def result_view(request):
    """ Display the final carbon footprint result """
    carbon_score = calculate_carbon_footprint(request.session)  # ✅ Compute the result
    return render(request, 'forms/result.html', {'carbon_score': carbon_score})  # ✅ Pass to template


