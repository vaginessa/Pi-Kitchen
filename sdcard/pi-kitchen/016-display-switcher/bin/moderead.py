modedmt='[
{ "code":4, "width":640, "height":480, "rate":60, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":5, "width":640, "height":480, "rate":72, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":6, "width":640, "height":480, "rate":75, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":9, "width":800, "height":600, "rate":60, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":10, "width":800, "height":600, "rate":72, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":11, "width":800, "height":600, "rate":75, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":16, "width":1024, "height":768, "rate":60, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":17, "width":1024, "height":768, "rate":70, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":18, "width":1024, "height":768, "rate":75, "aspect_ratio":"4:3", "scan":"p", "3d_modes":[] },
{ "code":35, "width":1280, "height":1024, "rate":60, "aspect_ratio":"5:4", "scan":"p", "3d_modes":[] },
{ "code":36, "width":1280, "height":1024, "rate":75, "aspect_ratio":"5:4", "scan":"p", "3d_modes":[] }
]'


import json
availablemodes = json.loads(modedmt)
print("Read 1st item: %s CODE:%s"%(availablemodes[0],availablemodes[0]["code"]))
for mode in availablemodes:
  print("Mode: %s"%(mode["code"]))