from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from core.models import Commit
from core import utils

import plotly.express as px


# Create your views here.
@login_required
def commits(request):
    commits = Commit.objects.filter(user=request.user).order_by('created')
    counts = [[] for _ in range(7)]
    dates = [[] for _ in range(7)]

    now = timezone.now()
    start = now - timezone.timedelta(days=364)

    daterange = utils.date_range(start, now)
    for dt in daterange:
        count = commits.filter(created__date=dt).count()
        day_number = dt.weekday()
        counts[day_number].append(count)
        dates[day_number].append(dt)

    import calendar
    days = list(calendar.day_name) 
    first_day = daterange[0].weekday() 
    days = days[first_day:] + days[:first_day]
    fig = px.imshow(
        counts,
        x=dates[0],
        y=days,
        color_continuous_scale='greens',
        height=320,
        width=1300,
    )
    fig.update_layout(plot_bgcolor='white')
    fig.update_traces({'xgap': 5, 'ygap': 5 })
    chart = fig.to_html()
    context = {'chart': chart}
    return render(request, 'commits.html', context)
