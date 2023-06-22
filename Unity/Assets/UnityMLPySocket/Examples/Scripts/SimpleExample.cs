using UnityEngine;

public class SimpleExample : MonoBehaviour {
    private IClient m_client;

    private void Start() {
        m_client = new Client();
        m_client.Connect("127.0.0.1", 5000);
        m_client.SendData("Hello World!");
        var response = m_client.ReceiveData();
        Debug.Log($"Received response: {response}");
    }

    private void OnApplicationQuit() {
        m_client.Close();
    }
}