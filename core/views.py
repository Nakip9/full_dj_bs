from django.shortcuts import render

from memberships.models import MembershipPlan
from schedules.models import GymClass


def home(request):
    plans = MembershipPlan.objects.filter(is_active=True).order_by("price")[:3]
    classes = (
        GymClass.objects.select_related("category")
        .filter(is_published=True)
        .order_by("start_time")[:6]
    )
    return render(request, "core/home.html", {"plans": plans, "classes": classes})


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")
