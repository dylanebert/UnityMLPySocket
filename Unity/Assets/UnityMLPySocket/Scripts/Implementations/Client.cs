using System.Net.Sockets;
using System.Text;

public class Client : IClient {
    private TcpClient m_client;
    private NetworkStream m_stream;

    public void Connect(string host, int port) {
        m_client = new TcpClient(host, port);
        m_stream = m_client.GetStream();
    }

    public void SendData(string data) {
        if (m_client == null || m_stream == null) {
            throw new System.Exception("Client not connected");
        }
        byte[] bytes = Encoding.ASCII.GetBytes(data);
        m_stream.Write(bytes, 0, bytes.Length);
    }

    public string ReceiveData() {
        if (m_client == null || m_stream == null) {
            throw new System.Exception("Client not connected");
        }
        byte[] bytes = new byte[1024];
        int bytesRead = m_stream.Read(bytes, 0, bytes.Length);
        return Encoding.ASCII.GetString(bytes, 0, bytesRead);
    }

    public void Close() {
        m_stream?.Close();
        m_client?.Close();
    }
}