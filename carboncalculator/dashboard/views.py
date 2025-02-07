from django.shortcuts import render
from forms.calculations import calculate_carbon_footprint  # Import existing function

def dashboard_view(request):
    """Dashboard that shows user's carbon footprint and reduction suggestions."""
    carbon_score = calculate_carbon_footprint(request.session)  # Get carbon footprint

    # Example suggestions (modify as needed)
    suggestions = []
    if carbon_score > 500:
        suggestions.append("Consider switching to public transport or carpooling.")
    if carbon_score > 1000:
        suggestions.append("Reduce air travel and use trains for long distances.")
    if carbon_score > 200:
        suggestions.append("Switch to energy-efficient appliances.")
    if carbon_score > 50:
        suggestions.append("Reduce food waste and adopt a plant-based diet.")

    return render(request, 'dashboard/dashboard.html', {
        'carbon_score': carbon_score,
        'suggestions': suggestions,
    })
