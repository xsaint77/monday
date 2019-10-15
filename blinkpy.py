from blinkpy import blinkpy


blink = blinkpy.Blink(username='anthonygranillo7@gmail.com', password='J@!den2016', refresh_rate=30)

blink.start()

for name, camera in blink.cameras.items():
  print(name)                   # Name of the camera
  print(camera.attributes['temperature'])      # Print available attributes of camera
  print(camera.attributes['motion_enabled'])
  print(camera.attributes['motion_detected'])
