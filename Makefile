CC = clang
CFLAGS = -W -Wall

dnslookup : 
	$(CC) $(CFLAGS) dnslookup.c -o dnslookup

.PHONY: clean
clean:
	rm dnslookup