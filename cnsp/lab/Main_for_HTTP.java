package proj;

import java.net.ServerSocket;
import java.net.Socket;

public class Main_for_HTTP {

	public static void main(String[] args) {

	try {
		ServerSocket serverSocket= new ServerSocket(80);
		boolean isStop=false;
		while(!isStop){
			Socket clientSocket=serverSocket.accept();
			System.out.println("client connected");
//			System.out.println("client"+clientsocket.getInetAddress().getHostAddress()+"is connected");
			ClientThread clientthread=new ClientThread(clientSocket);
			clientthread.start();	
		}
	}catch(Exception e) {
		System.out.println(e.toString());
	}
	}
}
