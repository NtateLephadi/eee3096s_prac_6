from gpiozero import LED, Button, MCP3008
from time import sleep, time, clock
from character import character
from password import password
import pygame.mixer
from pygame.mixer import Sound
from signal import pause


pygame.mixer.init()

pot = MCP3008(channel=0)
u_line = LED(23)
l_line = LED(22)
s_line = Button(17)
m_line = Button(27)
unlock = Sound("samples/drum_roll.wav")
lock = Sound("samples/misc_burp.wav")

c = character('A', 4.0)
p1 = password([])
p1.add_character(c)
c = character('C', 3.0)
p1.add_character(c)
c = character('A', 3.0)
p1.add_character(c)

print("****** twiddle lock ******")
mode = 'S'
while True:
	if m_line.is_active:
		if mode == 'U':
			mode = 'S'
		elif mode == 'S':
			mode = 'U'
    	if s_line.is_active:
		direction = 'S'
		start = time()
		clock()
		seconds = 2
        	elapsed = 0
		start_duration = time()
		p = password([])
        	while elapsed < seconds:
            		current_direction = pot.value
            		sleep(0.1)
            		next_direction = pot.value
			if next_direction > current_direction + 0.01:
				direction = 'C'
				elapsed = 0
				start = time()
				clock()
            		elif next_direction < current_direction - 0.01:
				direction = 'A'
				elapsed = 0
				start = time()
				clock()
            		else:
				end_duration = time()
				duration = end_duration - start_duration
				duration = duration * 10 // 1
				if(direction != 'S'):
					c = character(direction, duration)
					p.add_character(c)
				start_duration = end_duration
				direction = 'S'
				elapsed = time() - start
		if mode == 'U':
			if p.validate_unsecure(p1)== True:
				u_line.on()
				unlock.play()
				sleep(2)
				u_line.off()
			else:
				l_line.on()
				lock.play()
				sleep(2)
				l_line.off()
		else:
			if p.validate_secure(p1) == True:
				u_line.on()
				unlock.play()
				sleep(2)
				u_line.off()
			else:
				l_line.on()
				lock.play()
				sleep(2)
				l_line.off()
		print(mode)
		print(p.to_string())
		print(p1.to_string())
		print("unsecure: " + str(p.validate_unsecure(p1)))
		print("secure: " + str(p.validate_secure(p1)))
