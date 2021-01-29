import matplotlib as plt
import mpld3
from django.shortcuts import render
import numpy as np

from djangoapp.calcapp import top
from djangoapp.calcapp.top import XAxis, YAxis
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'calcapp/post_list.html', {'posts': posts})


def image_show(request):
    fig = plt.figure()
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-32, 32, 0.8)
    plt.plot(x, top.f)
    plt.plot(x, XAxis(0, 0, x))
    plt.plot(YAxis(0, 0, x), y)
    plt.savefig("plot.png")
    figHtml = mpld3.fig_to_html(fig=fig)
    result = {'figure': figHtml}
    return render(request,"calcapp/image_show.html", result)