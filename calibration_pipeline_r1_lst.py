import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from traitlets import Dict, List
from ctapipe.calib import CameraR1CalibratorFactory
from ctapipe.core import Tool


class R1Tester(Tool):
    name = "R1Tester"
    description = "Test R1 Calibrator"

    aliases = Dict(
        dict(
            r1='CameraR1CalibratorFactory.product',
            pedestal_path='CameraR1CalibratorFactory.pedestal_path',
        )
    )
    classes = List([
        CameraR1CalibratorFactory,
    ])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.eventsource = None
        self.r1_calibrator = None
        self.plotter = None

    def setup(self):
        kwargs = dict(config=self.config, tool=self)

        self.r1_calibrator = CameraR1CalibratorFactory.produce(
            eventsource=None, **kwargs
        )

    def start(self):
        for i, ev in enumerate(inputfile_reader_event0):
            self.r1_calibrator.calibrate(ev)
         
    def finish(self):
        pass


if __name__ == '__main__':
    exe = R1Tester()
    exe.run()
