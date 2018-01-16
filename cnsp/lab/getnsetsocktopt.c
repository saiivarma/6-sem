#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<netinet/tcp.h>

int main(int argv, char* args[]){
        int sockfd,maxseg,nodelay,sendbuff,optlen;
        sockfd=socket(AF_INET,SOCK_STREAM,0);
        if(sockfd<0)
        {
                perror("socket");
                exit(0);
        }
        optlen=sizeof(maxseg);
        getsockopt(sockfd,IPPROTO_TCP,TCP_MAXSEG,(char *)&maxseg,&optlen);
        printf("\n TCP maxseg=%d",maxseg);
        optlen=sizeof(nodelay);
        getsockopt(sockfd,IPPROTO_TCP,TCP_NODELAY,(char *)&maxseg,&optlen);
        printf("\n TCP nodelay=%d",nodelay);
        sendbuff=12324;
        setsockopt(sockfd,SOL_SOCKET,SO_SNDBUF,(char *)&sendbuff,sizeof(sendbuff));
        optlen=sizeof(sendbuff);
        getsockopt(sockfd,SOL_SOCKET,SO_SNDBUF,(char *)&sendbuff,&optlen);
        printf("\n send buffer size=%d\n",sendbuff);

}
