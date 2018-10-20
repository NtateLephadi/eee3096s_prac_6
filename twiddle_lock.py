from gpiozero import LED, Button
from time import sleep
from gpiozero import MCP3008

pot = MCP3008(channel=0)

while True:
    	print(pot.value)
	sleep(0.5)

u_line = LED(23)
l_line = LED(22)
s_line = Button(17)
m_line = Button(27) 

while True:
	s_line.wait_for_press()
	print("s was pressed")

	m_line.wait_for_press()
	print("m was pressed")
	sleep(0.5)
