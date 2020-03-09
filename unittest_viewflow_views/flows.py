from viewflow import flow
from viewflow.base import Flow, this

from .views import SampleCreateView, SampleUpdateViewOne, SampleUpdateViewTwo


class SampleFlow(Flow):

    start = flow.Start(SampleCreateView).Next(this.update_one)

    update_one = flow.View(SampleUpdateViewOne).Next(this.update_two)

    update_two = flow.View(SampleUpdateViewTwo).Next(this.end)

    end = flow.End()


