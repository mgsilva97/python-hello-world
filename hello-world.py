#!/usr/bin/env python
from aws_xray_sdk.core import xray_recorder
xray_recorder.begin_segment('x-ray-recorder')
xray_recorder.begin_subsegment('x-ray-recorder-sub')
print ('hello world!')
xray_recorder.end_subsegment()
xray_recorder.end_segment()