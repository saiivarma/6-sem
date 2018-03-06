//package server;

import java.io.DataInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class FileServer extends Thread {
	
	private ServerSocket ss;

	/* creating socket for communication*/

	public FileServer(int port) {
		try {
			ss = new ServerSocket(port);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	/* thread.run() method basically used to run thread class*/
	public void run() {
		while (true) {
			try {
				Socket clientSock = ss.accept();// to bind the ip adress and port no
				saveFile(clientSock);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	/* file handling or input calling methods we r using*/
	private void saveFile(Socket clientSock) throws IOException {
		DataInputStream dis = new DataInputStream(clientSock.getInputStream());
		FileOutputStream fos = new FileOutputStream("new.zip");
		byte[] buffer = new byte[1000000000];
		 // insert the file size depend upon the file
		int read = 0;
		int totalRead = 0;
		int remaining = 999999999;
		while((read = dis.read(buffer, 0, Math.min(buffer.length, remaining))) > 0) {
			totalRead += read;
			remaining -= read;
			System.out.println("read " + totalRead + " bytes.");
			fos.write(buffer, 0, read);
		}
		
		fos.close();
		dis.close();
	}
	
	public static void main(String[] args) {
		FileServer fs = new FileServer(7755);
		fs.start();
	}

}