#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>


int main(int argc, char *argv[])
{

	int i, j; 
	struct addrinfo hints, *ai, *ai0;
	struct sockaddr_in *ip_access4;
	struct sockaddr_in6 *ip_access6;

	char ip4[INET_ADDRSTRLEN];
	char ip6[INET6_ADDRSTRLEN];

	if (argc < 2) {
		printf("Usage: %s <hostname>\n", argv[0]);
		return 1;
	}

	memset(&hints, 0, sizeof(hints));
	hints.ai_family    = PF_UNSPEC;
	hints.ai_socktype  = SOCK_STREAM;

	for (j = 1; j < argc; j++) {

		if ((i = getaddrinfo(argv[j], "8080", &hints, &ai0)) != 0) {
			printf("Unable to look up IP address: %s", gai_strerror(i));
			return 2;
		}

		for (ai = ai0; ai != NULL; ai = ai->ai_next) {
			if (ai->ai_family == AF_INET) {
				printf("%s IPv4 ", argv[j]);
				ip_access4 = (struct sockaddr_in *) ai->ai_addr;
				inet_ntop( AF_INET, &ip_access4->sin_addr, ip4, INET_ADDRSTRLEN );
				printf("%s\n", ip4);
			}

			if (ai->ai_family == AF_INET6) {
				printf("%s IPv6 ", argv[j]);
				ip_access6 = (struct sockaddr_in6 *) ai->ai_addr;
				inet_ntop( AF_INET6, &ip_access6->sin6_addr, ip6, INET6_ADDRSTRLEN );
				printf("%s\n", ip6);
			}
		}
	}

	return 0;
}