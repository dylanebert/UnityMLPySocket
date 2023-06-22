public interface IClient {
    void Connect(string host, int port);
    void SendData(string data);
    string ReceiveData();
    void Close();
}
