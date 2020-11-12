from aws_xray_sdk.core import xray_recorder

    xray_recorder.begin_segment('x-ray-recorder')

        print ('hello world!')
    
    xray_recorder.end_segment()