# Makefile
all: prac_6_lphtum003_jhrmoh002
	prac_6_lphtum003_jhrmoh002: prac_6_lphtum003_jhrmoh002.o
	gcc -o $@ $+
prac_6_lphtum003_jhrmoh002.o : prac_6_lphtum003_jhrmoh002.s
	as -g -mfpu=vfpv2 -o $@ $<
clean:
	rm -vf prac_6_lphtum003_jhrmoh002 *.o
