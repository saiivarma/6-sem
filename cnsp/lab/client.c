#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
int main(int argc,char *argv[])
{
        int s,t,len,a;
        struct sockaddr_in rem;
        char str[100];
        if(argc!=3)
        {
                printf("usage ./<client_program> address port");
                exit(0);
        }
        s=socket(AF_INET,SOCK_STREAM,0);
        if(s==-1)
        {
                perror("socket creation error");
                exit(1);
        }
        printf("trying to connect to.......%s\n",argv[1]);
        rem.sin_family=AF_INET;
        rem.sin_port=htons(atoi(argv[2]));
        rem.sin_addr.s_addr=inet_addr(argv[1]);
        a=connect(s,(struct sockaddr *)&rem,sizeof(rem));
        if(a==-1)
        {
                perror("connection unsuccessful");
                exit(1);
        }
        printf("connection sucessful\n");
        while(printf("->"),fgets(str,100,stdin),!feof(stdin))
        {
                if(send(s,str,strlen(str),0)==-1)
                {
                        perror("error sending the data");
                        exit(1);
                }
                if((t=recv(s,str,100,0))>0)
                  {
                        str[t]='\0';
                        printf("echo->%s\n",str);
                }
                else
                {
                        if(t<0)
                                perror("error receiving data");
                        else
                                printf("server closed connection\n");
                        exit(1);
                }
        }
        close(s);
        return 0;
}
