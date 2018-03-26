//package client;

import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.Socket;

public class FileClient {
	
	private Socket s;
	
/*accepting ip add $ port no $ file name*/

	public FileClient(String host, int port, String file) {
		try {
			s = new Socket(host, port);
			sendFile(file);
		} catch (Exception e) {
			e.printStackTrace();
		}		
	}
	
	public void sendFile(String file) throws IOException {
		DataOutputStream dos = new DataOutputStream(s.getOutputStream());
		FileInputStream fis = new FileInputStream(file);
		byte[] buffer = new byte[4096];
		
		while (fis.read(buffer) > 0) {
			dos.write(buffer);
		}
		
		fis.close();
		dos.close();	
	}
	
	public static void main(String[] args) {
		FileClient fc = new FileClient(args[0], 7755, args[1]);//args[0] is host ip addr, args[1] is file name(.zip file)
	}

}
